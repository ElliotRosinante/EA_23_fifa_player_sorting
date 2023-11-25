import requests
import time
from bs4 import BeautifulSoup
import csv

player_positions_info = {
    "CM": "Center Midfielder",
    "CAM": "Center Attacking Midfielder",
    "CDM": "Center Defensive Midfielder",
    "ST": "Striker",
    "LS": "Left Striker",
    "RS": "Right Striker",
    "LF": "Left Forward",
    "RF": "Right Forward",
    "GK": "Goalkeeper",
    "CB": "Center Back",
    "LB": "Left Back",
    "RB": "Right Back",
    "RW": "Right Winger",
    "LW": "Left Winger",
    "LM": "Left Midfielder",
    "RM": "Right Midfielder",
    "RWB": "Right WingBack",
    "LWB": "Left WingBack",
    "CF": "Center Forward",
    "SW": "Sweeper",
    "DM": "Defensive Midfielder",
    "AM": "Attacking Midfielder",
    "WF": "Wide Forward",
    "SS": "Secondary Striker",
    "FS": "False Striker",
    "FB": "Full Back",
    "CB": "Centre Back",
    "DF": "Defender",
    "M": "Midfielder",
    "F": "Forward",
    "W": "Winger",
    "WB": "Wing Back",
}

with open("playerShallowStats_1.csv",mode = "w",newline = '',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Team","Height","Weight","Jersey Number","Position Shorthand", "Position Longhand","Country","Overall","Potential","Stats","Detailed link"])

all_player_links = []

r = requests.get("https://www.fifaratings.com/teams")
doc = BeautifulSoup(r.text,"html.parser")
all_teams_and_leagues_links = doc.select(".entries a")
all_teams_elements = [link for link in all_teams_and_leagues_links if "team" in link.attrs["href"]]
all_leagues_elements = [link for link in all_teams_and_leagues_links if "league" in link.attrs["href"]]

duplicates_removed_team_links = []
for link in all_teams_elements:
    href = link.attrs["href"]
    if href not in [link.attrs["href"] for link in duplicates_removed_team_links]:
        duplicates_removed_team_links.append(link)


for link in duplicates_removed_team_links:
    current_team_page = requests.get(link.attrs["href"]).text
    team_doc = BeautifulSoup(current_team_page,"html.parser")
    for row in team_doc.select_one("tbody").select("tr"):
        player_entries = row.select(".entries")
        if len(player_entries)!= 0:
            element_containing_team_name = team_doc.find('h1', {'class': 'header-title pt-2 mb-0'})
            for player in player_entries:
                team_of_player = element_containing_team_name.text
            try:
                player_name_element = [player_entry.select_one(".entry-font") for player_entry in player_entries]
                if player_name_element:
                    player_name = player_name_element[-1].select_one("a").text
                    print(f"**** {player_name}")
                else:
                    print("player_name_element is empty!")
            except IndexError:
                print("player_name_element is empty!")
                pass
            player_details_elem = row.find("div", class_="text-nowrap entry-subtext-font crop-subtext-font")
            if player_details_elem is not None:
                    player_details = player_details_elem.text
                    player_details_arr = player_details.strip().split("|")
                    height,weight = [value.lstrip() for value in player_details_arr[1:]]
                    jersey_number = player_details_arr[0].strip().split(" ")[0] 
                    length = len(player_details_arr[0].strip().split(" "))   #should be 4
                    player_position_shorthand = player_details_arr[0].strip().split(" ")[length-1]
                    player_position_longhand = player_positions_info[player_position_shorthand]
                    player_country_elem = row.select_one(".all-star-badge-list img")
                    if player_country_elem is not None and 'title' in player_country_elem.attrs:
                        player_country_of_origin = player_country_elem.attrs["title"]
                        # or use player_country_elem.attrs["alt"] instead of "title" if needed
                    else:
                        pass                
            table_data = row.select("td")
            table_data_values = [value.text for value in table_data ]
            # the stats value contained "," so I had to remove them 
            player_attribute_data_values = [int(value.text.replace(",","")) for value in table_data if value.text.isdigit() or "," in value.text]
            if len(player_attribute_data_values) != 0:
                overall,potential,stats = player_attribute_data_values
            player_link_elem = row.select_one(".entry-font a")
            if player_link_elem is not None:
                player_link = player_link_elem.attrs["href"]
                all_player_links.append(player_link)
            print(player_name)
            print(team_of_player)
            print(height)
            print(weight)
            print(jersey_number)
            print(player_position_shorthand)
            print(player_position_longhand)
            print(player_country_of_origin)
            print(overall)
            print(potential)
            print(stats)
            print(player_link)
            #read each row and append the data
            with open("playerShallowStats_1.csv",mode = "a", newline = '',encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([player_name,team_of_player,height.strip(),weight,jersey_number,player_position_shorthand,player_position_longhand,player_country_of_origin,overall,potential,stats,player_link])
        else:
            continue
time.sleep(5)
        #after it sleeps for 10 seconds, it will go to the next row.

print(all_player_links)