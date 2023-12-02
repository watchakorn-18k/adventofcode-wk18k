"""
wk-18k
"""

import re

list_data = []
with open("input.txt","r") as f:
    for line in f:
        line = line.strip()
        list_data.append(line)


def parse_game_results(game_results):
    parsed_games = []
    for game_result in game_results:
        game_number = int(re.findall(r'Game (\d+):', game_result)[0])
    
        sets = game_result.split(';')
        game_data = {'game': game_number, 'sets': []}

        for set_data in sets:
            set_dict = {}
            
            for count , color  in re.findall(r'(\d+) (\w+)', set_data):
                set_dict[color] = int(count)

            game_data['sets'].append(set_dict)

        parsed_games.append(game_data)

    return parsed_games

game_results = list_data

parsed_games = parse_game_results(game_results)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


for i in parsed_games:
    maximum_values = {}
    for dictionary in i["sets"]:
        for key, value in dictionary.items():
            if key not in maximum_values or value > maximum_values[key]:
                maximum_values[key] = value

    sorted_values = sorted(maximum_values.items(), key=lambda x: ['red', 'blue', 'green'].index(x[0]))

    sorted_dict = dict(sorted_values)
    i["sets"] = sorted_dict


game_id_list = []
rgb_list = []
for i in parsed_games:
    if i["sets"]["blue"] <= MAX_BLUE and i["sets"]["green"] <= MAX_GREEN and i["sets"]["red"] <= MAX_RED:
        game_id_list.append(i["game"])
    rgb_list.append(i["sets"]["blue"] * i["sets"]["green"] * i["sets"]["red"])

print("part 1 = ",sum(game_id_list))
print("part 2 = ",sum(rgb_list))