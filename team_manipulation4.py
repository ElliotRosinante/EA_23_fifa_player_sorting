import csv
import json
all_teams_list = []
players = []
all_attributes = [
    "Weak Foot","Skill moves","International Reputation","Crossing","Finishing","Heading Accuracy",
    "Short Passing","Volleys","Dribbling","Curve","FreeKick Accuracy","Long Passing","Ball Control",
    "Acceleration","Sprint Speed","Agility","Reactions","Balance","Shot Power","Jumping","Stamina",
    "Strength","Long Shots","Aggression","Interceptions","Positioning","Vision","Penalties","Composure",
    "Marking","Standing Tackle","Sliding Tackle","GK Diving","GK Handling","GK Kicking","GK Positioning",
    "GK Reflexes","Striker (ST)","Left Wing (LW)","Left Forward (LF)","Center Forward (CF)",
    "Right Forward (RF)","Right Wing (RW)","Center Attacking Midfielder (CAM)","Left Midfielder (LM)",
    "Center Midfielder (CM)","Right Midfielder (RM)","Left Wing Back (LWB)",
    "Center Defensive Midfielder (CDM)","Right Wing Back (RWB)","Left Back (LB)",
    "Center Back (CB)","Right Back (RB)","Goalkeeper (GK)","Attacking Average","Attacking Total",
    "Skill Average","Skill Total","Movement Average","Movement Total","Power Average",
    "Power Total","Mentality Average","Mentality Total","Defending Average","Defending Total",
    "Goalkeeping Average","Goalkeeping Total","Base stats","Total Stats"
]

