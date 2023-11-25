import csv

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
teams_with_attr_averages_calculated = []
with open("team_attributes.csv",newline="",encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        all_teams_list.append(row["TeamName"])

with open("playerDetailedStats_main.csv",newline = '',encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        players.append(row)

# function to handle the calculation of the averages of every attribute

def calcAverage_attribute(li,attribute):
    # if the player has an actual attribute and the attribute is not equal to "--"
    # append it to a list of player's who have that attribute
    players_who_have_value_for_target_attribute = [player for player in li if player[attribute] and player[attribute]!= "--"]
    team_totale_attr = 0
    try:
        len_players_with_attributes = len(players_who_have_value_for_target_attribute)
        for player in players_who_have_value_for_target_attribute:
            team_totale_attr += int(player[attribute])

        average_val_for_attr = team_totale_attr/len_players_with_attributes
        return average_val_for_attr
    
    except ZeroDivisionError:
        return -1
# function to find all attribute averages for every team
def assign_attrAverages():
    for team in all_teams_list:
        current_team_dictionary = {
        }
        current_team_dictionary["teamName"] = team
        current_team_dictionary["team-players"] = []
        for player in players:
            if player["Team"] == team:
                current_team_dictionary["team-players"].append(player)

        #calculate all the averages for every attribute in the list
        for attribute in all_attributes:
            team_attr_average = calcAverage_attribute(current_team_dictionary["team-players"],attribute)
            current_team_dictionary[f"teamAverage_{attribute}"] = team_attr_average
        teams_with_attr_averages_calculated.append(current_team_dictionary)

        #this way, I am done assigning all the averages


        # before I do any sorting I need to call this function first so it works with each and every player 
        # and each and every team then I can do whatever I want.

assign_attrAverages()

# for team in teams_with_attr_averages_calculated[:9]:
#     print(team["teamName"])

# sorting teams by unique attributes
teams_sorted_by_weakfoot = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Weak Foot"],reverse=True)
teams_sorted_by_skillmoves = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Skill moves"],reverse=True)
teams_sorted_by_reputation = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_International Reputation"],reverse=True)
teams_sorted_by_crossing = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Crossing"],reverse=True)
teams_sorted_by_finishing = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Finishing"],reverse=True)
teams_sorted_by_headers = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Heading Accuracy"],reverse=True)
teams_sorted_by_shortPassing = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Short Passing"],reverse=True)
teams_sorted_by_Volleys = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Volleys"],reverse=True)
teams_sorted_by_Dribbling = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Dribbling"],reverse=True)
teams_sorted_by_Curve = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Curve"],reverse=True)
teams_sorted_by_freekicks = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_FreeKick Accuracy"],reverse=True)
teams_sorted_by_LongPassing = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Long Passing"],reverse=True)
teams_sorted_by_BallControl = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Ball Control"],reverse=True)
teams_sorted_by_Acceleration = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Acceleration"],reverse=True)
teams_sorted_by_SprintSpeed = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Sprint Speed"],reverse=True)
teams_sorted_by_Agility = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Agility"],reverse=True)
teams_sorted_by_reactions = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Reactions"],reverse=True)
teams_sorted_by_balance = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Balance"],reverse=True)
teams_sorted_by_ShotPower = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Shot Power"],reverse=True)
teams_sorted_by_jumping = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Jumping"],reverse=True)
teams_sorted_by_stamina = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Stamina"],reverse=True)
teams_sorted_by_strength = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Strength"],reverse=True)
teams_sorted_by_LongShots = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Long Shots"],reverse=True)
teams_sorted_by_Aggression = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Aggression"],reverse=True)
teams_sorted_by_Intercptions = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Interceptions"],reverse=True)
teams_sorted_by_Positioning = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Positioning"],reverse=True)
teams_sorted_by_Vision = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Vision"],reverse=True)
teams_sorted_by_Penalties= sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Penalties"],reverse=True)
teams_sorted_by_Composure = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Composure"],reverse=True)
teams_sorted_by_Marking = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Marking"],reverse=True)
teams_sorted_by_StandingTackle = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Standing Tackle"],reverse=True)
teams_sorted_by_SlidingTackle = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Sliding Tackle"],reverse=True)
teams_sorted_by_GKDiving = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_GK Diving"],reverse=True)
teams_sorted_by_GKHandling= sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_GK Handling"],reverse=True)
teams_sorted_by_GKkicking = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_GK Kicking"],reverse=True)
teams_sorted_by_GKPositioning= sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_GK Positioning"],reverse=True)
teams_sorted_by_GKReflexes = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_GK Reflexes"],reverse=True)
teams_sorted_by_AttackingAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Attacking Average"],reverse=True)
teams_sorted_by_AttackingTotal = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Attacking Total"],reverse=True)
teams_sorted_by_SkillAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Skill Average"],reverse=True)
teams_sorted_by_SkillTotal= sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Skill Total"],reverse=True)
teams_sorted_by_MovementAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Movement Average"],reverse=True)
teams_sorted_by_MovementTotal = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Movement Total"],reverse=True)
teams_sorted_by_PowerAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Power Average"],reverse=True)
teams_sorted_by_PowerTotal = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Power Total"],reverse=True)
teams_sorted_by_MentalityAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Mentality Average"],reverse=True)
teams_sorted_by_MentalityTotal= sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Mentality Total"],reverse=True)
teams_sorted_by_DefendingAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Defending Average"],reverse=True)
teams_sorted_by_DefendingTotal = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Defending Total"],reverse=True)
teams_sorted_by_GoalkeepingAverage = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Goalkeeping Average"],reverse=True)
teams_sorted_by_GoalkeepingTotal = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Goalkeeping Total"],reverse=True)
teams_sorted_by_baseStats = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Base stats"],reverse=True)
teams_sorted_by_totalstats = sorted(teams_with_attr_averages_calculated,key = lambda team: team["teamAverage_Total Stats"],reverse=True)

def printTeamsAndValuesInSortedTeams(li,n,attribute):
    for team in li[:n]:
        print(team["teamName"],team[f"teamAverage_{attribute}"])


# printTeamsAndValuesInSortedTeams(teams_sorted_by_finishing,30,"Finishing")
# printTeamsAndValuesInSortedTeams(teams_sorted_by_AttackingTotal,30,"Attacking Total")
# printTeamsAndValuesInSortedTeams(teams_sorted_by_BallControl,30,"Ball Control")


# for team in teams_sorted_by_finishing[:12]:
#     print(team["teamName"])

# search for teams with the following combinations 
#fastest players + best dribblers
#fastest players + strongest players 
#fastest players + best dribblers + strongest players
# best short passing + best long passing
# best finishers + best short passing + best long passing + fastest players 
# best finishers + best long passing + best short passing + best dribblers + fastest players 


attacking_team_averages_calculated = []
def assign_attrAverages_attackers():
    attackers = [ "Striker (ST)","Left Wing (LW)","Left Forward (LF)","Center Forward (CF)","Right Forward (RF)","Right Wing (RW)","Center Attacking Midfielder (CAM)","Left Midfielder (LM)","Center Midfielder (CM)","Right Midfielder (RM)"]
    for team in all_teams_list:
        current_team_dictionary = {
        }
        current_team_dictionary["teamName"] = team
        current_team_dictionary["team-players"] = []
        for player in players:
            if player["Team"] == team and player["Best Position"] in attackers:
                current_team_dictionary["team-players"].append(player)

        #calculate all the averages for every attribute in the list
        for attribute in all_attributes:
            team_attr_average = calcAverage_attribute(current_team_dictionary["team-players"],attribute)
            current_team_dictionary[f"teamAverage_{attribute}"] = team_attr_average
        attacking_team_averages_calculated.append(current_team_dictionary)

defending_team_averages_calculated = []
def assign_attrAverages_defenders():
    defenders = ["Left Wing Back (LWB)","Center Defensive Midfielder (CDM)","Right Wing Back (RWB)","Left Back (LB)","Center Back (CB)","Right Back (RB)"]
    for team in all_teams_list:
        current_team_dictionary = {
        }
        current_team_dictionary["teamName"] = team
        current_team_dictionary["team-players"] = []
        for player in players:
            if player["Team"] == team and player["Best Position"] in defenders:
                current_team_dictionary["team-players"].append(player)

        #calculate all the averages for every attribute in the list
        for attribute in all_attributes:
            team_attr_average = calcAverage_attribute(current_team_dictionary["team-players"],attribute)
            current_team_dictionary[f"teamAverage_{attribute}"] = team_attr_average
        defending_team_averages_calculated.append(current_team_dictionary)

# I need to call the functions so they fill the empty lists with somethings
assign_attrAverages_attackers()
assign_attrAverages_defenders()

teams_attackers_sorted_by_SprintSpeed = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Sprint Speed"],reverse=True)
teams_attackers_sorted_by_Acceleration = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Acceleration"],reverse=True)
teams_attackers_sorted_by_Finishing = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Finishing"],reverse=True)
teams_attackers_sorted_by_BallControl = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Ball Control"],reverse=True)
teams_attackers_sorted_by_Dribbling = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Dribbling"],reverse=True)
teams_attackers_sorted_by_shotPower = sorted(attacking_team_averages_calculated,key= lambda team: team["teamAverage_Shot Power"],reverse = True)
teams_attackers_sorted_by_Agility = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Agility"],reverse=True)
teams_attackers_sorted_by_Balance = sorted(attacking_team_averages_calculated,key= lambda team: team["teamAverage_Balance"],reverse=True)
teams_attackers_sorted_by_Composure = sorted(attacking_team_averages_calculated,key= lambda team: team["teamAverage_Composure"],reverse=True)
teams_attackers_sorted_by_Reactions = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Reactions"],reverse=True)
teams_attackers_sorted_by_Vision = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Vision"],reverse=True)
teams_attackers_sorted_by_Crossing = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Crossing"],reverse=True)
teams_attackers_sorted_by_FKAccuracy = sorted(attacking_team_averages_calculated, key = lambda team: team["teamAverage_FreeKick Accuracy"],reverse=True)
teams_attackers_sorted_by_shortPass = sorted(attacking_team_averages_calculated, key = lambda team : team["teamAverage_Short Passing"],reverse=True)
teams_attackers_sorted_by_longPass = sorted(attacking_team_averages_calculated,key=lambda team : team["teamAverage_Long Passing"],reverse=True)
teams_attackers_sorted_by_Curve = sorted(attacking_team_averages_calculated,key = lambda team : team["teamAverage_Curve"],reverse=True)
teams_attackers_sorted_by_Interceptions = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Interceptions"],reverse=True)
teams_attackers_sorted_by_HeadingAccuracy = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Heading Accuracy"],reverse= True)
teams_attackers_sorted_by_DefensiveAwareness = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Marking"],reverse=True)
teams_attackers_sorted_by_StandingTackle = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Standing Tackle"],reverse=True)
teams_attackers_sorted_by_SlidingTackle = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Sliding Tackle"],reverse=True)
teams_attackers_sorted_by_Jumping = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Jumping"],reverse=True)
teams_attackers_sorted_by_Stamina = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Stamina"],reverse=True)
teams_attackers_sorted_by_Strength = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Strength"],reverse=True)
teams_attackers_sorted_by_Aggression = sorted(attacking_team_averages_calculated, key= lambda team: team["teamAverage_Aggression"],reverse=True)
teams_attackers_sorted_by_AttackingPositioning = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Positioning"],reverse=True)
teams_atackers_sorted_by_LongShots = sorted(attacking_team_averages_calculated, key=lambda team: team["teamAverage_Long Shots"],reverse=True)
teams_attackers_sored_by_Volleys = sorted(attacking_team_averages_calculated,key=lambda team: team["teamAverage_Volleys"],reverse=True)
teams_attackers_sorted_by_Penalties = sorted(attacking_team_averages_calculated, key=lambda team: team["teamAverage_Penalties"],reverse=True)




teams_defenders_sorted_by_SprintSpeed = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Sprint Speed"],reverse=True)
teams_defenders_sorted_by_Acceleration = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Acceleration"],reverse=True)
teams_defenders_sorted_by_Finishing = sorted(attacking_team_averages_calculated,key = lambda team: team["teamAverage_Finishing"],reverse=True)
teams_defenders_sorted_by_BallControl = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Ball Control"],reverse=True)
teams_defenders_sorted_by_Dribbling = sorted(defending_team_averages_calculated,key = lambda team: team["teamAverage_Dribbling"],reverse=True)
teams_defenders_sorted_by_shotPower = sorted(defending_team_averages_calculated,key= lambda team: team["teamAverage_Shot Power"],reverse = True)
teams_defenders_sorted_by_Agility = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Agility"],reverse=True)
teams_defenders_sorted_by_Balance = sorted(defending_team_averages_calculated,key= lambda team: team["teamAverage_Balance"],reverse=True)
teams_defenders_sorted_by_Composure = sorted(defending_team_averages_calculated,key= lambda team: team["teamAverage_Composure"],reverse=True)
teams_defenders_sorted_by_Reactions = sorted(defending_team_averages_calculated,key = lambda team: team["teamAverage_Reactions"],reverse=True)
teams_defenders_sorted_by_Vision = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Vision"],reverse=True)
teams_defenders_sorted_by_Crossing = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Crossing"],reverse=True)
teams_defenders_sorted_by_FKAccuracy = sorted(defending_team_averages_calculated, key = lambda team: team["teamAverage_FreeKick Accuracy"],reverse=True)
teams_defenders_sorted_by_shortPass = sorted(defending_team_averages_calculated, key = lambda team : team["teamAverage_Short Passing"],reverse=True)
teams_defenders_sorted_by_longPass = sorted(defending_team_averages_calculated,key=lambda team : team["teamAverage_Long Passing"],reverse=True)
teams_defenders_sorted_by_Curve = sorted(defending_team_averages_calculated,key = lambda team : team["teamAverage_Curve"],reverse=True)
teams_defenders_sorted_by_Interceptions = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Interceptions"],reverse=True)
teams_defenders_sorted_by_HeadingAccuracy = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Heading Accuracy"],reverse= True)
teams_defenders_sorted_by_DefensiveAwareness = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Marking"],reverse=True)
teams_defenders_sorted_by_StandingTackle = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Standing Tackle"],reverse=True)
teams_defenders_sorted_by_SlidingTackle = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Sliding Tackle"],reverse=True)
teams_defenders_sorted_by_Jumping = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Jumping"],reverse=True)
teams_defenders_sorted_by_Stamina = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Stamina"],reverse=True)
teams_defenders_sorted_by_Strength = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Strength"],reverse=True)
teams_defenders_sorted_by_Aggression = sorted(defending_team_averages_calculated, key= lambda team: team["teamAverage_Aggression"],reverse=True)
teams_defenders_sorted_by_AttackingPositioning = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Positioning"],reverse=True)
teamsdefenders_sorted_by_LongShots = sorted(defending_team_averages_calculated, key=lambda team: team["teamAverage_Long Shots"])
teams_defenders_sored_by_Volleys = sorted(defending_team_averages_calculated,key=lambda team: team["teamAverage_Volleys"],reverse=True)
teams_defenders_sorted_by_Penalties = sorted(defending_team_averages_calculated, key=lambda team: team["teamAverage_Penalties"],reverse=True)

# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_SprintSpeed,20,"Sprint Speed")
# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_Acceleration,20, "Acceleration")
# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_Finishing,20,"Finishing")
# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_Dribbling,20,"Dribbling")
# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_shotPower,20,"Shot Power")

# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_Agility,20,"Agility")
# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_Balance,20,"Balance")
# printTeamsAndValuesInSortedTeams(teams_attackers_sorted_by_BallControl,20,"Ball Control")
# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_Acceleration,20,"Acceleration")
# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_Dribbling,20,"Dribbling")
# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_DefensiveAwareness,20,"Marking")
# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_SlidingTackle,20,"Sliding Tackle")
# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_StandingTackle,20,"Standing Tackle")

# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_SprintSpeed,20,"Sprint Speed")

# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_Acceleration,20,"Acceleration")
# printTeamsAndValuesInSortedTeams(teams_sorted_by_DefendingTotal,20,"Defending Total")
# printTeamsAndValuesInSortedTeams(teams_defenders_sorted_by_StandingTackle,20,"Standing Tackle")
# printTeamsAndValuesInSortedTeams(teams_sorted_by_DefendingAverage,20,"Defending Average")

# Later on I have to get teams with the best Center Backs, or Strikers or Wingers. 
# You kinda get my point right. Teams which have the best players at a specific position.