import csv
import time
import random


teams = []
players = []
all_teams_list = []
all_countries_list  = []
teams_belonging_to_same_league = []
all_countries_list_of_dictionaries_with_players_appended = []
all_leagues_list = []
all_leagues_list_of_dictionaries_with_players_appended = []
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

# this list contains all the teams as dictionaries that have the team names and the team players as values
team_players_grouped = []
def read_specified_csv(filename):
    with open(filename,mode= "r",encoding="utf-8") as csv_file:
        csv_file = csv.DictReader(csv_file)
        for team in csv_file:
            teams.append(team)

read_specified_csv("team_attributes.csv")
# print(teams[:10])
# get the list of all the players
with open("playerDetailedStats_main.csv",newline = '',encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        players.append(row)

with open("team_attributes.csv",newline="",encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        all_teams_list.append(row["TeamName"])

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


# print(team_players_grouped[:2])
# I printed to check if the order in which the teams where grouped is in the order of the most excellent teams


# teams sorted by defense
team_defense = sorted(teams,key=lambda team: int(team["Defense"]),reverse=True)
# teams sorted by attack 
team_attack = sorted(teams,key=lambda team: int(team["Attack"]),reverse=True)
# teams sorted by overrall
team_overall = sorted(teams,key=lambda team: int(team["Overall"]),reverse=True)
# teams sorted by midfield
team_midfield = sorted(teams,key=lambda team: int(team["Midfield"]),reverse=True)


def print_from_sorted_teams(li,attr):
    for i in range(10):
        print(li[i].get("TeamName") + " " + attr  + ": " + li[i].get(attr)) 

#print the top 10 teams with the best defense in the game 
# print_from_sorted_teams(team_defense,"Defense")
# print_from_sorted_teams(team_attack,"Attack")
# print_from_sorted_teams(team_midfield,"Midfield")
# print_from_sorted_teams(team_overall,"Overall")

# The next goal of mine is to get the player who has the best stat for a specific attribute in the whole team. 
# plan loop through each team as the outer loop and loop through each attribute as the inner loop.
# sort the players who have the highest of those attributes 
# pause for some seconds after the first team has already been accessed 
def get_players_excellent_at_specificAttr(attribute, li):
    excellent_players_at_specificAttr = sorted(li,key = lambda player : int(player[attribute]) if player[attribute] != "--" else -1,reverse=True)
    return excellent_players_at_specificAttr

def get_best_player_at_specific_attribute():
    for team in team_players_grouped:
        for attribute in all_attributes:
            top_players = get_players_excellent_at_specificAttr(attribute,team["team-players"])
            top_two_players = top_players[:2]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")
                time.sleep(1)

                print("\n")
                print("\n")
        time.sleep(2)

# this function goes through all the teams, every one of them  and prints the "n" players who are the best at those attributes
def get_best_player_at_specific_attribute_n(n):
    for team in team_players_grouped[:n+1]:
        for attribute in all_attributes:
            top_players = get_players_excellent_at_specificAttr(attribute,team["team-players"])
            top_two_players = top_players[:2]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")
                time.sleep(1)

                print("\n")
                print("\n")
        time.sleep(2)


# get_best_player_at_specific_attribute()
# get_best_player_at_specific_attribute_n(2)

# for this function you give it a team and an attribute and it prints a hardcoded the 5 best players at that specific 
# attribute in that team

def best_team_player_at_specific_attribute(attribute, team):
    for named_team in team_players_grouped:
        # I should use this line instead of the one below. if team == named_team["team-name"]  so that the string comparison
        # is strict to improve the accuracy
        if team == named_team["team-name"]:
            top_players = get_players_excellent_at_specificAttr(attribute,named_team["team-players"])
            top_two_players = top_players[:5]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")


# best_team_player_at_specific_attribute("Finishing","Manchester City")
# best_team_player_at_specific_attribute("Finishing","Napoli")
# best_team_player_at_specific_attribute("Dribbling","Napoli")
# best_team_player_at_specific_attribute("Finishing","Arsenal")
# best_team_player_at_specific_attribute("Ball Control","Real Madrid CF")
# best_team_player_at_specific_attribute("Dribbling","Real Madrid CF")

# best_team_player_at_specific_attribute("Dribbling","Liverpool")
# best_team_player_at_specific_attribute("Ball Control","Liverpool")
# best_team_player_at_specific_attribute("Sprint Speed","Liverpool")
# best_team_player_at_specific_attribute("Acceleration","Liverpool")


# best_team_player_at_specific_attribute("Dribbling","Manchester City")
# best_team_player_at_specific_attribute("Dribbling","Atlético de Madrid")
# best_team_player_at_specific_attribute("Ball Control","Inter")
# best_team_player_at_specific_attribute("Finishing","Barcelona")
# best_team_player_at_specific_attribute("Dribbling","Napoli")
# best_team_player_at_specific_attribute("Acceleration","Barcelona")
# best_team_player_at_specific_attribute("Acceleration","Real Madrid CF")
# best_team_player_at_specific_attribute("Sprint Speed","Manchester City")
# best_team_player_at_specific_attribute("Acceleration","Liverpool")
# best_team_player_at_specific_attribute("Ball Control","Atlético de Madrid")
# best_team_player_at_specific_attribute("Ball Control","Bayer 04 Leverkusen")
# best_team_player_at_specific_attribute("Dribbling","Bayer 04 Leverkusen")
# best_team_player_at_specific_attribute("Agility","Bayer 04 Leverkusen")
# best_team_player_at_specific_attribute("Finishing","Bayer 04 Leverkusen")
# best_team_player_at_specific_attribute("Dribbling","Inter")
# best_team_player_at_specific_attribute("Ball Control","Inter")
# best_team_player_at_specific_attribute("Ball Control","Real Madrid CF")
# best_team_player_at_specific_attribute("Dribbling","Real Madrid CF")
# best_team_player_at_specific_attribute("Balance","Real Madrid CF")
# best_team_player_at_specific_attribute("Agility","Real Madrid CF")
# best_team_player_at_specific_attribute("Finishing","Real Madrid CF")
# best_team_player_at_specific_attribute("Shot Power","Real Madrid CF")
# best_team_player_at_specific_attribute("Volleys","Real Madrid CF")



# GETTING THE HIGHEST RATED PLAYER FOR A SPECIFIC ATTRIBUTE FROM A SPECIFIC COUNTRY. 
# I just need the list of players and I need to get all the countries from that list
#  and put them in a list of which I will create dictionaries from and then I will just append players
# who come from that country. 


def group_players_by_nationality():
    for player in players:
        if player["Nationality"] not in all_countries_list:
            all_countries_list.append(player["Nationality"])

    for country in all_countries_list:
        countries_dictionary = {}
        countries_dictionary["country-name"] = country
        countries_dictionary["players"] = []
        for player in players:
            if player["Nationality"] == countries_dictionary["country-name"]:
                countries_dictionary["players"].append(player)
        all_countries_list_of_dictionaries_with_players_appended.append(countries_dictionary)

    return all_countries_list_of_dictionaries_with_players_appended

national_teams_filled = group_players_by_nationality()

def group_players_by_leagues():
    for player in players:
        if player["League"] not in all_leagues_list:
            all_leagues_list.append(player["League"])

    for league in all_leagues_list:
        leagues_dictionary = {}
        leagues_dictionary["league-name"] = league
        leagues_dictionary["players"] = []
        for player in players:
            if player["League"] == leagues_dictionary["league-name"]:
                leagues_dictionary["players"].append(player)

        all_leagues_list_of_dictionaries_with_players_appended.append(leagues_dictionary)

    return all_leagues_list_of_dictionaries_with_players_appended

league_teams_filled = group_players_by_leagues()

def get_best_player_at_specific_attribute_countriesVer():
    for team in all_countries_list_of_dictionaries_with_players_appended:
        for attribute in all_attributes:
            top_players = get_players_excellent_at_specificAttr(attribute,team["team-players"])
            top_two_players = top_players[:2]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")
                time.sleep(1)

                print("\n")
                print("\n")
        time.sleep(2)

def get_best_player_at_specific_attribute_leaguesVer():
    for team in all_leagues_list_of_dictionaries_with_players_appended:
        for attribute in all_attributes:
            top_players = get_players_excellent_at_specificAttr(attribute,team["team-players"])
            top_two_players = top_players[:2]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")
                time.sleep(1)

                print("\n")
                print("\n")
        time.sleep(2)

def best_team_player_at_specific_attribute_countriesVer(attribute, team):
    for named_team in all_countries_list_of_dictionaries_with_players_appended:
        if team in named_team["country-name"]:
            top_players = get_players_excellent_at_specificAttr(attribute,named_team["players"])
            top_two_players = top_players[:10]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")

def best_team_player_at_specific_attribute_leaguesVer(attribute, team):
    for named_team in all_leagues_list_of_dictionaries_with_players_appended:
        if team in named_team["league-name"]:
            top_players = get_players_excellent_at_specificAttr(attribute,named_team["players"])
            top_two_players = top_players[:10]

            for player in top_two_players:
                print(f"{player['Player Name']}   |  {attribute} : {player[attribute]}")

# in the following functions, best_team_player_at_specific_attribute_countriesVer and best_team_player_at_specific_attribute_leaguesVer,
# you don't really need to write these lines of code  if team in named_team["country-name"] and if team in named_team["league-name"],
# you can just do it for team in named_team and everything will work all right. 

# best_team_player_at_specific_attribute_countriesVer("Dribbling","Brazil")
# best_team_player_at_specific_attribute_countriesVer("Dribbling","Ghana")
# best_team_player_at_specific_attribute_countriesVer("Dribbling","Nigeria")
# best_team_player_at_specific_attribute_countriesVer("Dribbling","Portugal")
# best_team_player_at_specific_attribute_countriesVer("Finishing","Nigeria")
# best_team_player_at_specific_attribute_leaguesVer("Ball Control","Spain Primera Division")
# best_team_player_at_specific_attribute_leaguesVer("Dribbling","Spain Primera Division")
# best_team_player_at_specific_attribute_leaguesVer("Dribbling","English Premier League")
# best_team_player_at_specific_attribute_countriesVer("Finishing","Ghana")
# best_team_player_at_specific_attribute_countriesVer("Finishing","Japan")
# best_team_player_at_specific_attribute_countriesVer("Dribbling","Japan")
# best_team_player_at_specific_attribute_countriesVer("Agility","Nigeria")
# best_team_player_at_specific_attribute_countriesVer("Ball Control","Nigeria")
# best_team_player_at_specific_attribute_countriesVer("Balance","Nigeria")


# let's generate random match fixtures between teams 
def generate_random_match_fixture_teams():
    first_team_index = 0
    second_team_index = 0
    # done to prevent the function from generating a team against itself. we want to mimic real life as much as possible
    while first_team_index == second_team_index:
        first_team_index = random.randint(0,len(all_teams_list)-1)
        second_team_index = random.randint(0,len(all_teams_list)-1)
    team_1 = all_teams_list[first_team_index]
    team_2 = all_teams_list[second_team_index]
    return  f"\n{team_1}  vs {team_2} "

# versus_match = generate_random_match_fixture_teams()
# print(versus_match)

def generate_random_match_fixture_countries():
    first_team_index = 0
    second_team_index = 0
    # done to prevent the function from generating a team against itself. we want to mimic real life as much as possible
    while first_team_index == second_team_index:
        first_team_index = random.randint(0,len(all_countries_list)-1)
        second_team_index = random.randint(0,len(all_countries_list)-1)
    team_1 = all_countries_list[first_team_index]
    team_2 = all_countries_list[second_team_index]
    return  f"\n{team_1}  vs {team_2} "

# versus_match_1 = generate_random_match_fixture_countries()
# print(versus_match_1)

# function to generate random matches within the same league
def group_teams_belonging_to_same_league():
    for league in all_leagues_list:
        curr_dictionary = {
            "league-name" : league,
            "teams" : []
        }
        for team in teams:
            if team.get("LeagueName") == league:
                curr_dictionary["teams"].append(team)

        #after we are done finding all the teams in one league, we save the data somewhere by appending it to another list
        # and then we move on to the next iteration 
        teams_belonging_to_same_league.append(curr_dictionary)

    # print(teams_belonging_to_same_league[0])

#call the function so that we can do things with it 
group_teams_belonging_to_same_league()

#question, which league do you want the fixtures from? 
# I can make the league a random league everytime.
def generate_random_match_fixture_same_league():
    random_league_index = random.randint(0,len(all_leagues_list)-1)
    league_name = all_leagues_list[random_league_index]
    for league in teams_belonging_to_same_league:
        if league["league-name"] == league_name:
            league_to_use = league
            # we don't want the loop to continue even after we find what we are looking for
            break 
    
    first_team_index = 0
    second_team_index = 0
    # done to prevent the function from generating a team against itself. we want to mimic real life as much as possible
    while first_team_index == second_team_index:
        first_team_index = random.randint(0,len(league_to_use["teams"])-1)
        second_team_index = random.randint(0,len(league_to_use["teams"])-1)
    team_1 = league_to_use["teams"][first_team_index].get("TeamName")
    team_2 = league_to_use["teams"][second_team_index].get("TeamName")
    return  f"\n{team_1}  vs {team_2} "

# versus_match_same_league = generate_random_match_fixture_same_league()
# print(versus_match_same_league)

#This time you are the one who provides the league name you want the fixture generated from
# since it uses strict matching for comparison, you have to be correct everytime. (please no typos)
def generate_random_match_fixture_same_league_you_specify(league_name):
    # random_league_index = random.randint(0,len(all_leagues_list)-1)
    # league_name = all_leagues_list[random_league_index]
    for league in teams_belonging_to_same_league:
        if league["league-name"] == league_name:
            league_to_use = league
            # we don't want the loop to continue even after we find what we are looking for
            break 
    
    first_team_index = 0
    second_team_index = 0
    # done to prevent the function from generating a team against itself. we want to mimic real life as much as possible
    while first_team_index == second_team_index:
        first_team_index = random.randint(0,len(league_to_use["teams"])-1)
        second_team_index = random.randint(0,len(league_to_use["teams"])-1)
    team_1 = league_to_use["teams"][first_team_index].get("TeamName")
    team_2 = league_to_use["teams"][second_team_index].get("TeamName")
    return  f"\n{team_1}  vs {team_2} "

# premier_league_random_match = generate_random_match_fixture_same_league_you_specify('English Premier League')
# print(premier_league_random_match)
# Southampton  vs AFC Bournemouth
# Crystal Palace  vs AFC Bournemouth
# Southampton  vs Everton
