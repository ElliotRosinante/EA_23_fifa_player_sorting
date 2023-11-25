
# Step1: I need to get the list of all the teams.

import csv

all_teams_list = []
with open("team_attributes.csv",newline="",encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        all_teams_list.append(row["TeamName"])

# okay so now we have gotten the list of the teams. 
# for team in all_teams_list[:7]:
#     print(team)

# Manchester City
# Real Madrid CF     
# FC Bayern München  
# Paris Saint-Germain
# Liverpool
# FC Barcelona       
# Inter


# Step 2 : I need to get all the players in the whole game and append them to a list. 

players = []
with open("playerDetailedStats_main.csv",newline = '',encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        players.append(row)
        # returns a dictionary
        

# Step 3 : what I am going to do is that, I am going to use the list of the teams as the outer loop
# and use the list of the players as the inner loop. 
# The code that I am going to write in the inner loop is to check if the current player of that iteration 
# has the same team as the current team in the outer loop's iteration, what I am going to do is that 
# I am going to append the player(i.e. the whole dictionary) to a list and append it to a dictionary which 
# I will create for every team in the game so I can get all the players in a specific team and do things with them.


# Step 4 : After  I calculate the average for a specific attribute and assign it to the team, I append the team I am 
# done with to this list 

teams_with_attr_averages_calculated = []
def calcAverage_attribute(li,attribute):
        # if the player has an actual attribute and the attribute is not equal to "--"
        # append it to a list of player's who have that attribute
    players_who_have_value_for_target_attribute = [player for player in li if player[attribute] and player[attribute]!= "--"]
    team_totale_attr = 0
    len_players_with_attributes = len(players_who_have_value_for_target_attribute)
    for player in players_who_have_value_for_target_attribute:
        team_totale_attr += int(player[attribute])

    average_val_for_attr = team_totale_attr/len_players_with_attributes
    return average_val_for_attr


def sortTeams_by_attributes(attribute,n):
    for team in all_teams_list[:n]:
        current_team_dictionary = {
        }
        current_team_dictionary["teamName"] = team
        current_team_dictionary["team-players"] = []
        for player in players:
            if player["Team"] == team:
                current_team_dictionary["team-players"].append(player)
        # after we have appended all the players in one team, what we want to do is to calculate the average 
        # for a specific attribute or multiple attributes . 
        # for now lemme just find the average for a single attribute and then I will try for multiple attributes later on
        team_attr_average = calcAverage_attribute(current_team_dictionary["team-players"],attribute)

        # after we have calculated the average, we assign it to a key and place it into the current_team_dictionary
        # and then we append it to a new list which we have defined at the top
        current_team_dictionary[f"teamAverage_{attribute}"] = team_attr_average
        teams_with_attr_averages_calculated.append(current_team_dictionary)

def getAveragesForSprintersInEachTeam():
    sortTeams_by_attributes("Sprint Speed",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Sprint Speed"])

def getAveragesForDribblersInEachTeam():
    sortTeams_by_attributes("Dribbling",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Dribbling"])

def getAveragesForFinishersInEachTeam():
    sortTeams_by_attributes("Finishing",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Finishing"])
def getAveragesForshortPassersInEachTeam():
    sortTeams_by_attributes("Short Passing",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_short Passing"])
def getAveragesForlongPassersInEachTeam():
    sortTeams_by_attributes("Long Passing",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_long Passing"])
def getAveragesForAccelerationInEachTeam():
    sortTeams_by_attributes("Acceleration",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Acceleration"])
def getAveragesForAgilityInEachTeam():
    sortTeams_by_attributes("Agility",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Agility"])
def getAveragesForStrengthInEachTeam():
    sortTeams_by_attributes("Strength",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Strength"])
def getAveragesForVisionInEachTeam():
    sortTeams_by_attributes("Vision",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Vision"])

def getAveragesForPositioningInEachTeam():
    sortTeams_by_attributes("Positioning",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Positioning"])

def getAveragesForAggressionInEachTeam():
    sortTeams_by_attributes("Aggression",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Aggression"])

def getAveragesForInterceptionsInEachTeam():
    sortTeams_by_attributes("Interceptions",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Interceptions"])

def getAveragesForComposureInEachTeam():
    sortTeams_by_attributes("Composure",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Composure"])

def getAveragesForReactionsInEachTeam():
    sortTeams_by_attributes("Reactions",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Reactions"])

def getAveragesForLongShotsInEachTeam():
    sortTeams_by_attributes("Long Shots",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Long Shots"])
def getAveragesForDribblesInEachTeam():
    sortTeams_by_attributes("Shot Power",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Shot Power"])

def getAveragesForAttackingTotalInEachTeam():
    sortTeams_by_attributes("Attacking Total",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Attacking Total"])

def getAveragesForDefendingTotalInEachTeam():
    sortTeams_by_attributes("Defending Total",12)
    for dic in teams_with_attr_averages_calculated:
        print(dic["teamName"],dic["teamAverage_Defending Total"])


# getAveragesForDribblersInEachTeam()
getAveragesForSprintersInEachTeam()
# getAveragesForAttackingTotalInEachTeam()
# getAveragesForDefendingTotalInEachTeam()




        