import csv
import random 

attackers = [ "Striker (ST)","Left Wing (LW)","Left Forward (LF)","Center Forward (CF)","Right Forward (RF)","Right Wing (RW)","Center Attacking Midfielder (CAM)","Left Midfielder (LM)","Center Midfielder (CM)","Right Midfielder (RM)"]
defenders = ["Left Wing Back (LWB)","Center Defensive Midfielder (CDM)","Right Wing Back (RWB)","Left Back (LB)","Center Back (CB)","Right Back (RB)"]
neutral = ["Goalkeeper (GK)"]
# merge these lists
main_positions = attackers + defenders + neutral
# print(main_positions)
# loop through main_positions and create create out of the each position.

all_players = []
players = []
all_positions_list = []
all_positions_list_1 = []
with open("playerDetailedStats_main.csv",mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        all_players.append(row)
    
for position in main_positions:
    curr_dic = {
        "position-name" : position,
        "players-who-play-that-position" : []
    }
    for player in all_players:
        if player["Best Position"] == curr_dic["position-name"]:
            curr_dic["players-who-play-that-position"].append(player)

    all_positions_list.append(curr_dic)


def get_ten_players_in_each_position():
    for dic in all_positions_list:
        for player in dic["players-who-play-that-position"][:10]:
            print(player["Player Name"],player["League"],player["Team"],player["Best Position"])

# get_ten_players_in_each_position()

#let's go ahead and create a function that creates a random team consisting of players from different positions each time. 
def create_random_team():

    # we want just 11 players
    # we may need more than 11 players since we may need some subs and bench players
    random_team = []
    for dic in all_positions_list:
        # print(len_players_in_that_position)
        # print(random_index)
        if len(dic["players-who-play-that-position"]) == 0:
            print(dic["position-name"])
            print("This your position list has no occupants")
        else:
            len_players_in_that_position = len(dic["players-who-play-that-position"])
            # print(len_players_in_that_position)
            # random_index = random.randint(0,len_players_in_that_position+1)
            random_index = random.randint(0,len_players_in_that_position-1)
            # print(random_index)
            # print(dic["players-who-play-that-position"][random_index])
            random_team.append(dic["players-who-play-that-position"][random_index])
        
    # print(random_team)
    for player in random_team:
        print(player["Player Name"],player["League"],player["Team"],player["Best Position"])
    return random_team

# create_random_team()

# function to create random teams for two players and the player with the highest overralls wins. 
def read_specified_csv(filename):
    with open(filename,mode= "r",encoding="utf-8") as csv_file:
        csv_file = csv.DictReader(csv_file)
        for player in csv_file:
            players.append(player)


def group_players_by_position():
    for position in main_positions:
        curr_dic = {
        "position-name" : position,
        "players-who-play-that-position" : []
        }
        for player in players:
            position_name = curr_dic["position-name"].split("(")[1].split(")")[0]
            # print(position_name)
            if player["Position Shorthand"] == position_name:
                curr_dic["players-who-play-that-position"].append(player)

        all_positions_list_1.append(curr_dic)

def create_random_team_1():
    random_team = []
    for dic in all_positions_list_1:
        if len(dic["players-who-play-that-position"]) == 0:
            print(dic["position-name"])
            print("This your position list has no occupants")
        else:
            len_players_in_that_position = len(dic["players-who-play-that-position"])
            random_index = random.randint(0,len_players_in_that_position-1)
            random_team.append(dic["players-who-play-that-position"][random_index])

    for player in random_team:
        print(player["Name"],player["Team"],player["Position Shorthand"],player["Overall"])
    return random_team

read_specified_csv("playerShallowStats_1.csv")
group_players_by_position()
# create_random_team_1()

# so now let's start creating the game, player with the team that has the highest total overrall wins.
def game_init():
    player_1_name = input("Enter your name, player 1: ")
    player_2_name = input("Enter your name, player 2: ")

    player_1_team = create_random_team_1()
    for i in range(4):
        print("\n")
    player_2_team = create_random_team_1()

    totale_overall_player_1 = 0
    totale_overall_player_2 = 0
    for player in player_1_team:
        totale_overall_player_1 += int(player["Overall"])
    for player in player_2_team:
        totale_overall_player_2 += int(player["Overall"])

    print(f'''
    {player_1_name} : {str(totale_overall_player_1)} points
    {player_2_name} : {str(totale_overall_player_2)} points
    ''')
    print("\n")
    print("\n")
    if totale_overall_player_1 > totale_overall_player_2:
        print(f"{player_1_name} wins the game with an overall of {totale_overall_player_1} points!!")

    elif totale_overall_player_2 == totale_overall_player_1:
        print(f"This game ended in a draw with both teams having {totale_overall_player_2} points!!")
    else:
        print(f"{player_2_name} wins the game with an overall of {totale_overall_player_2} points!!")

game_init()
# There is a possibility that there is an empty list somewhere, that is why I am probably getting a list error
# Initially I waas getting an error that list index was out of range, that was because I wasn't checking if the list 
# was empty before I selected an element out of the list. That was wrong on my part. 
# So what I will do is that, I will use error handling to handle the empty list so that I don't try to randomly select from 
# an empty list. 

# getting this error 
# Traceback (most recent call last):
#   File "C:\Users\HP\Desktop\experimental_scapper\combine_random_players_2.py", line 63, in <module>
#     create_random_team()
#   File "C:\Users\HP\Desktop\experimental_scapper\combine_random_players_2.py", line 54, in create_random_team
#     random_team.append(dic["players-who-play-that-position"][random_index])
#                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
# IndexError: list index out of range

# It appears the reason why I was getting this IndexError: list index out of range was because of the range I was using for the 
# random.randint method. I incremented the second parameter by 1 so let's say the list has 7 elements, my range was 
# between 0 and 8 instead of between 0 and 7

# Another mistake I was making was that : I was selecting between the ranges of 0 to len instead of from 0 to len-1
# mistake 1: selecting from ranges of 0 to len + 1 instead of from ranges of 0 to len - 1 
# mistake 2: selecting from ranges of 0 to len instead of from 0 to len -1 
# It appears that for the random.randit method, both parameters are inclusive