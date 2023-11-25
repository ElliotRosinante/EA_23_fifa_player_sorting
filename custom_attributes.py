import csv
import unicodedata

all_players_detailed = []
all_players_shallow = []
all_players_ultra = []

# these were the values for the fifa 22
attributes_needed_calculate_pace = [("Acceleration",45),("Sprint Speed",55)]
attributes_needed_calculate_dribbling = [("Dribbling",50),("Ball Control",35),("Agility",10),("Balance",5)]
attributes_needed_calculate_defending = [("Interceptions",20),("Heading Accuracy",10),("Marking",30),("Standing Tackle",30),("Sliding Tackle",10)]
attributes_needed_calculate_passing = [("Vision",20),("Crossing",20),("FreeKick Accuracy",5),("Short Passing",35),("Long Passing",15),("Curve",5)]
attributes_needed_calculate_physical = [("Jumping",5),("Stamina",25),("Strength",50),("Aggression",20)]
attributes_needed_calculate_shooting = [("Positioning",5),("Finishing",45),("Shot Power",20),("Long Shots",20),("Volleys",5),("Penalties",5)]

# these are the values for the fifa 23
attributes_needed_calculate_pace_1 = [("Acceleration",45),("Sprint Speed",55)]
attributes_needed_calculate_dribbling_1 = [("Dribbling",50),("Ball Control",35),("Agility",10),("Balance",5)]
attributes_needed_calculate_defending_1 = [("Interceptions",20),("Heading Accuracy",10),("Marking",30),("Standing Tackle",30),("Sliding Tackle",10)]
attributes_needed_calculate_passing_1 = [("Vision",20),("Crossing",20),("FreeKick Accuracy",5),("Short Passing",35),("Long Passing",15),("Curve",5)]
attributes_needed_calculate_physical_1 = [("Jumping",5),("Stamina",25),("Strength",50),("Aggression",20)]
attributes_needed_calculate_shooting_1 = [("Positioning",5),("Finishing",45),("Shot Power",20),("Long Shots",20),("Volleys",5),("Penalties",5)]

# The order matters
six_custom_combined = [attributes_needed_calculate_pace,attributes_needed_calculate_dribbling,attributes_needed_calculate_defending,attributes_needed_calculate_passing,attributes_needed_calculate_physical,attributes_needed_calculate_shooting]

six_custom_combined_1 = [attributes_needed_calculate_pace_1,attributes_needed_calculate_dribbling_1,attributes_needed_calculate_defending_1,attributes_needed_calculate_passing_1,attributes_needed_calculate_physical_1,attributes_needed_calculate_shooting_1]

def read_specified_csv(filename,list):
    with open(filename,mode= "r",encoding="utf-8") as csv_file:
        csv_file = csv.DictReader(csv_file)
        for row in csv_file:
            list.append(row)

read_specified_csv("playerDetailedStats_main.csv",all_players_detailed)
read_specified_csv("playerShallowStats_1.csv",all_players_shallow)

#zip the all_players_detailed and all_players_shallow and loop through them. 
# get all the attributes you need and create a dictionary

for player_x,player_y in zip(all_players_detailed,all_players_shallow):
    # create a dictionary get all attributes/values in player_x and get 3 specific attributes from player_y 
    custom_dictionary = {
    }
    for attr,value in player_x.items():
        custom_dictionary[attr] = value

    # now let's get the specific attributes we need from player_y
    target_attr = ["Overall","Potential","Stats"]
    for attr in target_attr:
        custom_dictionary[attr] = player_y[attr]
    
    # so now we have all the attributes we need 

    #what we do next is that we append this dictionary with all cool_juicy_player info to a list.
    all_players_ultra.append(custom_dictionary)

