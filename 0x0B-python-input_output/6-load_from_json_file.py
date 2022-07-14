#!/usr/bin/python3
"""write an Object to a text file, using a JSON representation."""
import json


def load_from_json_file(filename):
    """JSON representation."""
    with open(filename, mode='w', encoding='utf-8')as f:
        return json.load(f)
