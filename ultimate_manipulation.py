import json 
# let's get the teams with all it's players grouped 
def open_json():
    with open("teams_grouped_2.json",'r',encoding = "utf-8") as json_file:
        all_teams_players = json.load(json_file)
        return all_teams_players

all_teams_players = open_json()
wing_positions = ["Right Wing (RW)","Left Wing (LW)"]
wing_plus_attacking_positions = ["Left Forward (LF)","Center Forward (CF)","Right Forward (RF)","Striker (ST)",
"Striker (ST)","Right Wing (RW)","Left Wing (LW)"]
attacking_absolute_positions = wing_plus_attacking_positions + ["Left Midfielder (LM)",
    "Center Midfielder (CM)","Right Midfielder (RM)"]
center_back_positions = ["Center Back (CB)"]
wing_defenders_positions = ["Right Back (RB)","Left Back (LB)","Right Wing Back (RWB)","Left Wing Back (LWB)"]
defending_absolute_positions = wing_defenders_positions + center_back_positions
# teams that have 4 or more really fast attackers.
def find_teams_with_fast_attackers():
    # target_positions_li = wing_plus_attacking_positions
    target_positions_li = attacking_absolute_positions
    for team in all_teams_players:
        players = team["team-players"]
        fast_attackers= [player for player in players if player["Best Position"] in  target_positions_li and int(player["Pace"])>=88]
        number_of_fast_attackers = len(fast_attackers)
        if number_of_fast_attackers >= 4:
            print(team["team-name"])
            # let's print the names of all the fast players 
            for player in fast_attackers:
                print(f'\t{player["Player Name"]}  pace : {player["Pace"]}')

def find_teams_with_fast_attackers_and_dribblers():
    # target_positions_li = wing_plus_attacking_positions
    target_positions_li = attacking_absolute_positions
    for team in all_teams_players:
        players = team["team-players"]
        fast_attackers_dribblers = [player for player in players if player["Best Position"] in target_positions_li and (int(player["Pace"])>=85 and int(player["Dribbling_overall"]) >= 80)]
        number_of_fast_attackers_dribblers = len(fast_attackers_dribblers)
        if number_of_fast_attackers_dribblers >= 1:
            print(team["team-name"])
            # let's print the names of all the fast players 
            for player in fast_attackers_dribblers:
                print(f'\t{player["Player Name"]}  pace : {player["Pace"]}  dribbling : {player["Dribbling_overall"]} ')

# find_teams_with_fast_attackers()
# find_teams_with_fast_attackers_and_dribblers()

# I need to create a function where I can dynamically create the conditions and pass it as a parameter/argument 
def find_teams_that_target_condition(condition,n):
    target_positions_li = []
    for team in all_teams_players:
        players = team["team-players"]
        players_satisfying_condition = [player for player in players if player["Best Position"] in target_positions_li and condition]
        number_of_players_satisfying_codition = len(players_satisfying_condition)

        if number_of_players_satisfying_codition >= n:
            print(team["team-name"])

        for player in players_satisfying_condition:
            print(f'\t{player["Player Name"]}')

# let's get fast defenders 
def find_teams_with_fast_defenders():
    target_positions_li = defending_absolute_positions
    for team in all_teams_players:
        players = team["team-players"]
        fast_defenders = [] 
        for player in players:
            if player["Best Position"] in target_positions_li and (int(player["Defending"])>= 80 and int(player["Pace"])>=80):
                fast_defenders.append(player)
        if len(fast_defenders) >= 1:
            print(team["team-name"])

            for player in fast_defenders:
                    print(f'\t{player["Player Name"]}  pace : {player["Pace"]} defending : {player["Defending"]}')

# find_teams_with_fast_defenders()