#let's test this to see if its working
# print(all_players_ultra[0])
# {'Player Name': 'Kevin De Bruyne', 'Nationality': 'Belgium', 'Team': 'Manchester City', 'Kit Number': '17', 'League': 'English Premier League', 'Height(inches)': "5'11", 'Height(cm)': '181 ', 'Weight(lbs)': '154', 'Weight(kg)': '70', 'Best Position': 'Center Midfielder (CM)', 'Best Foot': 'Right', 'Weak Foot': '5', 'Skill moves': '4', 'International Reputation': '4', 'Crossing': '94', 'Finishing': '85', 'Heading Accuracy': '55', 'Short Passing': '93', 'Volleys': '83', 'Dribbling': '88', 'Curve': '89', 'FreeKick Accuracy': '83', 'Long Passing': '93', 'Ball Control': '90', 'Acceleration': '76', 'Sprint Speed': '73', 'Agility': '76', 'Reactions': '91', 'Balance': '78', 'Shot Power': '92', 'Jumping': '63', 'Stamina': '88', 'Strength': '74', 'Long Shots': '91', 'Aggression': '75', 'Interceptions': '66', 'Positioning': '88', 'Vision': '94', 'Penalties': '83', 'Composure': '89', 'Marking': '68', 'Standing Tackle': '65', 'Sliding Tackle': '53', 'GK Diving': '15', 'GK Handling': '13', 'GK Kicking': '5', 'GK Positioning': '10', 'GK Reflexes': '13', 'Striker (ST)': '86', 'Left Wing (LW)': '88', 'Left Forward (LF)': '87', 'Center Forward (CF)': '87', 'Right Forward (RF)': '87', 'Right Wing (RW)': '88', 'Center Attacking Midfielder (CAM)': '91', 'Left Midfielder (LM)': '91', 'Center Midfielder (CM)': '91', 'Right Midfielder (RM)': '91', 'Left Wing Back (LWB)': '82', 'Center Defensive Midfielder (CDM)': '82', 'Right Wing Back (RWB)': '82', 'Left Back (LB)': '78', 'Center Back (CB)': '72', 'Right Back (RB)': '78', 'Goalkeeper (GK)': '24', 'Attacking Average': '82', 'Attacking Total': '410', 'Skill Average': '89', 'Skill Total': '443', 'Movement Average': '79', 'Movement Total': '394', 'Power Average': '82', 'Power Total': '408', 'Mentality Average': '83', 'Mentality Total': '495', 'Defending Average': '62', 'Defending Total': '186', 'Goalkeeping Average': '11', 'Goalkeeping Total': '56', 'Base stats': '483', 'Total Stats': '2298', 'Overall': '91', 'Potential': '91', 'Stats': '2298'}

# Now let's create the 6 main atttributes, the custom ones 
def create_custom_6_attributes():
    #define a list in the correct order to store the attributes calculated
    the_six_main_attributes = ["Pace","Dribbling_overall","Defending","Passing","Physical","Shooting"]
    for player in all_players_ultra:
        all_six_values = []
        for custom_attr_li in six_custom_combined:
            custom_val_sum = 0
            for pair in custom_attr_li:
                attr = pair[0]
                val = pair[1]
                if player[attr]!= "--":
                    #convert it into an integer and add it up to wanted_attr
                    custom_val_sum += int(player[attr]) * val
            # after finishing looping through all the pairs in the custom_attr_li, we divide the custom_val_sum by 100
            custom_val_sum_actual_value_out_of_hundred = custom_val_sum // 100

            # next we get hold of the value and append it to the all_six_values_list
            all_six_values.append(custom_val_sum_actual_value_out_of_hundred)

        # after we finish our calculations, we zip the_six_main_attributes and all_six_values
        for attr,val in zip(the_six_main_attributes,all_six_values):
            # now we assign our new custom attributes and their respective values to each player's dictionary
            player[attr] = val

            # now overhere in the assigning of values, if I were to write the data gotten into a csv file, I could do 
            # this properly by assigning converting the number value to  

# create_custom_6_attributes()

# let's test this to see if its working
# print(all_players_ultra[0])

