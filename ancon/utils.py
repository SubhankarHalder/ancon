""" 
Helper functions for the library
"""
import json

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