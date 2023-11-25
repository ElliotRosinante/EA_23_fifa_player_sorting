import csv 

#dict reader returns each row as a dictionary

all_players_list = []
with open("playerDetailedStats_main.csv",newline='',encoding="utf-8") as csv_file:
    csv_dictreader = csv.DictReader(csv_file)
    for row in csv_dictreader:
        # print(row)
        all_players_list.append(row)

# These are the functions to find individuals that excel at single attributes 


# function to get players with the highest sprint

def sprinters(li):
    speedy_players = sorted(li,key= lambda dic: int(dic["Sprint Speed"]) if dic["Sprint Speed"]!= "--" else -1,reverse = True)
    names_of_speedy_players = [player["Player Name"] for player in speedy_players]
    names_and_sprint_speed = [(player["Player Name"],player["Sprint Speed"]) for player in speedy_players]

    # let's see the first 30 players with the highest sprint speed in the game
    print(names_of_speedy_players[:31])
    for i in range(31):
        print(names_and_sprint_speed[i][0] + " : " + names_and_sprint_speed[i][1])


def accelerators(li):
    players_with_insane_acceleration = sorted (li, key= lambda dic: int(dic["Acceleration"]) if dic["Acceleration"]!= "--" else -1,reverse = True)
    names_of_players_with_insane_acceleration = [player["Player Name"] for player in players_with_insane_acceleration]
    names_and_acceleration = [(player["Player Name"],player["Acceleration"]) for player in players_with_insane_acceleration]
    
    print(names_of_players_with_insane_acceleration[:31])
    for i in range(31):
        print(names_and_acceleration[i][0] + " : " + names_and_acceleration[i][1])

def ball_controllers(li):
    players_with_insane_ballcontrol = sorted(li,key= lambda dic: int(dic["Ball Control"]) if dic["Ball Control"]!= "--" else -1,reverse = True )
    names_of_players_with_insane_ballcontrol = [player["Player Name"] for player in players_with_insane_ballcontrol]
    names_and_ballcontrol = [(player["Player Name"],player["Ball Control"]) for player in players_with_insane_ballcontrol]

    print(names_of_players_with_insane_ballcontrol[:31])
    for i in range(31):
        print(names_and_ballcontrol[i][0] + " : " + names_and_ballcontrol[i][1])

def reactors(li):
    players_with_insane_reactions = sorted(li,key= lambda dic: int(dic["Reactions"]) if dic["Reactions"]!= "--" else -1,reverse = True )
    names_of_players_with_insane_reactions = [player["Player Name"] for player in players_with_insane_reactions]
    names_and_reactions = [(player["Player Name"],player["Reactions"]) for player in players_with_insane_reactions]

    print(names_of_players_with_insane_reactions[:31])
    for i in range(31):
        print(names_and_reactions[i][0] + " : " + names_and_reactions[i][1])

def balancers(li):
    players_with_insane_balance = sorted(li,key=lambda dic: int(dic["Balance"]) if dic["Balance"]!= "--" else -1, reverse = True)
    names_of_players_with_insane_balance = [player["Player Name"] for player in players_with_insane_balance]
    names_and_balance = [(player["Player Name"],player["Balance"]) for player in players_with_insane_balance]

    print(names_of_players_with_insane_balance[:31])
    for i in range(32):
        print(names_and_balance[i][0] + " : " + names_and_balance[i][1])

def killer_shooters(li):
    players_with_insane_shooting = sorted(li,key=lambda dic: int(dic["Shot Power"]) if dic["Shot Power"]!= "--" else -1,reverse = True)
    names_of_players_with_insane_shooting = [player["Player Name"] for player in players_with_insane_shooting]
    names_and_shooting = [(player["Player Name"],player["Shot Power"]) for player in players_with_insane_shooting]

    print(names_of_players_with_insane_shooting[:31])
    for i in range(32):
        print(names_and_shooting[i][0] + " : " + names_and_shooting[i][1])

