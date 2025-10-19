import json

def save_data(data, file="database.json"):
    with open(file, "w") as f:
        json.dump(data, f)

def load_data(file="database.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
