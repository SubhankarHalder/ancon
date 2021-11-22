"""
Helper functions
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


def class_values(names_file):
    """Get integer value of classes from .names file

    Args:
        names_file (type): File containing a list of classes.
                           Each line of the file should contain
                           a separate class name

    Returns:
        class_dict (dict): Dict that maps class names with
                           integer values
    """
    class_dict = {}
    with open(names_file) as f:
        for index, name in f:
            class_dict[name] = index
    if not class_dict:
        raise ValueError("Names file is empty.")
    return class_dict