# names of people with the best jumping abilities. I call them grasshoppers :) such  a funny name
def grasshoppers(li):
    players_with_insane_jumping = sorted(li, key = lambda dic: int(dic["Jumping"] if dic["Jumping"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_jumping = [player["Player Name"] for player in players_with_insane_jumping]
    names_and_jumping = [(player["Player Name"],player["Jumping"]) for player in players_with_insane_jumping]

    print(names_of_players_with_insane_jumping[:31])
    for i in range(31):
        print(names_and_jumping[i][0] + " : " + names_and_jumping[i][1])

# how to last longer in bed, they have serious stamina,go to them for advise
def stamina_killers(li):
    players_with_insane_stamina = sorted(li, key = lambda dic: int(dic["Stamina"] if dic["Stamina"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_stamina = [player["Player Name"] for player in players_with_insane_stamina]
    names_and_stamina = [(player["Player Name"],player["Stamina"]) for player in players_with_insane_stamina]

    print(names_of_players_with_insane_stamina[:31])
    for i in range(32):
        print(names_and_stamina[i][0] + " : " + names_and_stamina[i][1])

# these guys are really really strong
def strong_players(li):
    players_with_insane_strength = sorted(li, key = lambda dic: int(dic["Strength"] if dic["Strength"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_strength = [player["Player Name"] for player in players_with_insane_strength]
    names_and_strength = [(player["Player Name"],player["Strength"]) for player in players_with_insane_strength]

    print(names_of_players_with_insane_strength[:31])
    for i in range(100):
        print(names_and_strength[i][0] + " : " + names_and_strength[i][1])

# these guys are good at scoring from long range
# when they cum it goes far :) Naugty boy
def long_shooters(li):
    players_with_insane_longShots = sorted(li, key = lambda dic: int(dic["Long Shots"] if dic["Long Shots"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_longShots = [player["Player Name"] for player in players_with_insane_longShots]
    names_and_longShots = [(player["Player Name"],player["Long Shots"]) for player in players_with_insane_longShots]

    print(names_of_players_with_insane_longShots[:31])
    for i in range(32):
        print(names_and_longShots[i][0] + " : " + names_and_longShots[i][1])

# these players are really aggressive
def aggressive_players(li):
    players_with_insane_aggression = sorted(li, key = lambda dic: int(dic["Aggression"] if dic["Aggression"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_aggression = [player["Player Name"] for player in players_with_insane_aggression]
    names_and_aggression = [(player["Player Name"],player["Aggression"]) for player in players_with_insane_aggression]

    print(names_of_players_with_insane_aggression[:31])
    for i in range(32):
        print(names_and_aggression[i][0] + " : " + names_and_aggression[i][1])

# these players are good at interceptions
def interceptors(li):
    players_with_insane_interceptions = sorted(li, key = lambda dic: int(dic["Interceptions"] if dic["Interceptions"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_interceptions = [player["Player Name"] for player in players_with_insane_interceptions]
    names_and_interceptions = [(player["Player Name"],player["Interceptions"]) for player in players_with_insane_interceptions]

    print(names_of_players_with_insane_interceptions[:31])
    for i in range(32):
        print(names_and_interceptions[i][0] + " : " + names_and_interceptions[i][1])

# these players are good at giving long passes
def long_passers(li):
    players_with_insane_longPassing = sorted(li, key = lambda dic: int(dic["Long Passing"] if dic["Long Passing"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_longPassing = [player["Player Name"] for player in players_with_insane_longPassing]
    names_and_longPassing = [(player["Player Name"],player["Long Passing"]) for player in players_with_insane_longPassing]

    print(names_of_players_with_insane_longPassing[:31])
    for i in range(32):
        print(names_and_longPassing[i][0] + " : " + names_and_longPassing[i][1])

# these players are excellent at Freekicks
def freekick_genuises(li):
    players_with_insane_freekickAccuracy = sorted(li, key = lambda dic: int(dic["FreeKick Accuracy"] if dic["FreeKick Accuracy"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_freekickAccuracy = [player["Player Name"] for player in players_with_insane_freekickAccuracy]
    names_and_freekickAccuracy = [(player["Player Name"],player["FreeKick Accuracy"]) for player in players_with_insane_freekickAccuracy]

    print(names_of_players_with_insane_freekickAccuracy[:31])
    for i in range(32):
        print(names_and_freekickAccuracy[i][0] + " : " + names_and_freekickAccuracy[i][1])

# these players are excellent at Curves pls not the curves you are thinking about, Naughty Boy
def curvy_players(li):
    players_with_insane_curves = sorted(li, key = lambda dic: int(dic["Curve"] if dic["Curve"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_curves = [player["Player Name"] for player in players_with_insane_curves]
    names_and_curves = [(player["Player Name"],player["Curve"]) for player in players_with_insane_curves]

    print(names_of_players_with_insane_curves[:31])
    for i in range(32):
        print(names_and_curves[i][0] + " : " + names_and_curves[i][1])

# these players are gods at dribbling 
def dribblers(li):
    players_with_insane_dribbling = sorted(li, key = lambda dic: int(dic["Dribbling"] if dic["Dribbling"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_dribbling = [player["Player Name"] for player in players_with_insane_dribbling]
    names_and_dribbling = [(player["Player Name"],player["Dribbling"]) for player in players_with_insane_dribbling]

    # print(names_of_players_with_insane_dribbling[:31])
    for i in range(30):
        print( str(i+ 1) +  " " + names_and_dribbling[i][0] + " : " + names_and_dribbling[i][1])

# these players are exceptional at volleys
def volleyball_players(li):
    players_with_insane_volleys= sorted(li, key = lambda dic: int(dic["Volleys"] if dic["Volleys"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_volleys = [player["Player Name"] for player in players_with_insane_volleys]
    names_and_volleys = [(player["Player Name"],player["Volleys"]) for player in players_with_insane_volleys]

    print(names_of_players_with_insane_volleys[:31])
    for i in range(32):
        print(names_and_volleys[i][0] + " : " + names_and_volleys[i][1])

# these players are exceptional at short passing
def short_pass_genuises(li):
    players_with_insane_shotPassing = sorted(li, key = lambda dic: int(dic["Short Passing"] if dic["Short Passing"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_shotPassing= [player["Player Name"] for player in players_with_insane_shotPassing]
    names_and_shotPassing = [(player["Player Name"],player["Short Passing"]) for player in players_with_insane_shotPassing]

    print(names_of_players_with_insane_shotPassing[:31])
    for i in range(32):
        print(names_and_shotPassing[i][0] + " : " + names_and_shotPassing[i][1])

# these players are headers. they are amazing at giving head :) Naughty boy
def excellent_headers(li):
    players_with_insane_headers = sorted(li, key = lambda dic: int(dic["Heading Accuracy"] if dic["Heading Accuracy"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_headers = [player["Player Name"] for player in players_with_insane_headers]
    names_and_headers = [(player["Player Name"],player["Heading Accuracy"]) for player in players_with_insane_headers]

    print(names_of_players_with_insane_headers[:31])
    for i in range(32):
        print( str(i+1 ) + " " + names_and_headers[i][0] + " : " + names_and_headers[i][1])

#These players are good at anihilating the nets and finishing the goalkeepers
def finishers(li):
    players_with_insane_finishing= sorted(li, key = lambda dic: int(dic["Finishing"] if dic["Finishing"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_finishing = [player["Player Name"] for player in players_with_insane_finishing]
    names_and_finishing = [(player["Player Name"],player["Finishing"]) for player in players_with_insane_finishing]

    print(names_of_players_with_insane_finishing[:31])
    for i in range(30):
        print( str(i+1 ) + " " + names_and_finishing[i][0] + " : " + names_and_finishing[i][1])

# These players are good at crossing
def crossers(li):
    players_with_insane_crossing = sorted(li, key = lambda dic: int(dic["Crossing"] if dic["Crossing"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_crossing = [player["Player Name"] for player in players_with_insane_crossing]
    names_and_crossing = [(player["Player Name"],player["Crossing"]) for player in players_with_insane_crossing]

    print(names_of_players_with_insane_crossing[:31])
    for i in range(32):
        print(names_and_crossing[i][0] + " : " + names_and_crossing[i][1])

# These players are highly agile

def agile_players(li):
    players_with_insane_agility = sorted(li, key = lambda dic: int(dic["Agility"] if dic["Agility"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_agility = [player["Player Name"] for player in players_with_insane_agility]
    names_and_agility = [(player["Player Name"],player["Agility"]) for player in players_with_insane_agility]

    print(names_of_players_with_insane_agility[:31])
    for i in range(32):
        print(names_and_agility[i][0] + " : " + names_and_agility[i][1])

# These players are are eagles. They have excellent Vision

def visionary_players(li):
    players_with_insane_vision = sorted(li, key = lambda dic: int(dic["Vision"] if dic["Vision"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_vision = [player["Player Name"] for player in players_with_insane_vision]
    names_and_vision = [(player["Player Name"],player["Vision"]) for player in players_with_insane_vision]

    print(names_of_players_with_insane_vision[:31])
    for i in range(32):
        print(names_and_vision[i][0] + " : " + names_and_vision[i][1])

# These players are excellent at scoring penalties
def penalty_genuises(li):
    players_with_insane_penalties = sorted(li, key = lambda dic: int(dic["Penalties"] if dic["Penalties"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_penalties = [player["Player Name"] for player in players_with_insane_penalties]
    names_and_penalties = [(player["Player Name"],player["Penalties"]) for player in players_with_insane_penalties]

    print(names_of_players_with_insane_penalties[:31])
    for i in range(32):
        print(names_and_penalties[i][0] + " : " + names_and_penalties[i][1])

# These players are excellent at positioning themselves
def position_gurus(li):
    players_with_insane_positioning = sorted(li, key = lambda dic: int(dic["Positioning"] if dic["Positioning"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_positioning = [player["Player Name"] for player in players_with_insane_positioning]
    names_and_positioning = [(player["Player Name"],player["Positioning"]) for player in players_with_insane_positioning]

    print(names_of_players_with_insane_positioning[:31])
    for i in range(100):
        print(names_and_positioning[i][0] + " : " + names_and_positioning[i][1])

# These players always have a calm and composed behaviour
def composed_players(li):
    players_with_insane_composure = sorted(li, key = lambda dic: int(dic["Composure"] if dic["Composure"]!= "--" else -1),reverse = True)
    names_of_players_with_insane_composure = [player["Player Name"] for player in players_with_insane_composure]
    names_and_composure = [(player["Player Name"],player["Composure"]) for player in players_with_insane_composure ]

    print(names_of_players_with_insane_composure[:31])
    for i in range(32):
        print(names_and_composure[i][0] + " : " + names_and_composure[i][1])

# 29th March update.
# skills I am left with to code up 
# Get the best Goolkeeping attributes
# Get the best sliding and standing tackle attributes 

# create the function, it's first parameter will be the attribute ,and it's second parameter will be n
# n represents the first n players excellent at that attribute. 
# we will use the all_players_list within the function since it is a global variable 

# the attribute should be a string 
# n should be an integer

def get_first_n_players(attribute, n):
    excellent_players_at_specificAttr = sorted(all_players_list,key = lambda player : int(player[attribute]) if player[attribute] != "--" else -1,reverse=True)
    names_of_excellent_players = [player["Player Name"] for player in excellent_players_at_specificAttr]

    #getting the first n players at specific attributes
    for i in range(n+1):
        print(excellent_players_at_specificAttr[i]["Player Name"] + " : " + excellent_players_at_specificAttr[i][attribute])


#Marking,Standing Tackle,Sliding Tackle,GK Diving,GK Handling,GK Kicking,GK Positioning,GK Reflexes,
# Striker (ST),Left Wing (LW),Left Forward (LF),Center Forward (CF),
# Right Forward (RF),Right Wing (RW),Center Attacking Midfielder (CAM),Left Midfielder (LM),
# Center Midfielder (CM),Right Midfielder (RM),Left Wing Back (LWB),Center Defensive Midfielder (CDM),
# Right Wing Back (RWB),Left Back (LB),Center Back (CB),Right Back (RB),
# Goalkeeper (GK),Attacking Average,Attacking Total,Skill Average,Skill Total,Movement Average,Movement Total,Power Average,Power Total,Mentality Average,Mentality Total,Defending Average,Defending Total,Goalkeeping Average,Goalkeeping Total,Base stats,Total Stats

# get_first_n_players("Marking", 30)
# get_first_n_players("Standing Tackle",40)
# get_first_n_players("Sliding Tackle", 40)
# get_first_n_players("GK Diving",30)
# get_first_n_players("GK Handling",12)
# get_first_n_players("GK Kicking",12)
# get_first_n_players("GK Positioning",12)
# get_first_n_players("GK Reflexes",30)
# get_first_n_players("Striker (ST)",12)
# get_first_n_players("Left Wing (LW)",12)
# get_first_n_players("Left Forward (LF)",12)
# get_first_n_players("Center Forward (CF)",12)
# get_first_n_players("Right Forward (RF)",12)
# get_first_n_players("Right Wing (RW)",12)
# get_first_n_players("Center Attacking Midfielder (CAM)",12)
# get_first_n_players("Left Midfielder (LM)",12)
# get_first_n_players("Center Midfielder (CM)",12)
# get_first_n_players("Right Midfielder (RM)",12)
# get_first_n_players("Center Forward (CF)",12)
# get_first_n_players("Left Wing Back (LWB)",12)
# get_first_n_players("Center Defensive Midfielder (CDM)",12)
# get_first_n_players("Right Wing Back (RWB)",12)
# get_first_n_players("Left Back (LB)",12)
# get_first_n_players("Right Back (RB)",12)
# get_first_n_players("Center Back (CB)",12)
# get_first_n_players("Goalkeeper (GK)",12)



# Combine the attributes 
# I will do that one some other time

# Best Foot,Weak Foot,Skill moves
#get players who are 5 star weak foot and 5 star skill moves

def ambidextrousPlayers(n):
    fiveStarPlayers = []
    for player in all_players_list:
        if player["Weak Foot"] == "5":
            fiveStarPlayers.append(player)

    for player in fiveStarPlayers[:n+1]:
        print(player["Player Name"])

def five_star_skillers(n):
    fiveStarSkillers = []
    for player in all_players_list:
        if player["Skill moves"] == "5":
            fiveStarSkillers.append(player)

    for player in fiveStarSkillers[:n+1]:
        print(player["Player Name"])

def skillers_and_ambidextrous(n):
    excellent_dribblers = []
    for player in all_players_list:
        if player["Skill moves"] == "5" and player["Weak Foot"] == "5":
            excellent_dribblers.append(player)

    for player in excellent_dribblers[:n+1]:
        print(player["Player Name"] + " " + player["Team"])


# ambidextrousPlayers(20)
# five_star_skillers(20)

# There are only 6 players with this ability
# skillers_and_ambidextrous(10)
#get players who are 5 star weak foot and have shot power above 80

def scorers_from_multipleAngles(n):
    killers = []
    for player in all_players_list:
        try:
            if int(player["Finishing"]) > 90 and player["Weak Foot"] == "5":
                killers.append(player)
        except ValueError:
            pass

    for player in killers[:n+1]:
        print(player["Player Name"])

def fastest_defenders():
    fastest_defenders = []
    defenders_positions = ["Left Wing Back (LWB)","Right Back (RB)","Right Wing Back (RWB)","Left Back (LB)","Center Back (CB)"]
    speedy_players = sorted(all_players_list,key= lambda dic: int(dic["Sprint Speed"]) if dic["Sprint Speed"]!= "--" else -1,reverse = True)
    for player in speedy_players:
        try:
            if int(player["Acceleration"]) > 80 and int(player["Sprint Speed"]) > 80 and player["Best Position"] in defenders_positions:
                fastest_defenders.append(player)
        except ValueError:
            pass

    for player in fastest_defenders[:50]:
        print(player["Player Name"] + " Position : " + player["Best Position"] + " Acceleration : " + player["Acceleration"] + " Sprint Speed : " + player["Sprint Speed"])

fastest_defenders()
def find_davies():
    for player in all_players_list:
        if "Alphonso" in player["Player Name"]: 
            pace = (int(player["Acceleration"]) + int(player["Sprint Speed"]))/2
            print(pace)
            print(player["Player Name"])
            print(player["Team"])
            print(player["Nationality"])
            print(player["Best Position"])
            print(player["Sprint Speed"])
            print(player["Acceleration"])

# find_davies()
#get players who are 5 star weak foot and have finishing above 80
#get players who are 5 star weak foot and have long shot above 80

# scorers_from_multipleAngles(10)

# Neymar da Silva Santos Jr.
# Ousmane Dembélé
# Jesús Corona
# Rayan Cherki
# Franck Ribéry
# Cesar Fernando Silva Melo
# Harry Kane   
# Heung Min Son
print("******")

def find_jesus_corona_team():
    for player in all_players_list:
        if player["Player Name"] == "Jesús Corona" :
            print(player["Team"],player["League"])

def findEndo():
        for player in all_players_list:
            if player["Player Name"] == "Wataru Endo" :
                # print(player["Team"],player["League"])
                for key,val in player.items():
                    print(f"{key} : {val}")
                

# findEndo()
# find_jesus_corona_team()

# Sevilla FC Spain Primera Division

# def position_gurus(li):
#     players_with_insane_positioning = sorted(li, key = lambda dic: int(dic["Positioning"] if dic["Positioning"]!= "--" else -1),reverse = True)
#     names_of_players_with_insane_positioning = [player["Player Name"] for player in players_with_insane_positioning]
#     names_and_positioning = [(player["Player Name"],player["Strength"]) for player in ]players_with_insane_positioning

#     print(names_of_players_with_insane_positioning[:31])
#     for i in range(32):
#         print(names_and_positioning[i][0] + " : " + names_and_positioning[i][1])

# finishers(all_players_list)
# sprinters(all_players_list)
# accelerators(all_players_list)
# print("****")
# ball_controllers(all_players_list)
# reactors(all_players_list)
# balancers(all_players_list)
# killer_shooters(all_players_list)
# grasshoppers(all_players_list)
# stamina_killers(all_players_list)
# strong_players(all_players_list)
# penalty_genuises(all_players_list)
# position_gurus(all_players_list)
# visionary_players(all_players_list)

# I am very sure people with excellent vision are really good at giving passes
# composed_players(all_players_list)
# agile_players(all_players_list)
# crossers(all_players_list)
# excellent_headers(all_players_list)
# short_pass_genuises(all_players_list)
# volleyball_players(all_players_list)
dribblers(all_players_list)
# curvy_players(all_players_list)
# freekick_genuises(all_players_list)
# long_passers(all_players_list)
# interceptors(all_players_list)
# aggressive_players(all_players_list)
# long_shooters(all_players_list)


