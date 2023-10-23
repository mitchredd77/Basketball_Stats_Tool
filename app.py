### Importing data to extract statistics from
from constants import TEAMS, PLAYERS

### no_exp is a list of players that are inexperienced & exp is  a list of players that are experienced
no_exp = []
exp = []

## new_constants will hold the cleaned and modified data
new_constants = []

### Function to separate experienced and non-experienced players
def ability(data):
    global no_exp
    global exp
    for dict in PLAYERS:
        if dict['experience'] == "NO":
            no_exp.append(dict)
        else:
            exp.append(dict)

### clean the data and place players balanced on each team, exp and non-exp players
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
            fixed['guardians'] = dict['guardians'].split(" and ", 1)
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

### when a team is picked that teams data is processed in this funtion
def team_data(player_data, team_name):
    team_info = []
    player_guardians = []
    sep_guardians = []
    in_exp_total = 0
    exp_total = 0
    total_height = 0
    for dict in new_constants:
        if dict['team'] == team_name:
           team_info.append(dict)
    ### print the team name name then total players on the team
    print("\033[1m" + "{}".format(team_name))
    print("\nThere are {} total players on the {} and they are:\n".format(len(team_info), team_name))

    ### print each players name separated by a comma
    for player in team_info:
       print(player['name'], end=", ")
       total_height = total_height + player['height']
       player_guardians.append(player['guardians'])
       if player['experience'] == False:
           in_exp_total += 1
       else:
           exp_total += 1
    
    print("\n\nThere are {} inexperienced players on the {}".format(in_exp_total, team_name))
    print("\nThere are {} experienced players on the {}".format(exp_total, team_name))
    print("\nAverage height is {}\n". format(total_height/len(team_info)))
    

### print out guardians of team separated by comma ###
    for guardian in player_guardians:
        for sep_guardian in guardian:
            sep_guardians.append(sep_guardian)
    print(f"The player's guardians on team {team_name} are:\n\n" + ", ".join([guardian for guardian in sep_guardians]))
### Menu Function ###
def menu():
    while True:
        team_selection = int(input("\nWhat team would you like to see statistics on?\n\nselect 1 for Panthers, 2 for Bandits, 3 for Warriors, or 4 to quit  "))

### if statements to add players to teams evenly
        if team_selection == 1:
            team_data(new_constants, "Panthers")
        elif team_selection == 2:
            team_data(new_constants, "Bandits")
        elif team_selection == 3:
            team_data(new_constants, "Warriors")
        elif team_selection == 4:
            break
if __name__ == "__main__":

### run functions for program to run        
    ability(PLAYERS)
    clean_data(exp, TEAMS)
    clean_data(no_exp, TEAMS)
    while True:
        try:
            menu()
            break
        except ValueError:
            print("\nYou did not enter 1, 2, 3, or 4!")
            continue
        except:
            print("\nThere was an error with your input, please select 1, 2, 3, or 4!")
            continue