# {'Player Name': 'Kevin De Bruyne', 'Nationality': 'Belgium', 'Team': 'Manchester City', 'Kit Number': '17', 'League': 'English Premier League', 'Height(inches)': "5'11", 'Height(cm)': '181 ', 'Weight(lbs)': '154', 'Weight(kg)': '70', 'Best Position': 'Center Midfielder (CM)', 'Best Foot': 'Right', 'Weak Foot': '5', 'Skill moves': '4', 'International Reputation': '4', 'Crossing': '94', 'Finishing': '85', 'Heading Accuracy': '55', 'Short Passing': '93', 'Volleys': '83', 'Dribbling': 87, 'Curve': '89', 'FreeKick Accuracy': '83', 'Long Passing': '93', 'Ball Control': '90', 'Acceleration': '76', 'Sprint Speed': '73', 'Agility': '76', 'Reactions': '91', 'Balance': '78', 'Shot Power': '92', 'Jumping': '63', 'Stamina': '88', 'Strength': '74', 'Long Shots': '91', 'Aggression': '75', 'Interceptions': '66', 'Positioning': '88', 'Vision': '94', 'Penalties': '83', 'Composure': '89', 'Marking': '68', 'Standing Tackle': '65', 'Sliding Tackle': '53', 'GK Diving': '15', 'GK Handling': '13', 'GK Kicking': '5', 'GK Positioning': '10', 'GK Reflexes': '13', 'Striker (ST)': '86', 'Left Wing (LW)': '88', 'Left Forward (LF)': '87', 'Center Forward (CF)': '87', 'Right Forward (RF)': '87', 'Right Wing (RW)': '88', 'Center Attacking Midfielder (CAM)': '91', 'Left Midfielder (LM)': '91', 'Center Midfielder (CM)': '91', 'Right Midfielder (RM)': '91', 'Left Wing Back (LWB)': '82', 'Center Defensive Midfielder (CDM)': '82', 'Right Wing Back (RWB)': '82', 'Left Back (LB)': '78', 'Center Back (CB)': '72', 'Right Back (RB)': '78', 'Goalkeeper (GK)': '24', 'Attacking Average': '82', 'Attacking Total': '410', 'Skill Average': '89', 'Skill Total': '443', 'Movement Average': '79', 'Movement Total': '394', 'Power Average': '82', 'Power Total': '408', 'Mentality Average': '83', 'Mentality Total': '495', 'Defending Average': '62', 'Defending Total': '186', 'Goalkeeping Average': '11', 'Goalkeeping Total': '56', 'Base stats': '483', 'Total Stats': '2298', 'Overall': '91', 'Potential': '91', 'Stats': '2298', 'Pace': 74, 'Defending': 63, 'Passing': 92, 'Physical': 77, 'Shooting': 87}
# Stats and Total Stats are the same

def create_custom_6_attributes_closer_to_real_life_version():
    #define a list in the correct order to store the attributes calculated
    the_six_main_attributes = ["Pace","Dribbling_overall","Defending","Passing","Physical","Shooting"]
    for player in all_players_ultra:
        all_six_values = []
        for custom_attr_li in six_custom_combined:
            custom_val_sum = 0
            for pair in custom_attr_li:
                attr = pair[0]
                val = pair[1]
                if player[attr]!= "--":
                    #convert it into an integer and add it up to wanted_attr
                    custom_val_sum += int(player[attr]) * val
            # after finishing looping through all the pairs in the custom_attr_li, we divide the custom_val_sum by 100
            custom_val_sum_actual_value_out_of_hundred = custom_val_sum // 100

            # next we get hold of the value and append it to the all_six_values_list
            all_six_values.append(custom_val_sum_actual_value_out_of_hundred)

        # after we finish our calculations, we zip the_six_main_attributes and all_six_values
        for attr,val in zip(the_six_main_attributes,all_six_values):
            # now we assign our new custom attributes and their respective values to each player's dictionary
            if attr in ["Shooting","Defending","Passing"]:
                player[attr] = val + 1
            else:
                player[attr] = val

            # now overhere in the assigning of values, if I were to write the data gotten into a csv file, I could do 
            # this properly by assigning converting the number value to  

# create_custom_6_attributes_closer_to_real_life_version()

