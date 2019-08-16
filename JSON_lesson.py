import json

filename = 'Players_settings.txt'
file = open(filename, 'w')

player1 = {
    'name': 'Tim',
    'age': 19,
    'nick': 'FamousLord',
    'rank': 'master_guardian1'
}

player2 = {
    'name': 'Jason',
    'age': 17,
    'nick': 'BADMAN',
    'rank': 'global_elite'
}

players = []
players.append(player1)
players.append(player2)

# SAVE by JSON
json.dump(players, file)

file.close()

# LOAD by JSON
file = open(filename, 'r')
json_data = json.load(file)
for user in json_data:
    print('Player_Name is ' + str(user['name']))
    print('Rank is ' + str(user['rank']))
