import json
import os

def load_rules():
    base_dir = os.path.dirname(os.path.dirname(__file__)) 
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as f:
        return json.load(f)