# let's sort defenders by defending ability so that we can get the best defenders in the game 
def get_defenders():
    target_positions = defending_absolute_positions
    all_defenders = []
    for team in all_teams_players:
        players = team["team-players"]
        for player in players:
            if player["Best Position"] in target_positions:
                all_defenders.append(player)
    #let's sort these defenders by different things 

    # we need something to display the positions
    count = 1
    # let's start sorting them by defending ability 
    defense = lambda x: int(x["Defending"])
    all_defenders_sorted_by_defense = sorted(all_defenders,key = defense,reverse=True)
    # print the first 15 of these along with their numbers 
    for player in all_defenders_sorted_by_defense[:15]:
        print(f'{count}. {player["Player Name"]}  defending : {player["Defending"]} team : {player["Team"]}')
        count += 1

    count = 1
    # let's also sort them by pace 
    speed = lambda x: int(x["Pace"])
    all_defenders_sorted_by_pace = sorted(all_defenders,key=speed,reverse=True)
    for player in all_defenders_sorted_by_pace[:15]:
        print(f'{count}. {player["Player Name"]} pace : {player["Pace"]} team : {player["Team"]}')
        count += 1

    count = 1
    # let's also sort them by physical
    muscles = lambda x: int(x["Physical"])
    all_defenders_sorted_by_muscles = sorted(all_defenders,key=muscles,reverse=True)
    for player in all_defenders_sorted_by_muscles[:15]:
        print(f'{count}. {player["Player Name"]} physical : {player["Physical"]} team : {player["Team"]}')
        count += 1
    count = 1
    # let's also sort them by dribbling ability 
    flur = lambda x : int(x["Dribbling_overall"])
    all_defenders_sorted_by_flur = sorted(all_defenders,key=flur,reverse=True)
    for player in all_defenders_sorted_by_flur[:15]:
        print(f'{count}. {player["Player Name"]} dribbling : {player["Dribbling_overall"]} team : {player["Team"]}')
        count += 1

    count = 1
    fire = lambda x : int(x["Shooting"])
    all_defenders_sorted_by_flur = sorted(all_defenders,key=fire,reverse=True)
    for player in all_defenders_sorted_by_flur[:15]:
        print(f'{count}. {player["Player Name"]} shooting : {player["Shooting"]} team : {player["Team"]}')
        count += 1

    count = 1
    tiki_taka = lambda x : int(x["Passing"])
    all_defenders_sorted_by_flur = sorted(all_defenders,key=tiki_taka,reverse=True)
    for player in all_defenders_sorted_by_flur[:15]:
        print(f'{count}. {player["Player Name"]} Passing : {player["Passing"]} team : {player["Team"]}')
        count += 1

# get_defenders()
def get_first_n_players(attribute, n,li):
    excellent_players_at_specificAttr = sorted(li,key = lambda player : int(player[attribute]) if player[attribute] != "--" else -1,reverse=True)
    names_of_excellent_players = [player["Player Name"] for player in excellent_players_at_specificAttr]

    #getting the first n players at specific attributes
    for i in range(n+1):
        print(excellent_players_at_specificAttr[i]["Player Name"] + " : " +  "attribute " + " : " + excellent_players_at_specificAttr[i][attribute] +  " team : " + excellent_players_at_specificAttr[i]["Team"])
all_players_li = []
for team in all_teams_players:
    all_players_li += team["team-players"]
# get_first_n_players("Pace",15,all_players_li)
# get_first_n_players("Shooting",15,all_players_li)
# get_first_n_players("Dribbling_overall",15,all_players_li)
# get_first_n_players("Defending",15,all_players_li)
# get_first_n_players("Physical",15,all_players_li)
# get_first_n_players("Passing",15,all_players_li)

# we want to build our team of the year using the best player at a specific attribute


all_positions_li = ["Striker (ST)","Left Wing (LW)","Left Forward (LF)","Center Forward (CF)",
    "Right Forward (RF)","Right Wing (RW)","Center Attacking Midfielder (CAM)","Left Midfielder (LM)",
    "Center Midfielder (CM)","Right Midfielder (RM)","Left Wing Back (LWB)",
    "Center Defensive Midfielder (CDM)","Right Wing Back (RWB)","Left Back (LB)",
    "Center Back (CB)","Right Back (RB)","Goalkeeper (GK)"]

# "Center Midfielder (CM)"
# # we need to split the positions so that we can just pair them. 
# ["Striker (ST)","Left Wing (LW)","Right Wing (RW)","Right Back (RB)","Left Back (LB)","Center Back (CB)","Left Midfielder (LM)",
# "Center Midfielder (CM)","Right Midfielder (RM)"]

# 'positions involving three defenders , positions involving four defenders'

# let's get the best 5 or 10 at each position and then we can then pick the ones we want and pair them up for the team
# of the year 

def find_best_at_specific_positions(li,n):
    #let's group the players according to their positions.
    curr_dictionary = {

    }
    for position in all_positions_li:
        # sort all the players in the team by that position
        sorted_positions = sorted(li,key=lambda x: int(x[position]) if x[position] != '--' else -1,reverse=True)
        curr_dictionary['players_sorted_by_{position}'] = sorted_positions
        for player in sorted_positions[:n]:
            print(f'{player["Player Name"]}  |  {position} : {player[position]}')

    # after we are done sorting and grouping, just return the dictionary 
    return curr_dictionary

players_grouped_by_positions = find_best_at_specific_positions(all_players_li,15)



