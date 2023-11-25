import requests
import time
from bs4 import BeautifulSoup
import csv


#function to check a string is a digit or if a string with it's comma replaced is a digit and 
#it alse ends up converting the string to integer as its return value.

with open("playerDetailedStats_46.csv",mode = "w",newline = '',encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Player Name","Nationality","Team","Kit Number","League","Height(inches)","Height(cm)","Weight(lbs)","Weight(kg)",
"Best Position","Best Foot","Weak Foot","Skill moves","International Reputation",'Crossing', 'Finishing', 'Heading Accuracy', 'Short Passing',
'Volleys', 'Dribbling', 'Curve', 'FreeKick Accuracy', 'Long Passing', 'Ball Control', 'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 
'Balance', 'Shot Power', 'Jumping', 'Stamina', 'Strength', 'Long Shots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
'Composure', 'Marking', 'Standing Tackle', 'Sliding Tackle', 'GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes',
'Striker (ST)', 'Left Wing (LW)', 'Left Forward (LF)', 'Center Forward (CF)', 'Right Forward (RF)', 'Right Wing (RW)', 'Center Attacking Midfielder (CAM)',
'Left Midfielder (LM)', 'Center Midfielder (CM)', 'Right Midfielder (RM)', 'Left Wing Back (LWB)', 'Center Defensive Midfielder (CDM)', 'Right Wing Back (RWB)',
'Left Back (LB)', 'Center Back (CB)', 'Right Back (RB)', 'Goalkeeper (GK)',"Attacking Average","Attacking Total","Skill Average","Skill Total","Movement Average",
"Movement Total","Power Average","Power Total","Mentality Average","Mentality Total","Defending Average",
"Defending Total","Goalkeeping Average","Goalkeeping Total","Base stats","Total Stats"])

def check_convert_digit(str):
    if str.isdigit() or str.replace(",","").isdigit():
        return int(str.replace(",",""))

#stores lists each containing strings of the attribute name and the value    
in_depth_list_val_plus_attribute = []
#stores only the values gotten  
in_depth_val_only = []
#stores only the attribute names which I will use as reference to create variables to unpack the values array into
in_depth_attribute_only = []

rating_by_position_plus_val= []
positions_list = []
positions_ratings_val = []


