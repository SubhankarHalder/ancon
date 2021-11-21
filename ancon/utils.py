"""
Helper functions
"""
import json
from config import allowed_formats, names_file_req


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


def check_input_format(source_format, target_format):
    """Check if allowed source/target formats have been provided

    Args:
        source_format (str): Source Format
        target_format (str): Target Format

    Raises:
        ValueError: If source format is wrong or not currently supported
        ValueError: If target format is wrong or not currently supported
    """
    if source_format not in allowed_formats:
        raise ValueError("Source Format is not currently supported")
    if target_format not in allowed_formats[source_format]:
        raise ValueError("Target Format is not currently supported")


def check_names_file_req(source_format, target_format, names_file):
    """Checks if names file is provided for given source and target formats

    Args:
        source_format (str): Source Format
        target_format (str): Target Format

    Raises:
        ValueError: If Names file is required
                    and user hasn't passed that as a function argument
    """
    if source_format in names_file_req:
        if target_format in names_file_req[source_format]:
            if not names_file:
                raise ValueError("Names File required as function argument")
