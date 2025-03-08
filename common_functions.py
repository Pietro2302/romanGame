import json

def load_characters(filename):
    try: 
        with open(filename,"r") as json_file:
            type(json_file)
            return json.load(json_file)
    except FileNotFoundError:
        return []
    
def save_characters(filename, characters_dict):
    with open(filename, "w") as json_file:
        json.dump(characters_dict, json_file, indent=4)