with open("playerShallowstats.csv",encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)

    # initialize a counter to skip already read rows
    counter = 0
    detailed_link_col_index = headers.index('Detailed link')
    for i,row in enumerate(csv_reader):
        if counter>=16650:
                
            detailed_link_value = row[detailed_link_col_index]
            print(detailed_link_value)

            # so we now have the href of each individual player so we need to scrape each individual attribute
            r = requests.get(detailed_link_value)
            time.sleep(1)
            player_page = BeautifulSoup(r.text,"html.parser")
            name_element = player_page.find('h1', {'class': 'header-title pt-2 mb-0'})
            name = name_element.text.strip()
            print(name)
            essential_details_element = player_page.select_one(".header-subtitle")
            player_details = essential_details_element.find_all("p",{'class': "mb-0"})
            # the normal length of the player_details list is supposed to be 8 but for players who didn't 
            # provide nationality, the href of their link doesn't contain "country"
            # if len(player_details)== 7 and "country" not in player_details[0].select_one("a").attrs["href"]:
            if len(player_details) != 10 and "country" not in player_details[0].select_one("a").attrs["href"]:
                # print(player_details[0].select_one("a").attrs["href"])
                nationality = "Unprovided"
                for i,detail in enumerate(player_details):
                    if i == 0:
                        team = detail.select_one("a").text.strip()
                        print(team)
                    elif i == 1:
                        if detail.text.split(":")[1].split("#")[1].replace(" ","") == "":
                            kit_number = "Unprovided"
                        else:
                            kit_number = detail.text.split(":")[1].split("#")[1]
                        print(kit_number)
                    elif i == 2:
                        league = detail.select_one("a").text.strip()
                        print(league)

                    elif i == 3:
                        s = detail.text.replace('"', '')
                        height_str, weight_str = s.split("|")
                        height_inches_str, height_cm_str = height_str.split("(")
                        height_inches_str = height_inches_str.strip()
                        height_inches = height_inches_str.split(":")[1].strip()
                        print(height_inches)
                        height_cm = height_cm_str.strip(")").replace("cm", "").replace(")","")
                        print(height_cm)
                        weight_lbs_str, weight_kg_str = weight_str.split("(")
                        weight_lbs = weight_lbs_str.strip().replace("lbs", "").split(":")[1].strip()
                        print(weight_lbs)
                        weight_kg = weight_kg_str.strip(")").replace("kg", "")
                        print(weight_kg)
                    elif i == 4:
                        best_position  = detail.select_one("a").text.strip()
                        print(best_position)
                    if i == 5:
                        best_foot = detail.text.split(":")[1].strip()
                        print(best_foot)

                    # for index 7,8,9 the data was represented as stars and the number or length of elements 
                    # which are span elements with the class of fa fa-star text-warning within each paragraph with class of
                    #mb-0 which I have referenced as detail is the Number of stars that player has in that attribute
                    elif i == 6:
                        weak_foot_list = detail.find_all("span",{"class":"fa fa-star text-warning"})
                        weak_foot_stars = len(weak_foot_list)
                        print(f"weakfoot: {weak_foot_stars} stars")
                    elif i == 7:
                        skill_moves_list = detail.find_all("span",{"class":"fa fa-star text-warning"})
                        skill_moves_stars = len(skill_moves_list)
                        print(f"skill moves: {skill_moves_stars} stars")

                    elif i == 8:
                        international_reputation_list =  detail.find_all("span",{"class":"fa fa-star text-warning"})
                        international_reputation_stars = len(international_reputation_list)
                        print(f"international reputation: {international_reputation_stars} stars")


                attributes_div = player_page.find("div",{"class": "tab-pane fade show active mt-3"})
                positions_ratings_div = player_page.find("div",{"class": "tab-pane fade mt-3"})
                attributes_card = attributes_div.select_one(".row").find_all("div",{"class": "card"})
                for card in attributes_card:
                    header_attribute_li = card.select(".card-header h5")
                    for header in header_attribute_li:
                        attribute_value_li = header.text.split(" ",1)
                        if "Attacking Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                attacking_average = int(val.replace(",","")) 
                                print(attribute,attacking_average)
                        elif "Attacking Total" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                attacking_total =  int(val.replace(",",""))
                                print(attribute,attacking_total) 
                        elif "Skill Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                skill_average =  int(val.replace(",",""))
                                print(attribute,skill_average) 
                        elif "Skill Total" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                skill_total =  int(val.replace(",",""))
                                print(attribute,skill_total)
                        elif "Movement Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                movement_average =  int(val.replace(",",""))
                                print(attribute,movement_average) 
                        elif  'Movement Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                movement_total =  int(val.replace(",",""))
                                print(attribute,movement_total) 
                        elif 'Power Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                power_average =  int(val.replace(",",""))
                                print(attribute,power_average) 
                        elif  'Power Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                power_total =  int(val.replace(",",""))
                                print(attribute,power_total) 
                        elif 'Mentality Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                mentality_average =  int(val.replace(",",""))
                                print(attribute,mentality_average) 
                        elif 'Mentality Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                mentality_total =  int(val.replace(",",""))
                                print(attribute,mentality_total) 
                        elif 'Defending Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                defending_average =  int(val.replace(",",""))
                                print(attribute,defending_average) 
                        elif  'Defending Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                defending_total =  int(val.replace(",",""))
                                print(attribute,defending_total) 
                        elif  'Goalkeeping Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                goalkeeping_average =  int(val.replace(",",""))
                                print(attribute,goalkeeping_average) 
                        elif  'Goalkeeping Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                goalkeeping_total =  int(val.replace(",",""))
                                print(attribute,goalkeeping_total) 
                        elif  'Base Stats' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                base_stats =  int(val.replace(",",""))
                                print(attribute,base_stats) 
                        elif  'Total Stats' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                total_stats =  int(val.replace(",",""))
                                print(attribute,total_stats)                         
                for card in attributes_card:
                    attributes_indepth_li = card.find_all("li")
                    for li in attributes_indepth_li:
                        in_depth_list_val_plus_attribute.append(li.text.split(" ",1))
                        in_depth_attribute_only.append(li.text.split(" ",1)[1])
                        in_depth_val_only.append(li.text.split(" ",1)[0])

                # print(in_depth_val_only)
                # print(in_depth_attribute_only)
                print(len(in_depth_attribute_only))
                print(len(in_depth_val_only))
                print(len(in_depth_list_val_plus_attribute)) 
                # now we have to unpack the elements of the list into several variables so we can be able to write the attributes into csv files without a problem
                crossing,finishing,heading_accuracy,short_passing,volleys,dribbling,curve,freekick_accuracy,long_passing,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes = in_depth_val_only
                
                for position_rating_elem in positions_ratings_div.find_all("h5"):
                    position_rating_li = position_rating_elem.text.split(" ",1)
                    rating_by_position_plus_val.append(position_rating_li)
                    positions_ratings_val.append(position_rating_li[0])
                    positions_list.append(position_rating_li[1])

                # print(positions_ratings_val)
                # print(positions_list)
                print(len(positions_ratings_val))
                print(len(positions_list))
                print(len(rating_by_position_plus_val))
                striker,left_wing,left_forward,center_forward,right_forward,right_wing,center_attacking_midfielder,left_midfielder,center_midfielder,right_midfielder,left_wing_back,center_defensive_midfielder,right_wing_back,left_back,center_back,right_back,goalkeeper = positions_ratings_val
                
                with open("playerDetailedStats_46.csv",mode = "a", newline = '',encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([name,nationality,team,kit_number,league,height_inches,height_cm,weight_lbs,weight_kg,
        best_position,best_foot,weak_foot_stars,skill_moves_stars,international_reputation_stars,crossing,
        finishing,heading_accuracy,short_passing,volleys,dribbling,curve,freekick_accuracy,long_passing,ball_control,
        acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,
        aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,
        gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes,striker,left_wing,left_forward,center_forward,right_forward,right_wing,
        center_attacking_midfielder,left_midfielder,center_midfielder,right_midfielder,left_wing_back,
        center_defensive_midfielder,right_wing_back,left_back,center_back,right_back,goalkeeper,attacking_average,attacking_total,
        skill_average,skill_total,movement_average,movement_total,power_average,power_total,mentality_average,mentality_total,defending_average,defending_total,goalkeeping_average,goalkeeping_total,base_stats,total_stats])
                    # I had to make sure I emptied all the lists again after each row is done being transfered to csv file
                    # so that I do not get error message trying to unpack too many values more than expected
                #stores lists each containing strings of the attribute name and the value    
                    in_depth_list_val_plus_attribute = []
                    #stores only the values gotten  
                    in_depth_val_only = []
                    #stores only the attribute names which I will use as reference to create variables to unpack the values array into
                    in_depth_attribute_only = []

                    rating_by_position_plus_val= []
                    positions_list = []
                    positions_ratings_val = []
                    
                
                if (i + 1) % 27 == 0:
                    time.sleep(5) # pause for 5 seconds
        # The elif , if method I used to scrape the data is honestly so stressful, manual,repetitive and a bit boring
        # It feels so painful to have to change one tiny occurence in all the respective places in which it's found
        # Next time, I will scrape all the attributes, add them to a list and after I am done adding them to a list,
        # I will zip the list and write to the csv file because the method I used to scrape stuff like international
        # reputation, weakfoot,skill move team, league, height, weight, best postion etc, although it works, it is 
        # so repetitive and involves so much work. I have to write as many if statements and elif statements for as many 
        # unique cases as there are, which isn't very helpful especially if you are dealing with extremely numerouns
        # number of unique cases.




        # I have realized that I am using way too many procedural and repetitive code which makes my code unnecessarily long.
        # I need to seriously start creating and using callback functions to make my code look cleaner, faster and more effective.

                




        # I have realized that I am using way too many procedural and repetitive code which makes my code unnecessarily long.
        # I need to seriously start creating and using callback functions to make my code look cleaner, faster and more effective.


            # I have to add a new condition because I realized some of the players didn't provide best foot. 
            # and  I have to restructure the code. I should've used functions so my code won't be so repetitive.
            elif len(player_details) != 10 and "Best Foot" not in player_details[6].text:
                best_foot = "Unprovided"
                for i,detail in enumerate(player_details):
                    if i == 0:
                        # print(detail)
                        # detail is an element
                        #select the link within the class and get it's innner text
                        nationality = detail.select_one("a").text.strip()
                        print(nationality)
                    elif i == 1:
                        team = detail.select_one("a").text.strip()
                        print(team)

                    elif i == 2:
                        if detail.text.split(":")[1].split("#")[1].replace(" ","") == "":
                            kit_number = "Unprovided"
                        else:
                            kit_number = detail.text.split(":")[1].split("#")[1]
                        print(kit_number)
                    elif i == 3:
                        league = detail.select_one("a").text.strip()
                        print(league)

                    elif i == 4:
                        s = detail.text.replace('"', '')
                        height_str, weight_str = s.split("|")
                        height_inches_str, height_cm_str = height_str.split("(")
                        height_inches_str = height_inches_str.strip()
                        height_inches = height_inches_str.split(":")[1].strip()
                        print(height_inches)
                        height_cm = height_cm_str.strip(")").replace("cm", "").replace(")","")
                        print(height_cm)
                        weight_lbs_str, weight_kg_str = weight_str.split("(")
                        weight_lbs = weight_lbs_str.strip().replace("lbs", "").split(":")[1].strip()
                        print(weight_lbs)
                        weight_kg = weight_kg_str.strip(")").replace("kg", "")
                        print(weight_kg)
                    elif i == 5:
                        best_position  = detail.select_one("a").text.strip()
                        print(best_position)

                    # for index 7,8,9 the data was represented as stars and the number or length of elements 
                    # which are span elements with the class of fa fa-star text-warning within each paragraph with class of
                    #mb-0 which I have referenced as detail is the Number of stars that player has in that attribute
                    elif i == 6:
                        weak_foot_list = detail.find_all("span",{"class":"fa fa-star text-warning"})
                        weak_foot_stars = len(weak_foot_list)
                        print(f"weakfoot: {weak_foot_stars} stars")
                    elif i == 7:
                        skill_moves_list = detail.find_all("span",{"class":"fa fa-star text-warning"})
                        skill_moves_stars = len(skill_moves_list)
                        print(f"skill moves: {skill_moves_stars} stars")

                    elif i == 8:
                        international_reputation_list =  detail.find_all("span",{"class":"fa fa-star text-warning"})
                        international_reputation_stars = len(international_reputation_list)
                        print(f"international reputation: {international_reputation_stars} stars")


                attributes_div = player_page.find("div",{"class": "tab-pane fade show active mt-3"})
                positions_ratings_div = player_page.find("div",{"class": "tab-pane fade mt-3"})
                attributes_card = attributes_div.select_one(".row").find_all("div",{"class": "card"})
                for card in attributes_card:
                    header_attribute_li = card.select(".card-header h5")
                    for header in header_attribute_li:
                        attribute_value_li = header.text.split(" ",1)
                        if "Attacking Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                attacking_average = int(val.replace(",","")) 
                                print(attribute,attacking_average)
                        elif "Attacking Total" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                attacking_total =  int(val.replace(",",""))
                                print(attribute,attacking_total) 
                        elif "Skill Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                skill_average =  int(val.replace(",",""))
                                print(attribute,skill_average) 
                        elif "Skill Total" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                skill_total =  int(val.replace(",",""))
                                print(attribute,skill_total)
                        elif "Movement Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                movement_average =  int(val.replace(",",""))
                                print(attribute,movement_average) 
                        elif  'Movement Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                movement_total =  int(val.replace(",",""))
                                print(attribute,movement_total) 
                        elif 'Power Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                power_average =  int(val.replace(",",""))
                                print(attribute,power_average) 
                        elif  'Power Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                power_total =  int(val.replace(",",""))
                                print(attribute,power_total) 
                        elif 'Mentality Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                mentality_average =  int(val.replace(",",""))
                                print(attribute,mentality_average) 
                        elif 'Mentality Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                mentality_total =  int(val.replace(",",""))
                                print(attribute,mentality_total) 
                        elif 'Defending Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                defending_average =  int(val.replace(",",""))
                                print(attribute,defending_average) 
                        elif  'Defending Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                defending_total =  int(val.replace(",",""))
                                print(attribute,defending_total) 
                        elif  'Goalkeeping Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                goalkeeping_average =  int(val.replace(",",""))
                                print(attribute,goalkeeping_average) 
                        elif  'Goalkeeping Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                goalkeeping_total =  int(val.replace(",",""))
                                print(attribute,goalkeeping_total) 
                        elif  'Base Stats' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                base_stats =  int(val.replace(",",""))
                                print(attribute,base_stats) 
                        elif  'Total Stats' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                total_stats =  int(val.replace(",",""))
                                print(attribute,total_stats)                         
                for card in attributes_card:
                    attributes_indepth_li = card.find_all("li")
                    for li in attributes_indepth_li:
                        in_depth_list_val_plus_attribute.append(li.text.split(" ",1))
                        in_depth_attribute_only.append(li.text.split(" ",1)[1])
                        in_depth_val_only.append(li.text.split(" ",1)[0])

                # print(in_depth_val_only)
                # print(in_depth_attribute_only)
                print(len(in_depth_attribute_only))
                print(len(in_depth_val_only))
                print(len(in_depth_list_val_plus_attribute)) 
                # now we have to unpack the elements of the list into several variables so we can be able to write the attributes into csv files without a problem
                crossing,finishing,heading_accuracy,short_passing,volleys,dribbling,curve,freekick_accuracy,long_passing,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes = in_depth_val_only
                
                for position_rating_elem in positions_ratings_div.find_all("h5"):
                    position_rating_li = position_rating_elem.text.split(" ",1)
                    rating_by_position_plus_val.append(position_rating_li)
                    positions_ratings_val.append(position_rating_li[0])
                    positions_list.append(position_rating_li[1])

                # print(positions_ratings_val)
                # print(positions_list)
                print(len(positions_ratings_val))
                print(len(positions_list))
                print(len(rating_by_position_plus_val))
                striker,left_wing,left_forward,center_forward,right_forward,right_wing,center_attacking_midfielder,left_midfielder,center_midfielder,right_midfielder,left_wing_back,center_defensive_midfielder,right_wing_back,left_back,center_back,right_back,goalkeeper = positions_ratings_val
                
                with open("playerDetailedStats_46.csv",mode = "a", newline = '',encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([name,nationality,team,kit_number,league,height_inches,height_cm,weight_lbs,weight_kg,
        best_position,best_foot,weak_foot_stars,skill_moves_stars,international_reputation_stars,crossing,
        finishing,heading_accuracy,short_passing,volleys,dribbling,curve,freekick_accuracy,long_passing,ball_control,
        acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,
        aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,
        gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes,striker,left_wing,left_forward,center_forward,right_forward,right_wing,
        center_attacking_midfielder,left_midfielder,center_midfielder,right_midfielder,left_wing_back,
        center_defensive_midfielder,right_wing_back,left_back,center_back,right_back,goalkeeper,attacking_average,attacking_total,
        skill_average,skill_total,movement_average,movement_total,power_average,power_total,mentality_average,mentality_total,defending_average,defending_total,goalkeeping_average,goalkeeping_total,base_stats,total_stats])
                    # I had to make sure I emptied all the lists again after each row is done being transfered to csv file
                    # so that I do not get error message trying to unpack too many values more than expected
                #stores lists each containing strings of the attribute name and the value    
                    in_depth_list_val_plus_attribute = []
                    #stores only the values gotten  
                    in_depth_val_only = []
                    #stores only the attribute names which I will use as reference to create variables to unpack the values array into
                    in_depth_attribute_only = []

                    rating_by_position_plus_val= []
                    positions_list = []
                    positions_ratings_val = []
                    
                
                if (i + 1) % 27 == 0:
                    time.sleep(5) # pause for 5 seconds

            else:
            #the text of each paragraph in the player_details list is significantly different
            #so if I want to loop through the list, I need to use enumerate so I can acess each index differently
            #and execute different code depending on what index I am currently at in the iteration

            #the text of each paragraph in the player_details list is significantly different
            #so if I want to loop through the list, I need to use enumerate so I can acess each index differently
            #and execute different code depending on what index I am currently at in the iteration

                for i,detail in enumerate(player_details):
                    if i == 0:
                        # print(detail)
                        # detail is an element
                        #select the link within the class and get it's innner text
                        nationality = detail.select_one("a").text.strip()
                        print(nationality)
                    elif i == 1:
                        team = detail.select_one("a").text.strip()
                        print(team)

                    elif i == 2:
                        if detail.text.split(":")[1].split("#")[1].replace(" ","") == "":
                            kit_number = "Unprovided"
                        else:
                            kit_number = detail.text.split(":")[1].split("#")[1]
                        print(kit_number)
                    elif i == 3:
                        league = detail.select_one("a").text.strip()
                        print(league)

                    elif i == 4:
                        s = detail.text.replace('"', '')
                        height_str, weight_str = s.split("|")
                        height_inches_str, height_cm_str = height_str.split("(")
                        height_inches_str = height_inches_str.strip()
                        height_inches = height_inches_str.split(":")[1].strip()
                        print(height_inches)
                        height_cm = height_cm_str.strip(")").replace("cm", "").replace(")","")
                        print(height_cm)
                        weight_lbs_str, weight_kg_str = weight_str.split("(")
                        weight_lbs = weight_lbs_str.strip().replace("lbs", "").split(":")[1].strip()
                        print(weight_lbs)
                        weight_kg = weight_kg_str.strip(")").replace("kg", "")
                        print(weight_kg)
                    elif i == 5:
                        best_position  = detail.select_one("a").text.strip()
                        print(best_position)
                    elif i == 6:
                        best_foot = detail.text.split(":")[1].strip()
                        print(best_foot)

                    # for index 7,8,9 the data was represented as stars and the number or length of elements 
                    # which are span elements with the class of fa fa-star text-warning within each paragraph with class of
                    #mb-0 which I have referenced as detail is the Number of stars that player has in that attribute
                    elif i == 7:
                        weak_foot_list = detail.find_all("span",{"class":"fa fa-star text-warning"})
                        weak_foot_stars = len(weak_foot_list)
                        print(f"weakfoot: {weak_foot_stars} stars")
                    elif i == 8:
                        skill_moves_list = detail.find_all("span",{"class":"fa fa-star text-warning"})
                        skill_moves_stars = len(skill_moves_list)
                        print(f"skill moves: {skill_moves_stars} stars")

                    elif i == 9:
                        international_reputation_list =  detail.find_all("span",{"class":"fa fa-star text-warning"})
                        international_reputation_stars = len(international_reputation_list)
                        print(f"international reputation: {international_reputation_stars} stars")


                attributes_div = player_page.find("div",{"class": "tab-pane fade show active mt-3"})
                positions_ratings_div = player_page.find("div",{"class": "tab-pane fade mt-3"})
                attributes_card = attributes_div.select_one(".row").find_all("div",{"class": "card"})
                for card in attributes_card:
                    header_attribute_li = card.select(".card-header h5")
                    for header in header_attribute_li:
                        attribute_value_li = header.text.split(" ",1)
                        if "Attacking Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                attacking_average = int(val.replace(",","")) 
                                print(attribute,attacking_average)
                        elif "Attacking Total" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                attacking_total =  int(val.replace(",",""))
                                print(attribute,attacking_total) 
                        elif "Skill Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                skill_average =  int(val.replace(",",""))
                                print(attribute,skill_average) 
                        elif "Skill Total" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                skill_total =  int(val.replace(",",""))
                                print(attribute,skill_total)
                        elif "Movement Average" in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                movement_average =  int(val.replace(",",""))
                                print(attribute,movement_average) 
                        elif  'Movement Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                movement_total =  int(val.replace(",",""))
                                print(attribute,movement_total) 
                        elif 'Power Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1] 
                            if val.isdigit() or val.replace(",","").isdigit():
                                power_average =  int(val.replace(",",""))
                                print(attribute,power_average) 
                        elif  'Power Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                power_total =  int(val.replace(",",""))
                                print(attribute,power_total) 
                        elif 'Mentality Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                mentality_average =  int(val.replace(",",""))
                                print(attribute,mentality_average) 
                        elif 'Mentality Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                mentality_total =  int(val.replace(",",""))
                                print(attribute,mentality_total) 
                        elif 'Defending Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                defending_average =  int(val.replace(",",""))
                                print(attribute,defending_average) 
                        elif  'Defending Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                defending_total =  int(val.replace(",",""))
                                print(attribute,defending_total) 
                        elif  'Goalkeeping Average' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                goalkeeping_average =  int(val.replace(",",""))
                                print(attribute,goalkeeping_average) 
                        elif  'Goalkeeping Total' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                goalkeeping_total =  int(val.replace(",",""))
                                print(attribute,goalkeeping_total) 
                        elif  'Base Stats' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                base_stats =  int(val.replace(",",""))
                                print(attribute,base_stats) 
                        elif  'Total Stats' in attribute_value_li[1]:
                            val = attribute_value_li[0]
                            attribute = attribute_value_li[1]
                            if val.isdigit() or val.replace(",","").isdigit():
                                total_stats =  int(val.replace(",",""))
                                print(attribute,total_stats)                         
                for card in attributes_card:
                    attributes_indepth_li = card.find_all("li")
                    for li in attributes_indepth_li:
                        in_depth_list_val_plus_attribute.append(li.text.split(" ",1))
                        in_depth_attribute_only.append(li.text.split(" ",1)[1])
                        in_depth_val_only.append(li.text.split(" ",1)[0])

                # print(in_depth_val_only)
                # print(in_depth_attribute_only)
                print(len(in_depth_attribute_only))
                print(len(in_depth_val_only))
                print(len(in_depth_list_val_plus_attribute)) 
                # now we have to unpack the elements of the list into several variables so we can be able to write the attributes into csv files without a problem
                crossing,finishing,heading_accuracy,short_passing,volleys,dribbling,curve,freekick_accuracy,long_passing,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes = in_depth_val_only
                
                for position_rating_elem in positions_ratings_div.find_all("h5"):
                    position_rating_li = position_rating_elem.text.split(" ",1)
                    rating_by_position_plus_val.append(position_rating_li)
                    positions_ratings_val.append(position_rating_li[0])
                    positions_list.append(position_rating_li[1])

                # print(positions_ratings_val)
                # print(positions_list)
                print(len(positions_ratings_val))
                print(len(positions_list))
                print(len(rating_by_position_plus_val))
                striker,left_wing,left_forward,center_forward,right_forward,right_wing,center_attacking_midfielder,left_midfielder,center_midfielder,right_midfielder,left_wing_back,center_defensive_midfielder,right_wing_back,left_back,center_back,right_back,goalkeeper = positions_ratings_val
                
                with open("playerDetailedStats_46.csv",mode = "a", newline = '',encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([name,nationality,team,kit_number,league,height_inches,height_cm,weight_lbs,weight_kg,
        best_position,best_foot,weak_foot_stars,skill_moves_stars,international_reputation_stars,crossing,
        finishing,heading_accuracy,short_passing,volleys,dribbling,curve,freekick_accuracy,long_passing,ball_control,
        acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,
        aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,
        gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes,striker,left_wing,left_forward,center_forward,right_forward,right_wing,
        center_attacking_midfielder,left_midfielder,center_midfielder,right_midfielder,left_wing_back,
        center_defensive_midfielder,right_wing_back,left_back,center_back,right_back,goalkeeper,attacking_average,attacking_total,
        skill_average,skill_total,movement_average,movement_total,power_average,power_total,mentality_average,mentality_total,defending_average,defending_total,goalkeeping_average,goalkeeping_total,base_stats,total_stats])
                    # I had to make sure I emptied all the lists again after each row is done being transfered to csv file
                    # so that I do not get error message trying to unpack too many values more than expected
                #stores lists each containing strings of the attribute name and the value    
                    in_depth_list_val_plus_attribute = []
                    #stores only the values gotten  
                    in_depth_val_only = []
                    #stores only the attribute names which I will use as reference to create variables to unpack the values array into
                    in_depth_attribute_only = []

                    rating_by_position_plus_val= []
                    positions_list = []
                    positions_ratings_val = []
                    
                
                # if (i + 1) % 27 == 0:
                #     time.sleep(5) # pause for 5 seconds
                # break      
        counter += 1
        # The elif , if method I used to scrape the data is honestly so stressful, manual,repetitive and a bit boring
        # It feels so painful to have to change one tiny occurence in all the respective places in which it's found
        # Next time, I will scrape all the attributes, add them to a list and after I am done adding them to a list,
        # I will zip the list and write to the csv file because the method I used to scrape stuff like international
        # reputation, weakfoot,skill move team, league, height, weight, best postion etc, although it works, it is 
        # so repetitive and involves so much work. I have to write as many if statements and elif statements for as many 
        # unique cases as there are, which isn't very helpful especially if you are dealing with extremely numerouns
        # number of unique cases.




        # I have realized that I am using way too many procedural and repetitive code which makes my code unnecessarily long.
        # I need to seriously start creating and using callback functions to make my code look cleaner, faster and more effective.