# let's test this to see if its working
# print(all_players_ultra[0])
# {'Player Name': 'Kevin De Bruyne', 'Nationality': 'Belgium', 'Team': 'Manchester City', 'Kit Number': '17', 'League': 'English Premier League', 'Height(inches)': "5'11", 'Height(cm)': '181 ', 'Weight(lbs)': '154', 'Weight(kg)': '70', 'Best Position': 'Center Midfielder (CM)', 'Best Foot': 'Right', 'Weak Foot': '5', 'Skill moves': '4', 'International Reputation': '4', 'Crossing': '94', 'Finishing': '85', 'Heading Accuracy': '55', 'Short Passing': '93', 'Volleys': '83', 'Dribbling': '88', 'Curve': '89', 'FreeKick Accuracy': '83', 'Long Passing': '93', 'Ball Control': '90', 'Acceleration': '76', 'Sprint Speed': '73', 'Agility': '76', 'Reactions': '91', 'Balance': '78', 'Shot Power': '92', 'Jumping': '63', 'Stamina': '88', 'Strength': '74', 'Long Shots': '91', 'Aggression': '75', 'Interceptions': '66', 'Positioning': '88', 'Vision': '94', 'Penalties': '83', 'Composure': '89', 'Marking': '68', 'Standing Tackle': '65', 'Sliding Tackle': '53', 'GK Diving': '15', 'GK Handling': '13', 'GK Kicking': '5', 'GK Positioning': '10', 'GK Reflexes': '13', 'Striker (ST)': '86', 'Left Wing (LW)': '88', 'Left Forward (LF)': '87', 'Center Forward (CF)': '87', 'Right Forward (RF)': '87', 'Right Wing (RW)': '88', 'Center Attacking Midfielder (CAM)': '91', 'Left Midfielder (LM)': '91', 'Center Midfielder (CM)': '91', 'Right Midfielder (RM)': '91', 'Left Wing Back (LWB)': '82', 'Center Defensive Midfielder (CDM)': '82', 'Right Wing Back (RWB)': '82', 'Left Back (LB)': '78', 'Center Back (CB)': '72', 'Right Back (RB)': '78', 'Goalkeeper (GK)': '24', 'Attacking Average': '82', 'Attacking Total': '410', 'Skill Average': '89', 'Skill Total': '443', 'Movement Average': '79', 'Movement Total': '394', 'Power Average': '82', 'Power Total': '408', 'Mentality Average': '83', 'Mentality Total': '495', 'Defending Average': '62', 'Defending Total': '186', 'Goalkeeping Average': '11', 'Goalkeeping Total': '56', 'Base stats': '483', 'Total Stats': '2298', 'Overall': '91', 'Potential': '91', 'Stats': '2298', 'Pace': 74, 'Dribbling_overall': 87, 'Defending': 64, 'Passing': 93, 'Physical': 77, 'Shooting': 88}


# I was getting differences between this and the real life version because I was just doing integer division 
# instead of using float division and rounding to the nearest integer depending on whether or not the decimal part is 
# greater than or less than 0.5

def create_custom_6_attributes_update_no_skemishes():
    #define a list in the correct order to store the attributes calculated
    the_six_main_attributes = ["Pace","Dribbling_overall","Defending","Passing","Physical","Shooting"]
    for player in all_players_ultra:
        all_six_values = []
        for custom_attr_li in six_custom_combined:
            custom_val_sum = 0
            for pair in custom_attr_li:
                attr = pair[0]
                val = pair[1]
                if player[attr]!= "--":
                    #convert it into an integer and add it up to wanted_attr
                    custom_val_sum += int(player[attr]) * val
            # after finishing looping through all the pairs in the custom_attr_li, we divide the custom_val_sum by 100
            custom_val_sum_actual_value_out_of_hundred = round(custom_val_sum / 100)

            # the line above is what changed

            # next we get hold of the value and append it to the all_six_values_list
            all_six_values.append(custom_val_sum_actual_value_out_of_hundred)

        # after we finish our calculations, we zip the_six_main_attributes and all_six_values
        for attr,val in zip(the_six_main_attributes,all_six_values):
            # now we assign our new custom attributes and their respective values to each player's dictionary
            player[attr] = val

            # now overhere in the assigning of values, if I were to write the data gotten into a csv file, I could do 
            # this properly by assigning converting the number value to  

create_custom_6_attributes_update_no_skemishes()

# let's do something really cool. What we are going to do is that we are going to write the data gotten from 
# adding the custom attributes to the ultimate player details. 

# for the li, we will use all_players_ultra
def create_custom_csv(li):
    # let's create the headers that we will use for the dictionary
    if len(li) != 0:
        headers = li[0].keys()
        # print(headers)
    with open("all_player_details.csv",mode='w',newline = "",encoding = "utf-8") as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=headers)
        csv_writer.writeheader()

        for row in li:
            csv_writer.writerow(row)

# create_custom_csv(all_players_ultra)

# okay so that means that I have already created my csv_file with all the data that I need. 

# let's test this to see if its working
# print(all_players_ultra[0])
# print(all_players_ultra[1])
# very very very close to the real version of the 6 main attributes. 

def get_first_n_players(attribute, n,list):
    excellent_players_at_specificAttr = sorted(list,key = lambda player : int(player[attribute]) if player[attribute] != "--" else -1,reverse=True)
    #getting the first n players at specific attributes
    for i in range(n+1):
        print(excellent_players_at_specificAttr[i]["Player Name"] + " : " + str(excellent_players_at_specificAttr[i][attribute]))

