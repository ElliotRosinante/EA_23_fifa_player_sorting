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
batch_size = 20
num_batches = len(duplicates_removed_team_links) // batch_size
last_batch_size = len(duplicates_removed_team_links) % batch_size
for i in range(num_batches):
    batch_start = i * batch_size
    batch_end = (i + 1) * batch_size
    batch_links = duplicates_removed_team_links[batch_start:batch_end]
