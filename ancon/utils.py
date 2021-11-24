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
    """Gets integer value of classes from .names file

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
        raise Exception("Names file is empty.")
    return class_dict


def lmj_pascalvoc(matrix):
    """Extracts box coordinates from lmjson labels to pascalvoc

    Args:
        label_dict (list of lists): lmjson points matrix

    Returns:
        list of floats: Box coordinates in Pascalvoc
              [x_min, y_min, x_max, y_max]
    """
    min_column = [min(column) for column in zip(*matrix)]
    max_column = [max(column) for column in zip(*matrix)]
    x_min = min_column[0]
    y_min = min_column[1]
    x_max = max_column[0]
    y_max = max_column[1]
    return [x_min, y_min, x_max, y_max]


def pascalvoc_yolo(img_width, img_height, pascalvoc_box):
    """Converts a box with arguments to x_min, y_min, x_max, y_max to YOLO
       The YOLO format is x_center, y_center, width, height (Normalized)

    Args:
        img_width (int): Width of the image
        img_height (int): Height of the image
        pascalvoc_box (List of floats): Bounding Box coordinates
                                        x_min, y_min, x_max, y_max

    Returns:
        list: Box coordinates in YOLO[x_center, y_center, width, height]
    """
    x_min, y_min, x_max, y_max = pascalvoc_box
    x = (x_min + x_max)/2.0
    y = (y_min + y_max)/2.0
    w = x_max - x_min
    h = y_max - y_min
    # Normalize
    x /= img_width
    w /= img_width
    y /= img_height
    h /= img_height
    return [x, y, w, h]