# get_first_n_players("Pace",5,all_players_ultra)
# get_first_n_players("Shooting",5,all_players_ultra)
# get_first_n_players("Passing",5,all_players_ultra)
# get_first_n_players("Defending",5,all_players_ultra)
# get_first_n_players("Physical",5,all_players_ultra)
# get_first_n_players("Dribbling_overall",5,all_players_ultra)


# function to find player and get all his attributes
# The info can be an attribute for instance pace or maybe an info for instance weight

#please enter the correct attribute
# These function is more generic, if you enter a name and it has spaces and any of the names is inside the player's names,
# you get count to increment by one and if count increments by one we append the player who has any of the names inside 
#into the list of players_found
def find_player_and_info(name,info):
    players_found = []
    name_to_search_for = name.lower()
    # the user might enter a string of name with spaces inside it and some names 
    # may or may not be correct so what I will do is that if the user enters 
    # a string which has more spaces, I will split that string into a list and check if dny of those names is inside the 
    # player["Player Name"] string

    names_li = name_to_search_for.split(" ")
    for player in all_players_ultra:
        # some players have common names allthough their fullnames may be different, to avoid duplications,
        count = 0
        player_name = unicodedata.normalize('NFD', player['Player Name']).encode('ascii', 'ignore').decode('utf-8').lower()
        for name in names_li:
            if name in player_name.split(" "):
                count += 1
        #after we are done checking through all the names

        if name_to_search_for in player_name:
            players_found.append(player)
        elif count >= 1 or player_name == name_to_search_for:
            players_found.append(player)

    #after we are done searching we just get the players whose name we want and print out the attribute we want 

    for player in players_found:
        print(f"{player['Player Name']}  {info} : {player[info]}  ")


# say you want a function that finds a player and gets you a list of all the attributes you need 
def find_player_and_multiple_infos(name,info_list):
    players_found = []
    name_to_search_for = name.lower()
    # the user might enter a string of name with spaces inside it and some names 
    # may or may not be correct so what I will do is that if the user enters 
    # a string which has more spaces, I will split that string into a list and check if dny of those names is inside the 
    # player["Player Name"] string

    # some players have common names allthough their fullnames may be different, to avoid duplications,
    names_li = name_to_search_for.split(" ")
    for player in all_players_ultra:
        count = 0
        player_name = unicodedata.normalize('NFD', player['Player Name']).encode('ascii', 'ignore').decode('utf-8').lower()
        for name in names_li:
            if name in player_name.split(" "):
                count += 1
        #after we are done checking through all the names

        if name_to_search_for in player_name:
            players_found.append(player)
            # break
        elif count >= 1 or player_name == name_to_search_for:
            players_found.append(player)

    #after we are done searching we just get the players whose name we want and print out the attribute we want 

    for player in players_found:
        print(f"{player['Player Name']} \n ")
        print("Attributes are below")
        for attr in info_list:
            print(f"\n{attr} : {player[attr]}  ")

