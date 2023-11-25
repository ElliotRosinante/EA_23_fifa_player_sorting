import random
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
attackers = [ "Striker (ST)","Left Wing (LW)","Left Forward (LF)","Center Forward (CF)","Right Forward (RF)","Right Wing (RW)","Center Attacking Midfielder (CAM)","Left Midfielder (LM)","Center Midfielder (CM)","Right Midfielder (RM)"]
defenders = ["Left Wing Back (LWB)","Center Defensive Midfielder (CDM)","Right Wing Back (RWB)","Left Back (LB)","Center Back (CB)","Right Back (RB)"]

# merge these lists
main_positions = attackers + defenders

# for key,value in player_positions_info.items():
#     print(key,value)
all_positions_list = []

all_players = []
with open("playerDetailedStats_main.csv",mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        all_players.append(row)

for key,value in player_positions_info.items():
    curr_dic = {
        "position-name" : value,
        "players-who-play-that-position" : []
    }
    #loop through the players, if there are any players who play that position, add them to the list
    for player in all_players:
        if curr_dic["position-name"] in player["Best Position"]:
            curr_dic["players-who-play-that-position"].append(player)
    all_positions_list.append(curr_dic)

#loop through all_positions_list and just print out the first 10 characters of each position dictionary and see
# if my method of grouping the players by position worked.

for dic in all_positions_list:
    for player in dic["players-who-play-that-position"][:11]:
        print(player["Player Name"])
        print(player["Best Position"])


def check_which_positions_are_empty():
    # how many positions are non-existent in the csv file containing all the player details
    count = 0
    for dic in all_positions_list:
        if len(dic["players-who-play-that-position"]) == 0:
            print(dic["position-name"])
            count += 1

    print("Number of positions which are not in the game but are in my dictionary are", count)

check_which_positions_are_empty()
















# list of  all the things I want to do.
# I want to be able to create a random team where all the players have different positions.
# Using the random module, the players of each team will be random each and every time. 
# a GK, a RB, a LB, a CAM, a CDM, a RW, a LW, a ST
# To do this, I will loop through the positions dictionary and create a dictionary out of each position, and make a list 
# one of the values, loop through the playes list and if the player has the same position as the position in that specific
# dictionary, I will append the player to that list. 

# one problem is that since wing back might be in either left wing back or right wing back , it may cause a problem 
# because the string comparison I am using is weak and forgiving. should I use a strong string comparison for just that one case?