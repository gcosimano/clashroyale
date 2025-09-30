import json

class Runner:
    file_path = 'troops.json'
    with open(file_path, 'r') as file:
            json_data = json.load(file)

    list_of_objects = []
    for x in json_data:
          obj = Card(x['sc_key'], x['elixir'], x['type'], x['combat_state'], x['damage'], x['mechanics'], x['counters'], x['synergies']) # type: ignore
          list_of_objects.append(obj)        