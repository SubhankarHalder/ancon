""" 
Helper functions for the library
"""
import json
from config import lmj_keys

def json_extract(json_path):
    """Converts JSON file to Python Dict

    Args:
        json_path (str): Path to JSON file

    Returns:
        data (dict): Dictionary containing JSON information 
    """
    with open(json_path) as f:
        data = json.load(f)
        return data

def check_lmj_keys(lmj_dict):
    """Check if LabelMeJSON dict contains relevant keys

    Args:
        lmj_dict (dict): LabelMeJSON dict

    Returns:
        boolean: True or False
    """
    counter = 0
    for key in lmj_dict.keys():
        if key in lmj_keys:
            counter += 1
    if counter == len(lmj_keys):
        return True
    else:
        return False
