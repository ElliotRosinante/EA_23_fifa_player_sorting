import requests
import time
from bs4 import BeautifulSoup
import csv

with open("playerShallowstats.csv",encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    detailed_link_col_index = headers.index('Detailed link')
    for row in csv_reader:
        detailed_link_value = row[detailed_link_col_index]
        print(detailed_link_value)

        # so we now have the href of each individual player so we need to scrape each individual attribute
        r = requests.get(detailed_link_value)
        player_page = BeautifulSoup(r.text,"html.parser")
        name_element = player_page.find('h1', {'class': 'header-title pt-2 mb-0'})
        print(name_element.text)
        essential_details_element = player_page.select_one(".header-subtitle")
        player_details = essential_details_element.find_all("p",{'class': "mb-0"})

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
            if i == 6:
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
                print(attribute_value_li)

        break