# Let's test this out 
# find_player_and_info("diogo Jose", "Finishing")
# Diogo José Teixeira da Silva  Finishing : 86  
# José Diogo Dalot Teixeira  Finishing : 52       
# Diogo António Cupido Gonçalves  Finishing : 69  
# Diogo Meireles Costa  Finishing : 6
# Diogo Filipe Rocha Costa  Finishing : 69        
# Diogo Filipe Pacheco Abreu  Finishing : 49
# Rúben Diogo da Silva Neves  Finishing : 65
# Joseph Aidoo  Finishing : 18
# Josep María Chavarría Pérez  Finishing : 48
# Josep Gayà Martínez  Finishing : 30
# Joseba Zaldúa Bengoetxea  Finishing : 32
# Diogo Filipe Pinto Leite  Finishing : 30
# Enzo Diogo Merques Gomes  Finishing : 57
# Enaldo Diogo Barbosa Prazeres  Finishing : 45
# Joseph Hungbo  Finishing : 62
# Ailton Diogo Coelho Barbosa  Finishing : 71
# Jose Luís García Vayá  Finishing : 58
# Jose Luís García Vayá  Finishing : 58
# Joseph Okumu  Finishing : 37
# Joseph Paintsil  Finishing : 68
# Josep Martínez Riera  Finishing : 6
# Diogo Nathan Peixe Barreto  Finishing : 61
# Diogo da Costa Silva  Finishing : 27
# Francois-Joseph Sollacaro  Finishing : 6
# Jose Herrera  Finishing : 59
# Diogo Costa Pinto  Finishing : 60
# Josef Bursik  Finishing : 20
# Peter Jose Torreiro Costa  Finishing : 11
# Josecarlos Van Rankin  Finishing : 34  
# Diogo Lucas Queirós  Finishing : 38
# Jose María Pérez García  Finishing : 28
# Diogo Alexandre Almeida Mendes  Finishing : 42
# Fábio Diogo Agrela Ferreira  Finishing : 32
# João Diogo Fonseca Ferreira  Finishing : 31
# Joseph Attamah  Finishing : 27
# Josef Martínez  Finishing : 81
# Diogo dos Santos Cabral  Finishing : 46
# Joseph Lopy  Finishing : 68
# Joseph Espinoza  Finishing : 32
# Joseph Ceesay  Finishing : 61
# Joseph Ganda  Finishing : 60
# Diogo Pinheiro Monteiro  Finishing : 19
# Joseph Rosales  Finishing : 39
# Joseph Mora  Finishing : 44
# Lenny Joseph  Finishing : 67
# Joseph N’Duquidi  Finishing : 37  
# Joseph Anang  Finishing : 6
# Josep Señé Escudero  Finishing : 63
# Jose Antonio Delgado Villar  Finishing : 59
# Josepmir Ballón  Finishing : 58
# Joseph Boyamba  Finishing : 67
# Jose Joaquim de Carvalho  Finishing : 69
# Diogo Sousa Verdasca  Finishing : 28
# Kyle Joseph  Finishing : 63
# Joseph Mendes  Finishing : 62
# Josef Weberbauer  Finishing : 22
# Joseph Efford  Finishing : 65
# Joseph-Claude Gyau  Finishing : 55
# Joseph Gbode  Finishing : 50
# Joseph Olowu  Finishing : 32
# Josef Brian Baccay  Finishing : 40
# Joseph Amoako  Finishing : 52

# The function below is what really works
# I need more accurate results
# to avoid all the stress I can possibly get into I need the user to enter two
def find_player_and_info_1(name,info):
    players_found = []
    name_to_search_for = unicodedata.normalize('NFC',name.lower())
    # the user might enter a string of name with spaces inside it and some names 
    # may or may not be correct so what I will do is that if the user enters 
    # a string which has more spaces, I will split that string into a list and check if dny of those names is inside the 
    # player["Player Name"] string

    names_li = name_to_search_for.split(" ")
    # print(names_li)
    for player in all_players_ultra:
        # some players have common names allthough their fullnames may be different, to avoid duplications,
        count = 0
        player_name = unicodedata.normalize('NFD', player['Player Name']).encode('ascii', 'ignore').decode('utf-8').lower()
        # player_name = player["Player Name"].lower()
        for part_name in names_li:
            if part_name in player_name:
                count += 1
        #after we are done checking through all the names
        
        #if we find the exact player we are looking for just break out of the loop 
        if name_to_search_for ==  player_name:
            # print(count, "gotten from exact match")
            players_found.append(player)
            break
        # I need more than two names to be accurate
        elif count >= 2 or player_name == name_to_search_for:
            # print(count)
            # print(count, "gotten from multiple part names matching")
            players_found.append(player)

    #after we are done searching we just get the players whose name we want and print out the attribute we want 

    for player in players_found:
        print(f"{player['Player Name']}  {info} : {player[info]}  ")

# find_player_and_info_1("diogo Jose", "Finishing")

# 2  gotten from multiple part names matching
# 2 gotten from multiple part names matching
# Diogo José Teixeira da Silva  Finishing : 86  
# José Diogo Dalot Teixeira  Finishing : 52 

# find_player_and_info_1("Lionel messi","Finishing")

# 2 gotten from exact match
# Lionel Messi  Finishing : 90

find_player_and_info_1("Robert Lewandowski", "Dribbling_overall")
# Robert Lewandowski  Dribbling_overall : 85  










# if there is any error in the ranking, it probably means in the csv file, the attibute's value couldn't be gotten 
# so it was replaced with "--". later on,  I will write code that searches for and automatically replaces the -- values with 
# the real values gotten from the internet


