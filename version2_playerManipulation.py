import csv
import random

# this list store all the players we got from the csv file
players = []
with open("playerDetailedStats_main.csv",newline = '',encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        players.append(row)
        # returns a dictionary
        

# we want to be able to combine attributes

# for example let's say we want to sort all players and make those with pace + finishing + long shot 
# by pace I mean sprint speed + acceleration 



def get_killer_attributes():
    killer_attributes = ["Sprint Speed","Acceleration","Long Shots","Finishing"]
    for player in players:
        sum_attributes = 0
        for attribute in killer_attributes:
            try:
                sum_attributes += int(player[attribute])
                # i.e we want to add player["Sprint Speed"] + player["Acceleration"] + player["Long Shot"] + player["Finishing"]
                # combined is the variable that stores the combined attributes sum
                player["CombinedFastFinisher"] = sum_attributes

            except ValueError:
                pass
    # so now after we are done reading all our players, we sort them by the sum of their combined values
    killers = sorted(players,key=lambda player: player["CombinedFastFinisher"],reverse=True)
    return killers

def printKillerStrikers(n):
    killers = get_killer_attributes()
    for killer in killers[:n]:
        name = killer["Player Name"]
        acc = killer["Acceleration"]
        speed = killer["Sprint Speed"]
        long_shots = killer["Long Shots"]
        finishing = killer["Finishing"]
        combinedFastFinisher = killer["CombinedFastFinisher"]
        print(f"{name}  Acceleration : {acc}    Sprint Speed : {speed}  Long Shot: {long_shots}  finishing : {finishing} CombinedFastFinisher : {combinedFastFinisher}")

# printKillerStrikers(10)

# for the extreme killer attributes, I am adding shot power and strength
def get_Extreme_Killer_Attributes():
    killer_attributes = ["Sprint Speed","Acceleration","Long Shots","Finishing","Shot Power","Strength"]
    for player in players:
        sum_attributes = 0
        for attribute in killer_attributes:
            try:
                sum_attributes += int(player[attribute])
                # i.e we want to add player["Sprint Speed"] + player["Acceleration"] + player["Long Shot"] + player["Finishing"]
                # combined is the variable that stores the combined attributes sum
                player["CombinedStrongFastFinisher"] = sum_attributes

            except ValueError:
                pass
    # so now after we are done reading all our players, we sort them by the sum of their combined values
    ultimate_killers = sorted(players,key=lambda player: player["CombinedStrongFastFinisher"],reverse=True)
    return ultimate_killers


#attributes to locate people I will call true dribblers.
# they have these attributes Agility,Balance,Ball Control,Dribbling
def get_Print_True_Dribblers(n):
    attributes = ["Agility","Balance","Ball Control","Dribbling"]
    for player in players:
        sum_attributes = 0
        for attribute in attributes:
            try:
                sum_attributes += int(player[attribute])
            except ValueError:
                pass
        player["CombinedVal_trueDribbling"] = sum_attributes

    # so now after we are done reading all of our players we sort them by the sum of their combined values
    ultimate_dribblers = sorted(players,key=lambda player:player["CombinedVal_trueDribbling"],reverse = True)
    for player in ultimate_dribblers[:n+1]:
        agility = player["Agility"]
        balance = player["Balance"]
        ballControl = player["Ball Control"]
        dribbling = player["Dribbling"]
        print(player.get("Player Name"),"  Combined_dribbling_attributes :",player.get("CombinedVal_trueDribbling") )
        print(f"      agility : {agility}  balance : {balance}  ballControl : {ballControl} dribbling : {dribbling}")

# "Ball Control","Dribbling"
# get_Print_True_Dribblers(30)

def get_Print_fluid_movers(n):
    attributes = ["Agility","Balance"]
    for player in players:
        sum_attributes = 0
        for attribute in attributes:
            try:
                sum_attributes += int(player[attribute])
            except ValueError:
                pass
        player["CombinedVal_truefluidity"] = sum_attributes

    # so now after we are done reading all of our players we sort them by the sum of their combined values
    ultimate_dribblers = sorted(players,key=lambda player:player["CombinedVal_truefluidity"],reverse = True)
    for player in ultimate_dribblers[:n+1]:
        agility = player["Agility"]
        balance = player["Balance"]
        # ballControl = player["Ball Control"]
        # dribbling = player["Dribbling"]
        print(player.get("Player Name"),"  Combined_dribbling_attributes :",player.get("CombinedVal_truefluidity") )
        print(f"      agility : {agility}  balance : {balance}")

# get_Print_fluid_movers(30)

def get_Print_excellentDribblers(n):
    attributes = ["Ball Control","Dribbling"]
    for player in players:
        sum_attributes = 0
        for attribute in attributes:
            try:
                sum_attributes += int(player[attribute])
            except ValueError:
                pass
        player["CombinedVal_trueDribbling"] = sum_attributes

    # so now after we are done reading all of our players we sort them by the sum of their combined values
    ultimate_dribblers = sorted(players,key=lambda player:player["CombinedVal_trueDribbling"],reverse = True)
    for player in ultimate_dribblers[:n+1]:
        # agility = player["Agility"]
        # balance = player["Balance"]
        ballControl = player["Ball Control"]
        dribbling = player["Dribbling"]
        print(player.get("Player Name"),"  Combined_dribbling_attributes :",player.get("CombinedVal_trueDribbling") )
        print(f"      ball control : {ballControl}  dribbling : {dribbling}")

# get_Print_excellentDribblers(30)
def printStrongKillerStrikers(n):
    Strongkillers = get_Extreme_Killer_Attributes()
    for killer in Strongkillers[:n]:
        name = killer["Player Name"]
        acc = killer["Acceleration"]
        speed = killer["Sprint Speed"]
        long_shots = killer["Long Shots"]
        finishing = killer["Finishing"]
        strength = killer["Strength"]
        shot_power = killer["Shot Power"]
        combinedStrongFastFinisher = killer["CombinedStrongFastFinisher"]
        print(f"{name}  Acceleration : {acc}    Sprint Speed : {speed} Shot power {shot_power} Long Shot: {long_shots}  finishing : {finishing} CombinedStrongFastFinisher : {combinedStrongFastFinisher} strength : {strength}")

printStrongKillerStrikers(12)

def killersAtFinesse(n):
    attributes_target = ["Long Shots","Finishing","Curve","Positioning"]
    for player in players:
        sum_attributes = 0
        for attribute in attributes_target:
            try:
                sum_attributes += int(player[attribute])
            except ValueError:
                pass
        player["CombinedAttributes"] = sum_attributes


    excellent_finesseScorers = sorted(players,key = lambda player: player["CombinedAttributes"],reverse=True)
    return excellent_finesseScorers[:n+1]


# for finesse_genuis in killersAtFinesse(10):
#     print(finesse_genuis["Player Name"])

def killersAtFinesse2(n):
    attributes_target = ["Finishing","Curve"]
    for player in players:
        sum_attributes = 0
        for attribute in attributes_target:
            try:
                sum_attributes += int(player[attribute])
            except ValueError:
                pass
        player["lower_CombinedAttributes"] = sum_attributes


    excellent_finesseScorers = sorted(players,key = lambda player: player["lower_CombinedAttributes"],reverse=True)
    print([player["Player Name"] for player in excellent_finesseScorers[:n+1]])
    for player in excellent_finesseScorers[:n+1]:
        name = player["Player Name"]
        curve = player["Curve"]
        finishing = player["Finishing"]
        print(f"{name}  |  curve : {curve} | finishing : {finishing}")

# killersAtFinesse2(10)
    
    #get players who are 5 star weak foot and have shot power above 80
def incredibleAtScoringMultipleAngles(n):
    chosen_players = []
    try:
        for player in players:
            if player["Weak Foot"] == "5" and int(player["Finishing"]) >= 80:
                chosen_players.append(player)
    except ValueError:
        pass
    
    for player in chosen_players[:n+1]:
        print(player["Player Name"] + "  Finishing : " + player["Finishing"])
    
# incredibleAtScoringMultipleAngles(20)

# FINISHING ABOVE 90 and also 5 star weak foot
# Harry Kane  Finishing : 93
# Heung Min Son  Finishing : 91


# FINISHING ABOVE 85 and also 5 star weak foot
# Harry Kane  Finishing : 93
# Heung Min Son  Finishing : 91
# Edin Džeko  Finishing : 87
# Wissam Ben Yedder  Finishing : 87
# Diogo José Teixeira da Silva  Finishing : 86

# FINISHING ABOVE 84 and  also have a 5 star weak foot
# Kevin De Bruyne  Finishing : 85
# Diogo José Teixeira da Silva  Finishing : 86
# Edin Džeko  Finishing : 87
# Harry Kane  Finishing : 93
# Heung Min Son  Finishing : 91
# Andrea Belotti  Finishing : 85
# Wissam Ben Yedder  Finishing : 87



# I was looking for my star boy jota that was why I was doing all this
# FINISHING 80 and Above and also have a 5 star weak foot
# Kevin De Bruyne  Finishing : 85
# Neymar da Silva Santos Jr.  Finishing : 83
# Diogo José Teixeira da Silva  Finishing : 86
# Edin Džeko  Finishing : 87
# Harry Kane  Finishing : 93
# Heung Min Son  Finishing : 91
# Ivan Perišić  Finishing : 80
# Richarlison de Andrade  Finishing : 81
# Giacomo Raspadori  Finishing : 80
# Andrea Belotti  Finishing : 85
# Sergej Milinković-Savić  Finishing : 82
# Wissam Ben Yedder  Finishing : 87
# Ezequiel Ávila  Finishing : 80
# Deniz Undav  Finishing : 82
# Jonathan David  Finishing : 82
# Hans Vanaken  Finishing : 82


#find diogo Jota

# wow, it appears Jota's real name is "Diogo Jose"
def find_diogo_jota():
    for player in players:
        if "Jota" in player["Player Name"]:
            print(player["Finishing"])
            print(player["Weak Foot"])
            print(player["Team"])

# find_diogo_jota()

# get best dribblers + pacy players 

def pacyDribblers(n):
    fast_dribblers = []
    desired_attr = ["Dribbling","Sprint Speed", "Acceleration"]
    for player in players:
        sum_attr = 0
        for attribute in desired_attr:
            try:
                sum_attr += int(player[attribute])
            except ValueError:
                pass

        player["SpeedplusDribbling"] = sum_attr
        fast_dribblers.append(player)

    sorted_fastDribblers = sorted(fast_dribblers,key=lambda player: player["SpeedplusDribbling"],reverse=True)
    for killer in sorted_fastDribblers[:n+1]:
        name = killer["Player Name"]
        acc = killer["Acceleration"]
        speed = killer["Sprint Speed"]
        dribbling = killer["Dribbling"]
        print(f"{name} acceleration : {acc} speed : {speed} dribbling : {dribbling}")

# top 20 players with excellent dribbling and pace
# pacyDribblers(20)

# Kylian Mbappé acceleration : 97 speed : 97 dribbling : 93
# Adama Traoré Diarra acceleration : 96 speed : 96 dribbling : 92
# Vinícius José de Oliveira Júnior acceleration : 95 speed : 95 dribbling : 92
# Alphonso Davies acceleration : 96 speed : 93 dribbling : 87
# Ousmane Dembélé acceleration : 94 speed : 93 dribbling : 89
# Moussa Diaby acceleration : 95 speed : 92 dribbling : 88
# Jeremie Frimpong acceleration : 96 speed : 93 dribbling : 85
# Allan Saint-Maximin acceleration : 91 speed : 90 dribbling : 92
# Kingsley Coman acceleration : 94 speed : 90 dribbling : 88
# Luis Díaz acceleration : 92 speed : 91 dribbling : 89
# Antony Matheus dos Santos acceleration : 95 speed : 91 dribbling : 85
# Federico Chiesa acceleration : 91 speed : 91 dribbling : 89
# Rafael da Conceição Leão acceleration : 90 speed : 92 dribbling : 89
# Mohamed Salah acceleration : 89 speed : 91 dribbling : 90
# Juan Cuadrado acceleration : 91 speed : 89 dribbling : 90
# Leon Bailey acceleration : 93 speed : 92 dribbling : 85
# Ismaïla Sarr acceleration : 94 speed : 94 dribbling : 82
# Sadio Mané acceleration : 91 speed : 90 dribbling : 88
# Neymar da Silva Santos Jr. acceleration : 88 speed : 86 dribbling : 95
# Theo Hernández acceleration : 92 speed : 94 dribbling : 83
# Rafael A. Ferreira Silva acceleration : 92 speed : 91 dribbling : 86


# let us get fast dribblers who can also score amazing goals
def pacyDribblers_who_will_score(n):
    fast_dribblers_scorers = []
    desired_attr = ["Dribbling","Sprint Speed", "Acceleration","Finishing"]
    for player in players:
        sum_attr = 0
        for attribute in desired_attr:
            try:
                sum_attr += int(player[attribute])
            except ValueError:
                pass

        player["SpeedplusDribblingplusFinishing"] = sum_attr
        fast_dribblers_scorers.append(player)

    sorted_fastDribblers = sorted(fast_dribblers_scorers,key=lambda player: player["SpeedplusDribblingplusFinishing"],reverse=True)
    for killer in sorted_fastDribblers[:n+1]:
        name = killer["Player Name"]
        acc = killer["Acceleration"]
        speed = killer["Sprint Speed"]
        dribbling = killer["Dribbling"]
        finishing = killer["Finishing"]
        print(f"{name}  | acceleration : {acc} | speed : {speed} | dribbling : {dribbling} | finishing : {finishing}")

pacyDribblers_who_will_score(20)


# let us get Ghanaian players who excel at certain things 
# let us get Ghanaian players who have certain attributes
# the best brazilian dribblers (top 3)
# the fastest Ghanaian players
# the best Ghanaian players 
# Ghanaian players with the highest potential
# Ghanaian payers with the highest overrall

# players from Ghana who have certain attributes above 90 and print out those attributes
summary_players = []
ghanaian_players = []

with open("playerShallowStats_1.csv",newline='',encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        summary_players.append(row)

for player in summary_players:
        if player["Country"] == "Ghana":
            ghanaian_players.append(player)

def ghanaianPlayersOverall(n):
    ghanaian_players.sort(key=lambda player: int(player["Overall"]) if player["Overall"] != "--" else -1,reverse=True)
    for player in ghanaian_players[:n+1]:
        name = player["Name"]
        overall = player["Overall"]
        print(f"{name}   | overall: {overall}")


def ghanaianPlayersPotential(n):
    ghanaian_players.sort(key=lambda player: int(player["Potential"]) if player["Potential"] != "--" else -1,reverse=True)
    for player in ghanaian_players[:n+1]:
        name = player["Name"]
        potential = player["Potential"]
        print(f"{name}   | potential: {potential}")

# ghanaianPlayersOverall(20)
# ghanaianPlayersPotential(20)

def ghanaian_dribblers(n):
    good_ghanaian_dribblers = []
    for player in players:
        try:
            if player["Player Name"] in [ghanaian_player["Name"] for ghanaian_player in ghanaian_players] and int(player["Dribbling"]) >= 80:
                good_ghanaian_dribblers.append(player)
        except ValueError:
            pass
    for player in good_ghanaian_dribblers[:n+1]:
        print(player["Player Name"] + " dribbling : " + player["Dribbling"])

def ghanaian_speedsters(n):
    good_ghanaian_speedsters = []
    for player in players:
        try:
            if player["Player Name"] in [ghanaian_player["Name"] for ghanaian_player in ghanaian_players] and (int(player["Sprint Speed"])> 90 or int(player["Acceleration"])> 90):
                good_ghanaian_speedsters.append(player)
        except ValueError:
            pass

    arranged_ghanain_speedsters = sorted(good_ghanaian_speedsters,key=lambda player : int(player["Sprint Speed"]),reverse=True)
    for player in  arranged_ghanain_speedsters[:n+1]:
        speed = player["Sprint Speed"]
        acceleration = player["Acceleration"]
        name = player["Player Name"]
        print(f"{name}  |  acceleration : {acceleration}  | speed  : {speed}")

# ghanaian_dribblers(20)
# ghanaian_speedsters(20)

# acceleration or sprint speed above 90
# Tariq Lamptey  |  acceleration : 92  | speed  : 83
# Tariq Lamptey  |  acceleration : 92  | speed  : 83
# Joseph Paintsil  |  acceleration : 91  | speed  : 87
# Braydon Manu  |  acceleration : 93  | speed  : 89
# David Atanga  |  acceleration : 92  | speed  : 90        


# No ghanaian player has dribbling  90 or above

# No ghanaian player has dribbling 85 or above 

# Only two ghanaian players have dribbling 80 and above
# Thomas Partey dribbling : 84
# Mohammed Kudus dribbling : 80


#get fast ghanaian players

# sprint speed greater than 90
def ghanaian_sprinters(n):
    fast_ghanaians = []
    for player in players:
        if player["Nationality"] == "Ghana" and  int(player["Sprint Speed"]) >= 90:
            fast_ghanaians.append(player)

    for player in fast_ghanaians[:n+1]:
        print(player["Player Name"] + "  sprint speed :  " + player.get("Sprint Speed"))

def ghanaian_five_star_skillers(n):
    skilled_ghanaians = []
    for player in players:
        if player["Nationality"] == "Ghana" and  player["Skill moves"]== "5":
            skilled_ghanaians.append(player)

    for player in skilled_ghanaians[:n+1]:
        print(player["Player Name"] + "  Skill moves:  " + player.get("Skill moves"))


def ghanaian_five_star_weakFoot(n):
    bipedal_ghanaians = []
    for player in players:
        if player["Nationality"] == "Ghana" and  player["Weak Foot"]== "5":
            bipedal_ghanaians.append(player)

    for player in bipedal_ghanaians[:n+1]:
        print(player["Player Name"] +  player["Team"] + " " +  player ["League"] + "  Weak Foot:  " + player.get("Weak Foot"))


# ghanaian_sprinters(20)
# ghanaian_five_star_skillers(10)
# ghanaian_five_star_weakFoot(5)
# wow, Ghana has a five star skiller
# Daniel-Kofi Kyereh  Skill moves:  5


# oh wow, Ghana has a five star weakfoot
# Nana Ampomah  Weak Foot:  5

# These are all Ghana's four star skillers :
# Iñaki Williams Arthuer  Skill moves:  4
# Abdul Fatawu Issahaku  Skill moves:  4
# Mohammed Kudus  Skill moves:  4
# Kamaldeen Sulemana  Skill moves:  4
# Jordan Ayew  Skill moves:  4
# Kevin-Prince Boateng  Skill moves:  4
# Nana Ampomah  Skill moves:  4
# Braydon Manu  Skill moves:  4
# Tariqe Fosu  Skill moves:  4
# Emmanuel Boateng  Skill moves:  4
# Bernard Mensah  Skill moves:  4

# The list of really fast players
# Iñaki Williams Arthuer  sprint speed :  94
# Kamaldeen Sulemana  sprint speed :  93    
# Felix Afena-Gyan  sprint speed :  90      
# Emmanuel Boateng  sprint speed :  91      
# Emmanuel Boateng  sprint speed :  90      
# Yaw Yeboah  sprint speed :  90
# David Atanga  sprint speed :  90
# Ibrahim Sadiq  sprint speed :  90
# Lasso Coulibaly  sprint speed :  90       
# Frank Acheampong  sprint speed :  94      

# These are all of Ghana's 4 star weak foot
# Abdul Fatawu Issahaku  Weak Foot:  4
# Kamaldeen Sulemana  Weak Foot:  4
# Abdul Mumin  Weak Foot:  4
# Iddrisu Baba  Weak Foot:  4
# Kevin-Prince Boateng  Weak Foot:  4
# Latif Blessing  Weak Foot:  4


# I am sure brazil has more than 100 5 star skillers 
# lemme try something and see 
# cool_brazilians  = []
# for player in players:
#     if player["Nationality"] == "Brazil" and player["Skill moves"] == "5":
#         cool_brazilians.append(player)
# for player in cool_brazilians:
#     print(player["Player Name"])
# print(len(cool_brazilians))




# This is a new set of functions that locate players with all the attributes specified in a list 90 or above

# what we will do is that we will print the player's name , his team , his position and all his attributes.

#   THESE ARE THE ALL THE OVER 80 FUNCTIONS
def dribblingMonsters():
    target_atttrs = ["Agility","Balance", "Ball Control","Dribbling"]
    unique_players = []
    for player in players:
        count = 0
        for attribute in target_atttrs:
            try:
                if int(player[attribute]) >= 90:
                    count += 1
            except ValueError:
                pass
        if count == 4:
            unique_players.append(player)
    return unique_players
def get_insane_dribblers():
    Omg_dribblers = dribblingMonsters()
    for player in Omg_dribblers:
        target_atttrs = ["Player Name","Best Position","Team","Nationality","Agility","Balance", "Ball Control","Dribbling"]
        name, position, team, nationality,agility,balance,ballControl,dribbling = [player[attr] for attr in target_atttrs]
        print(f"{name}   |  {team}  | {nationality} | agility : {agility} | position : {position} balance : {balance} ballControl : {ballControl} dribbling : {dribbling}")

get_insane_dribblers()

def dribblingMonsters_lowerStandards():
    target_atttrs = ["Agility","Balance", "Ball Control","Dribbling"]
    unique_players = []
    for player in players:
        count = 0
        for attribute in target_atttrs:
            try:
                if int(player[attribute]) >= 85:
                    count += 1
            except ValueError:
                pass
        if count == 4:
            unique_players.append(player)
    return unique_players
def get_insane_dribblers_lowerStandards():
    Omg_dribblers = dribblingMonsters_lowerStandards()
    for player in Omg_dribblers:
        target_atttrs = ["Player Name","Best Position","Team","Nationality","Agility","Balance", "Ball Control","Dribbling"]
        name, position, team, nationality,agility,balance,ballControl,dribbling = [player[attr] for attr in target_atttrs]
        print(f"{name}   |  {team}  | {nationality} | agility : {agility} | position : {position} balance : {balance} ballControl : {ballControl} dribbling : {dribbling}")

# get_insane_dribblers_lowerStandards()

def killer_scorers():
    target_atttrs = ["Finishing","Sprint Speed","Acceleration"]
    unique_players = []
    for player in players:
        count = 0
        for attribute in target_atttrs:
            try:
                if int(player[attribute]) >= 85:
                    count += 1
            except ValueError:
                pass
        if count == 3:
            unique_players.append(player)
    return unique_players
def getKiller_scorers():
    Omg_scorers = killer_scorers()
    for player in Omg_scorers:
        target_atttrs = ["Player Name","Best Position","Team","Nationality","Finishing","Sprint Speed","Acceleration"]
        name, position, team, nationality,finishing,sprintSpeed,acceleration = [player[attr] for attr in target_atttrs]
        print(f"{name}   |  {team}  | {nationality} | finishing : {finishing} | position : {position} speed: {sprintSpeed} acceleration: {acceleration} ")

# getKiller_scorers()

# for this function its only one player that satisfies all the requirements for over 90 
# just mbappe
# Kylian Mbappé   |  Paris Saint-Germain  | France | finishing : 93 | position : Striker (ST) speed: 97 acceleration: 97

#when I brought the bar down to 88 
# Kylian Mbappé   |  Paris Saint-Germain  | France | finishing : 93 | position : Striker (ST) speed: 97 acceleration: 97 
# Mohamed Salah   |  Liverpool  | Egypt | finishing : 93 | position : Right Wing (RW) speed: 91 acceleration: 89 

# when I brought the bar down to 85
# Sadio Mané   |  FC Bayern München  | Senegal | finishing : 86 | position : Left Midfielder (LM) speed: 90 acceleration: 91 
# Kylian Mbappé   |  Paris Saint-Germain  | France | finishing : 93 | position : Striker (ST) speed: 97 acceleration: 97
# Mohamed Salah   |  Liverpool  | Egypt | finishing : 93 | position : Right Wing (RW) speed: 91 acceleration: 89
# Ángel Correa   |  Atlético de Madrid  | Argentina | finishing : 86 | position : Center Forward (CF) speed: 85 acceleration: 86 
# Pierre-Emerick Aubameyang   |  Chelsea  | Gabon | finishing : 87 | position : Striker (ST) speed: 89 acceleration: 85
# Heung Min Son   |  Tottenham Hotspur  | South Korea | finishing : 91 | position : Left Wing (LW) speed: 90 acceleration: 85    
# Christopher Nkunku   |  RB Leipzig  | France | finishing : 86 | position : Center Attacking Midfielder (CAM) speed: 89 acceleration: 87
# Arnaut Danjuma   |  Villarreal CF  | Netherlands | finishing : 85 | position : Left Midfielder (LM) speed: 90 acceleration: 85 
# Victor Osimhen   |  Napoli  | Nigeria | finishing : 88 | position : Striker (ST) speed: 93 acceleration: 86

# I am lookng for another way to implement the same functionality
def omg_good_dribblers():
    target_attr = ["Dribbling","Ball Control"]
    unique_players = []
    for player in players:
        count = 0
        for attr in target_attr:
            try:
                if int(player[attr]) >= 88:
                    count += 1
            except ValueError:
                pass
        if count == 2:
            unique_players.append(player)
    return unique_players


def get_over_90_dribbling_and_ballControl():
    great_dribblers = omg_good_dribblers()
    for player in great_dribblers:
        ball_control = player["Ball Control"]
        dribbling = player["Dribbling"]
        print(player["Player Name"] ,player["Team"],player["Best Position"])
        print(f"dribbling : {dribbling}  ball control : {ball_control}")
    
# get_over_90_dribbling_and_ballControl()


def omg_good_shooters():
    target_attr = ["Shot Power","Long Shots"]
    unique_players = []
    for player in players:
        count = 0
        for attr in target_attr:
            try:
                if int(player[attr]) >= 88:
                    count += 1
            except ValueError:
                pass
        if count == 2:
            unique_players.append(player)
    return unique_players


def get_over_90_longShots_and_power():
    great_shooters = omg_good_shooters()
    for player in great_shooters:
        long_shots = player["Long Shots"]
        shot_power = player["Shot Power"]
        print(player["Player Name"] ,player["Team"],player["Best Position"])
        print(f"Long Shots: {long_shots}  shot Power : {shot_power}")

    
# get_over_90_dribbling_and_ballControl()
# get_over_90_longShots_and_power()


# I am tired of copy pasting code all over again and changing a few things every now and then 
# So what I will do is to create a general purpose function and just provide the list of attributes
# and the cut off point for which you want the player to satisfy all requirements 

def get_all_players_over_n(li,n):
    unique_players = []
    len_attr = len(li)
    for player in players:
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
    for player in unique_players:
        print(player["Player Name"], player["Team"] , player["Best Position"])
        strline = " "
        for attribute in li:
            strline += attribute 
            strline += f": {player[attribute]}  | "
        print(strline)

defending_attributes = ["Sliding Tackle","Standing Tackle","Marking"]

# create a function that accepts one list of attributes and another list of values whose elements are integers 
# This way we can be more flexible with the value 
def get_players_over_different_n_values(li_attr,li_values):
    # if the length of the attributes and the length of the values aren't the same, raise an error. 
    attributes_length = len(li_attr)
    values_length = len(li_values)
    if attributes_length != values_length:
        return "your values don't match your attributes"

    # group each attribute and value into a tuple
    unique_players = []
    for player in players:
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

    for player in unique_players:
        print(player["Player Name"], player["Team"] , player["Best Position"])
        strline = " "
        for attribute in li_attr:
            strline += attribute 
            strline += f": {player[attribute]}  | "
        print(strline)
# for example let's say we want play maker attributes. 
# agility and balance over 88
# short passing and long passing over 88
# dribbling over 88
# ball control also over 88 
#vision over 85
playmaker_attributes_list = ["Short Passing","Long Passing","Dribbling","Balance","Agility","Vision"]
defenders_list = ["Sliding Tackle","Standing Tackle","Strength","Aggression"]
# defenders_values = [88,88,85,80]  # no one exists
defenders_values = [85,85,80,80]
excellent_defending_attributes = ["Acceleration","Sprint Speed","Strength","Standing Tackle","Aggression"]
# excellent_defending_values = [80,80,85,85,80]   # no person exist
playmaker_values = [88,88,88,88,88,85]
excellent_defending_values = [75,80,85,85,80]

# excellent defending attributes
# Presnel Kimpembe Paris Saint-Germain Center Back (CB)
#  Acceleration: 79  | Sprint Speed: 80  | Strength: 88  | Standing Tackle: 86  | Aggression: 90  |
# Milan Škriniar Inter Center Back (CB)
#  Acceleration: 75  | Sprint Speed: 81  | Strength: 89  | Standing Tackle: 90  | Aggression: 87  |

deadly_playmaking_attributes = ["Dribbling","Ball Control","Short Passing","Finishing"]
deadly_playmaking_values = [85,88,85,87]

# best set piece takers 

# get_players_over_different_n_values(playmaker_attributes_list,playmaker_values)
# get_players_over_different_n_values(defenders_list,defenders_values)
# get_players_over_different_n_values(excellent_defending_attributes,excellent_defending_values)
# get_players_over_different_n_values(deadly_playmaking_attributes,deadly_playmaking_values)

# Karim Benzema Real Madrid CF Center Forward (CF)
#  Dribbling: 87  | Ball Control: 91  | Short Passing: 89  | Finishing: 92  | 
# Kylian Mbappé Paris Saint-Germain Striker (ST)
#  Dribbling: 93  | Ball Control: 91  | Short Passing: 85  | Finishing: 93  |
# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Dribbling: 95  | Ball Control: 93  | Short Passing: 91  | Finishing: 90  |


# playmakers 
# Lionel Messi Paris Saint-Germain Center Attacking Midfielder (CAM)
#  Short Passing: 91  | Long Passing: 90  | Dribbling: 95  | Balance: 95  | Agility: 91  | Vision: 94  | 
# Marco Verratti Paris Saint-Germain Center Midfielder (CM)
#  Short Passing: 90  | Long Passing: 89  | Dribbling: 91  | Balance: 93  | Agility: 90  | Vision: 89  |
# Thiago Alcântara Liverpool Center Midfielder (CM)
#  Short Passing: 91  | Long Passing: 89  | Dribbling: 89  | Balance: 90  | Agility: 90  | Vision: 88  |

# get_all_players_over_n(defending_attributes,88)

# only one person with sliding tackle, standing tackle and marking over 90
# Marcos Aoás Corrêa Paris Saint-Germain Center Back (CB)
#  Sliding Tackle: 89  | Standing Tackle: 89  | Marking: 90  |

# get_all_players_over_n(defending_attributes,87)

# Marcos Aoás Corrêa Paris Saint-Germain Center Back (CB)
#  Sliding Tackle: 89  | Standing Tackle: 89  | Marking: 90  |
# Carlos Henrique Venancio Casimiro Manchester United Center Defensive Midfielder (CDM)
#  Sliding Tackle: 87  | Standing Tackle: 88  | Marking: 87  |

# get_all_players_over_n(defending_attributes,85)

# Marcos Aoás Corrêa Paris Saint-Germain Center Back (CB)
#  Sliding Tackle: 89  | Standing Tackle: 89  | Marking: 90  | 
# PS C:\Users\HP\Desktop\experimental_scapper> python .\version2_playerManipulation.py
# Marcos Aoás Corrêa Paris Saint-Germain Center Back (CB)
#  Sliding Tackle: 89  | Standing Tackle: 89  | Marking: 90  |
# Carlos Henrique Venancio Casimiro Manchester United Center Defensive Midfielder (CDM)
#  Sliding Tackle: 87  | Standing Tackle: 88  | Marking: 87  |
# PS C:\Users\HP\Desktop\experimental_scapper> python .\version2_playerManipulation.py
# Rúben Santos Gato Alves Dias Manchester City Center Back (CB)
#  Sliding Tackle: 85  | Standing Tackle: 89  | Marking: 90  | 
# Aymeric Laporte Manchester City Center Back (CB)
#  Sliding Tackle: 86  | Standing Tackle: 87  | Marking: 86  |
# Marcos Aoás Corrêa Paris Saint-Germain Center Back (CB)
#  Sliding Tackle: 89  | Standing Tackle: 89  | Marking: 90  |
# Virgil van Dijk Liverpool Center Back (CB)
#  Sliding Tackle: 86  | Standing Tackle: 92  | Marking: 92  |
# Fábio Henrique Tavares Liverpool Center Defensive Midfielder (CDM)
#  Sliding Tackle: 86  | Standing Tackle: 88  | Marking: 86  |
# Stefan de Vrij Inter Center Back (CB)
#  Sliding Tackle: 85  | Standing Tackle: 87  | Marking: 88  |
# José María Giménez Atlético de Madrid Center Back (CB)
#  Sliding Tackle: 85  | Standing Tackle: 85  | Marking: 87  |
# N’Golo Kanté Chelsea Center Defensive Midfielder (CDM)
#  Sliding Tackle: 86  | Standing Tackle: 93  | Marking: 90  |
# Kalidou Koulibaly Chelsea Center Back (CB)
#  Sliding Tackle: 86  | Standing Tackle: 89  | Marking: 90  |
# Carlos Henrique Venancio Casimiro Manchester United Center Defensive Midfielder (CDM)
#  Sliding Tackle: 87  | Standing Tackle: 88  | Marking: 87  |
# Cristian Romero Tottenham Hotspur Center Back (CB)
#  Sliding Tackle: 85  | Standing Tackle: 86  | Marking: 86  |
# Mats Hummels Borussia Dortmund Center Back (CB)
#  Sliding Tackle: 85  | Standing Tackle: 86  | Marking: 88  |
# Raúl Albiol Tortajada Villarreal CF Center Back (CB)
#  Sliding Tackle: 85  | Standing Tackle: 86  | Marking: 87  |

strongFinishers = ["Strength","Finishing","Shot Power"]
# get_all_players_over_n(strongFinishers,90)

# over 90 
# Erling Haaland Manchester City Striker (ST)
#  Strength: 93  | Finishing: 94  | Shot Power: 94  | 

# get_all_players_over_n(strongFinishers,88)  no one exists beside halaand
# get_all_players_over_n(strongFinishers,85)

# over 85

# Erling Haaland Manchester City Striker (ST)
#  Strength: 93  | Finishing: 94  | Shot Power: 94  | 
# Robert Lewandowski FC Barcelona Striker (ST)
#  Strength: 87  | Finishing: 94  | Shot Power: 91  |
# Romelu Lukaku Inter Striker (ST)
#  Strength: 95  | Finishing: 88  | Shot Power: 87  |
# Edin Džeko Inter Striker (ST)
#  Strength: 86  | Finishing: 87  | Shot Power: 86  |
# Olivier Giroud AC Milan Striker (ST)
#  Strength: 90  | Finishing: 86  | Shot Power: 86  |
# Duván Zapata Atalanta Striker (ST)
#  Strength: 95  | Finishing: 87  | Shot Power: 86  |
# Kevin Volland AS Monaco Striker (ST)
#  Strength: 86  | Finishing: 85  | Shot Power: 87  |

extreme_defending_attributes = ["Sliding Tackle","Standing Tackle","Marking","Acceleration","Sprint Speed"]
# get_all_players_over_n(extreme_defending_attributes,88)  # no one exists for over 88
# get_all_players_over_n(extreme_defending_attributes,84)  # no one exists for all these attributes  over 84
# get_all_players_over_n(extreme_defending_attributes,83)  # some people exist for all these attributes over 83

# Éder Gabriel Militão Real Madrid CF Center Back (CB)
#  Sliding Tackle: 84  | Standing Tackle: 86  | Marking: 85  | Acceleration: 83  | Sprint Speed: 88  | 
# Jules Koundé FC Barcelona Center Back (CB)
#  Sliding Tackle: 83  | Standing Tackle: 85  | Marking: 85  | Acceleration: 85  | Sprint Speed: 83  | 

# get_all_players_over_n(extreme_defending_attributes,82)  # no one exists for all these attributes over 82
# get_all_players_over_n(extreme_defending_attributes,80)

# João Pedro Cavaco Cancelo Manchester City Left Back (LB)
#  Sliding Tackle: 80  | Standing Tackle: 84  | Marking: 81  | Acceleration: 86  | Sprint Speed: 84  | 
# Éder Gabriel Militão Real Madrid CF Center Back (CB)
#  Sliding Tackle: 84  | Standing Tackle: 86  | Marking: 85  | Acceleration: 83  | Sprint Speed: 88  |
# Jules Koundé FC Barcelona Center Back (CB)
#  Sliding Tackle: 83  | Standing Tackle: 85  | Marking: 85  | Acceleration: 85  | Sprint Speed: 83  |
# Fikayo Tomori AC Milan Center Back (CB)
#  Sliding Tackle: 82  | Standing Tackle: 89  | Marking: 86  | Acceleration: 80  | Sprint Speed: 90  |
# Roger Ibañez Da Silva Roma Center Back (CB)
#  Sliding Tackle: 84  | Standing Tackle: 80  | Marking: 80  | Acceleration: 85  | Sprint Speed: 80  |

# my next goal 
# The thing is that I don't want to be manually creating the list of Attributes each and every time 
# since the number of combinations is so numerous. I want to write code in python that handles this for me. 

primal_attributes = ['Crossing', 'Finishing', 'Heading Accuracy', 'Short Passing', 'Volleys', 'Dribbling', 'Curve', 'FK Accuracy', 'Long Passing', 'Ball Control', 'Acceleration', 'Sprint Speed', 'Agility', 'Reactions', 'Balance', 'Shot Power', 'Jumping', 'Stamina', 'Strength', 'Long Shots', 'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'Standing Tackle', 'Sliding Tackle']
goal_keeper_attributes = ['GK Diving', 'GK Handling', 'GK Kicking', 'GK Positioning', 'GK Reflexes']

# I need to generate a combination of four attributes out of this list and I don't want any attributes 
# to get repeated.

# from a group of the list of attributes, combine three attributes and put them  in a list and print them out to the console.

#random.choices returns a list.
# attributes = random.choices(primal_attributes,k=3)
# print(attributes)

# The thing is that I don't wan't some attributes to repeat 

length_of_primal_attributes = len(primal_attributes)
arr_of_3_attributes = []
def generateRandomIndex():
        attr_index = random.randint(0,length_of_primal_attributes-1)
        return attr_index
for i in range(3):
    index = generateRandomIndex()
    if primal_attributes[index] in arr_of_3_attributes:
        index = generateRandomIndex()
    else:
        arr_of_3_attributes.append(primal_attributes[index])
print(arr_of_3_attributes)
# ['Reactions', 'Curve', 'Long Shots']
# ['Volleys', 'Sprint Speed', 'Short Passing']
# ['Jumping', 'Shot Power', 'Strength']
# ['Finishing', 'Sprint Speed', 'Long Passing']
# ['Interceptions', 'FK Accuracy', 'Marking']
# ['Crossing', 'Ball Control', 'Dribbling']
# ['Sprint Speed', 'Sprint Speed', 'Interceptions']



#to do 
# find players with above 85 for all the following ["Sliding Tackle","Standing Tackle","Marking"]
# find players with above 85 for all the following ["Sliding Tackle","Standing Tackle","Marking","Acceleration","Sprint Speed"]
# find players with above 85 for all the following ["Standing Tackle","Marking","Strength","Acceleration"]