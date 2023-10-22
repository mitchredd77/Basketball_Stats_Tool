from constants import TEAMS, PLAYERS

no_exp = []
exp = []
new_constants = []

def ability(data):
    global no_exp
    global exp
    for dict in PLAYERS:
        if dict['experience'] == "NO":
            no_exp.append(dict)
        else:
            exp.append(dict)
def clean_data(players, teams):
    teams_not_full = True
    global new_constants
    goodexp = 0
    global no_exp
    global exp
    team_one = True
    team_two = False
    team_three = False

    for dict in players:
        fixed = {}
        fixed["name"] = dict["name"]
        if dict["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        if "and" in dict['guardians']:
            fixed['guardians'] = dict['guardians'].split("and", 1)
        else:
            fixed['guardians'] = dict['guardians'].split(" ", 0)
        fixed['height'] = int(dict['height'].split(" ")[0])
        new_constants.append(fixed)
        if team_one == True:
            fixed["team"] = teams[0]
            team_two = True
            team_one = False
        elif team_two == True:
            fixed["team"] = teams[1]
            team_three = True
            team_two = False
        else:
            fixed["team"] = teams[2]
            team_one = True
            team_three = False
        



ability(PLAYERS)
clean_data(exp, TEAMS)
clean_data(no_exp, TEAMS)
for team in new_constants:
    print(team['team'])
print(new_constants)
#if __name__ == "__main__":