team_players_grouped = []
# get the list of all the teams
with open("team_attributes.csv",newline="",encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        all_teams_list.append(row["TeamName"])

# get the list of all the players
# filename = "playerDetailedStats_main.csv"
filename = "all_player_details.csv"
with open(filename,newline = '',encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        players.append(row)

def groupPlayersByTeam():
    for team in all_teams_list:
        current_dictionary = {

        }
        current_dictionary["team-name"] = team
        current_dictionary["team-players"] = []
        for player in players:
            if player["Team"] == team:
                current_dictionary["team-players"].append(player)
            else:
                pass
                
        team_players_grouped.append(current_dictionary)

groupPlayersByTeam()

with open("teams_grouped_2.json",'w',encoding = 'utf-8') as json_file:
    json.dump(team_players_grouped,json_file)

print("Data stored in json format.")

# we write the list with all the players and their custom attributes grouped by teams into a json file so that 
# we can read it into a different file and use it for our computation. 


# for dictionary in team_players_grouped:
#     if "Manchester City" in dictionary["team-name"]:
#         print(len(dictionary["team-players"]))
#         for player in dictionary["team-players"]:
#             print(player["Player Name"])

def get_players_over_different_n_values(li_attr,li_values,team_li):
    # create a variable to store the boolean responsible for exiting the function or returning the list.
    scale = False
    # if the length of the attributes and the length of the values aren't the same, raise an error. 
    attributes_length = len(li_attr)
    values_length = len(li_values)
    if attributes_length != values_length:
        print("your values don't match your attributes")
        scale = False
        return [scale]

    # group each attribute and value into a tuple
    unique_players = []
    for player in team_li:
        count = 0
        for attribute,val in zip(li_attr,li_values):
            try:
                if int(player[attribute]) >= val:
                    count += 1
            except ValueError:
                pass

        # after the player has checked for all the values, if he satisfies all the criteria, append the player to the list
        if count == len(li_attr):
            unique_players.append(player)
    if len(unique_players) == 0:
        scale = False 
        return [scale]
    else:
        return [True,unique_players]

def get_all_players_over_n(li,n,team_li):
    unique_players = []
    len_attr = len(li)
    for player in team_li:
        count = 0 
        for attribute in li:
            try:
                if int(player[attribute]) >= n:
                    count += 1
            except ValueError:
                pass

        if count == len_attr:
            unique_players.append(player)
    # print(unique_players)
    if len(unique_players) == 0:
        return [False]
    else : 
        return [True,unique_players]



# what I want to do. 
# if a team has players who have certain attributes I specifically am targetting over 90 or 85 
# I want that to know how many players of that calibur that team has and the names and positions of those players 

# list of attributes I desire
omg_dribblers  = ["Agility","Balance", "Ball Control","Dribbling"]
omg_defenders = ["Standing Tackle","Sliding Tackle","Marking"]
scoring_attributes = ["Finishing","Shot Power","Long Shots"]
# How do you even return multiple values from a function
def findteamsWithUniquePlayers(li,n):
    all_special_players = []
    for dictionary in team_players_grouped:
        decidingVal = get_all_players_over_n(li,n,dictionary["team-players"])
        if decidingVal[0]:
            all_special_players.append(decidingVal[1])
    # these are team-players who satisfy the attributes in the list
    for team_players in all_special_players:
        print(team_players[0]["Team"] + f"  | no. of unique players {len(team_players)}")
        for player in team_players:
            print(player["Player Name"], player["Team"] , player["Best Position"])
            strline = " "
            for attribute in li:
                strline += attribute 
                strline += f": {player[attribute]}  | "
            print(strline)
        
def findteamsWithUniquePlayers_over_different_n(attr_li,attr_val_li):
    all_special_players = []
    for dictionary in team_players_grouped:
        decidingVal = get_players_over_different_n_values(attr_li,attr_val_li,dictionary["team-players"])
        if decidingVal[0]:
            all_special_players.append(decidingVal[1])
    # these are team-players who satisfy the attributes in the list
    for team_players in all_special_players:
        print(team_players[0]["Team"] + f"  | no. of unique players {len(team_players)}")
        for player in team_players:
            print(player["Player Name"], player["Team"] , player["Best Position"])
            strline = " "
            for attribute in attr_li:
                strline += attribute 
                strline += f": {player[attribute]}  | "
            print(strline)

killer_defending_attributes = ["Standing Tackle","Sliding Tackle","Strength","Aggression"]
killer_defending_values = [85,85,80,75]

decent_dribbling_attributes = ["Dribbling","Ball Control","Agility","Balance"]
decent_dribbling_values = [88,89,80,80]
decent_dribbling_passing_attributes = ["Dribbling","Ball Control","Agility","Balance", "Short Passing"]
decent_dribbling_passing_values = [88,89,80,80,85]
scoring_killers_attributes  = ["Finishing","Penalties","Shot Power"]
scoring_killers_values = [90,85,85]
fast_and_accurate_scoring_attributes = ["Finishing","Penalties","Acceleration","Sprint Speed","Shot Power"]
fast_and_accurate_scoring_values = [90,80,80,80,85]
dribbling_and_shooting_qualities = ["Dribbling","Ball Control","Finishing","Shot Power","Acceleration","Agility","Balance"]
dribbling_and_shooting_qualities_values = [87,84,82,80,82,82,82]
# findteamsWithUniquePlayers_over_different_n(scoring_killers_attributes,scoring_killers_values)
best_passing_attributes = ["Vision","Short Passing","Long Passing"]
best_passing_values = [85,85,80]
# findteamsWithUniquePlayers_over_different_n(best_passing_attributes,best_passing_values)
ultimate_scoring_lowered_standards_attributes = ["Positioning","Finishing","Sprint Speed","Acceleration","Shot Power"]
ultimate_scoring_lowered_standards_attributes_values = [83,87,80,80,80]
# findteamsWithUniquePlayers_over_different_n(ultimate_scoring_lowered_standards_attributes,ultimate_scoring_lowered_standards_attributes_values)
# print("Players good at both dribbling and shooting")
# print("Players who are excellent at defending")
# findteamsWithUniquePlayers_over_different_n(killer_defending_attributes,killer_defending_values)
# print("Players excellent at finishing and dribbling")
# findteamsWithUniquePlayers_over_different_n(["Finishing","Dribbling"],[90,90])
# findteamsWithUniquePlayers_over_different_n(["Short Passing","Long Passing"],[90,90])
# findteamsWithUniquePlayers_over_different_n(dribbling_and_shooting_qualities,dribbling_and_shooting_qualities_values)
# findteamsWithUniquePlayers_over_different_n(["Dribbling","Acceleration","Ball Control","Finishing"],[89,85,88,80])
# findteamsWithUniquePlayers_over_different_n(["Short Passing"],[90])
# findteamsWithUniquePlayers_over_different_n(killer_defending_attributes,killer_defending_values)
# findteamsWithUniquePlayers_over_different_n(decent_dribbling_attributes,decent_dribbling_values)
# findteamsWithUniquePlayers_over_different_n(decent_dribbling_passing_attributes,decent_dribbling_passing_values)
# findteamsWithUniquePlayers(omg_dribblers,90)
# findteamsWithUniquePlayers(killer_defending_attributes,91)
# findteamsWithUniquePlayers(["Skill moves"],5)
# findteamsWithUniquePlayers(omg_defenders,88)

# findteamsWithUniquePlayers(scoring_attributes,90)

# Al Nassr  | no. of unique players 1
# Cristiano Ronaldo Al Nassr Striker (ST)
#  Finishing: 93  | Shot Power: 93  | Long Shots: 90  |

# findteamsWithUniquePlayers(scoring_attributes,85)
# findteamsWithUniquePlayers(["Finishing"],90)

# Manchester City  | no. of unique players 1
# Erling Haaland Manchester City Striker (ST)
#  Finishing: 94  |
# Real Madrid CF  | no. of unique players 1
# Karim Benzema Real Madrid CF Center Forward (CF)
#  Finishing: 92  |
# Paris Saint-Germain  | no. of unique players 2
# Kylian Mbappé Paris Saint-Germain Striker (ST)
#  Finishing: 93  |
# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Finishing: 90  |
# Liverpool  | no. of unique players 1
# Mohamed Salah Liverpool Right Wing (RW)
#  Finishing: 93  |
# FC Barcelona  | no. of unique players 1
# Robert Lewandowski FC Barcelona Striker (ST)
#  Finishing: 94  |
# Tottenham Hotspur  | no. of unique players 2
# Harry Kane Tottenham Hotspur Striker (ST)
#  Finishing: 93  |
# Heung Min Son Tottenham Hotspur Left Wing (LW)
#  Finishing: 91  |
# Lazio  | no. of unique players 1
# Ciro Immobile Lazio Striker (ST)
#  Finishing: 91  |
# Leicester City  | no. of unique players 1
# Jamie Vardy Leicester City Striker (ST)
#  Finishing: 90  |
# RC Celta de Vigo  | no. of unique players 1
# Iago Aspas Juncal RC Celta de Vigo Striker (ST)
#  Finishing: 90  |
# Al Nassr  | no. of unique players 1
# Cristiano Ronaldo Al Nassr Striker (ST)
#  Finishing: 93  |


# Al Nassr  | no. of unique players 1
# Cristiano Ronaldo Al Nassr Striker (ST)
#  Finishing: 93  | Shot Power: 93  | Long Shots: 90  |

# Manchester City  | no. of unique players 2
# Kevin De Bruyne Manchester City Center Midfielder (CM)
#  Finishing: 85  | Shot Power: 92  | Long Shots: 91  |
# Erling Haaland Manchester City Striker (ST)
#  Finishing: 94  | Shot Power: 94  | Long Shots: 87  |

# Paris Saint-Germain  | no. of unique players 1
# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Finishing: 90  | Shot Power: 86  | Long Shots: 91  |

# Tottenham Hotspur  | no. of unique players 2
# Harry Kane Tottenham Hotspur Striker (ST)
#  Finishing: 93  | Shot Power: 92  | Long Shots: 86  |
# Heung Min Son Tottenham Hotspur Left Wing (LW)
#  Finishing: 91  | Shot Power: 88  | Long Shots: 89  |

# AFC Richmond  | no. of unique players 1
# Jamie Tartt AFC Richmond Center Attacking Midfielder (CAM)
#  Finishing: 86  | Shot Power: 90  | Long Shots: 85  |
# Al Nassr  | no. of unique players 1

# Cristiano Ronaldo Al Nassr Striker (ST)
#  Finishing: 93  | Shot Power: 93  | Long Shots: 90  |



# Paris Saint-Germain  | no. of unique players 1
# Marcos Aoás Corrêa Paris Saint-Germain Center Back (CB)
#  Standing Tackle: 89  | Sliding Tackle: 89  | Marking: 90  |

# results
#  Manchester City
# 1
# Bernardo Mota Carvalho e Silva Manchester City Center Attacking Midfielder (CAM)
#  Agility: 94  | Balance: 92  | Ball Control: 91  | Dribbling: 92  |
# Paris Saint-Germain
# 2
# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Agility: 91  | Balance: 95  | Ball Control: 93  | Dribbling: 95  |
# Marco Verratti Paris Saint-Germain Center Midfielder (CM)
#  Agility: 90  | Balance: 93  | Ball Control: 92  | Dribbling: 91  |
# Toronto FC
# 1
# Lorenzo Insigne Toronto FC Center Attacking Midfielder (CAM)
#  Agility: 90  | Balance: 94  | Ball Control: 90  | Dribbling: 90  |


# bool object is not scriptable? what does that even mean


# build  a lot of projects, you will get significantly good at programming.

# findteamsWithUniquePlayers(["Strength","Standing Tackle","Marking"],88)

# Manchester City  | no. of unique players 1
# Rúben Santos Gato Alves Dias Manchester City Center Back (CB)
#  Strength: 89  | Standing Tackle: 89  | Marking: 90  |
# Liverpool  | no. of unique players 1
# Virgil van Dijk Liverpool Center Back (CB)
#  Strength: 93  | Standing Tackle: 92  | Marking: 92  |
# Inter  | no. of unique players 1
# Milan Škriniar Inter Center Back (CB)
#  Strength: 89  | Standing Tackle: 90  | Marking: 91  |
# Chelsea  | no. of unique players 1
# Kalidou Koulibaly Chelsea Center Back (CB)
#  Strength: 94  | Standing Tackle: 89  | Marking: 90  |

# findteamsWithUniquePlayers(["Sprint Speed","Acceleration"],90)

# I am sure this combination will be very rare 

# findteamsWithUniquePlayers(["Sprint Speed","Acceleration","Short Passing"],90) 
# I was right, there is no one who is that fast and accurate at passing at the same time.

# findteamsWithUniquePlayers(["Sprint Speed","Acceleration","Short Passing"],88) 
# still no one.

# findteamsWithUniquePlayers(["Sprint Speed","Acceleration","Short Passing"],85) 

# Paris Saint-Germain  | no. of unique players 2
# Kylian Mbappé Paris Saint-Germain Striker (ST)
#  Sprint Speed: 97  | Acceleration: 97  | Short Passing: 85  |
# Neymar da Silva Santos Jr. Paris Saint-Germain Left Wing (LW)
#  Sprint Speed: 86  | Acceleration: 88  | Short Passing: 85  |
# Atlético de Madrid  | no. of unique players 1
# Marcos Llorente Moreno Atlético de Madrid Center Attacking Midfielder (CAM)
#  Sprint Speed: 90  | Acceleration: 85  | Short Passing: 86  |
# RB Leipzig  | no. of unique players 1
# Christopher Nkunku RB Leipzig Center Attacking Midfielder (CAM)
#  Sprint Speed: 89  | Acceleration: 87  | Short Passing: 85  |
# AFC Richmond  | no. of unique players 1
# Moe Bumbercatch AFC Richmond Center Midfielder (CM)
#  Sprint Speed: 87  | Acceleration: 88  | Short Passing: 85  |


# quikly cooking a list of certain desirable attributes 
["Ball Control","Dribbling"]
["Dribbling","Long Passing","Short Passing"]
["Agility","Balance"]
["Dribbling","Long Passing"]
["Agility","Balance","Long Passing","Short Passing"]
["Dribbling","Ball Control","Finishing"]
["Agility","Balance","Ball Control","Finishing"]


# findteamsWithUniquePlayers(["Agility","Balance","Ball Control","Finishing"],80) 
# findteamsWithUniquePlayers(["Agility","Balance","Ball Control","Finishing"],90) 

# Paris Saint-Germain  | no. of unique players 1
# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Agility: 91  | Balance: 95  | Ball Control: 93  | Finishing: 90  |

# findteamsWithUniquePlayers(["Agility","Balance","Ball Control","Finishing"],85) 

# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Agility: 91  | Balance: 95  | Ball Control: 93  | Finishing: 90  |

# Liverpool  | no. of unique players 1
# Mohamed Salah Liverpool Right Wing (RW)
#  Agility: 90  | Balance: 91  | Ball Control: 88  | Finishing: 93  |

# Inter  | no. of unique players 1
# Lautaro Martínez Inter Striker (ST)
#  Agility: 86  | Balance: 89  | Ball Control: 86  | Finishing: 88  | 

# Atlético de Madrid  | no. of unique players 1
# Ángel Correa Atlético de Madrid Center Forward (CF)
#  Agility: 90  | Balance: 88  | Ball Control: 87  | Finishing: 86  |

# RB Leipzig  | no. of unique players 1
# Christopher Nkunku RB Leipzig Center Attacking Midfielder (CAM)
#  Agility: 88  | Balance: 90  | Ball Control: 88  | Finishing: 86  |

# AS Monaco  | no. of unique players 1
# Wissam Ben Yedder AS Monaco Center Forward (CF)
#  Agility: 91  | Balance: 91  | Ball Control: 88  | Finishing: 87  |
 