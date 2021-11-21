"""
Business Logic
"""
from pathlib import Path
from utils import json_extract


def pascalvoc_boxconvert_yolo(img_width, img_height, pascalvoc_box):
    """Convert a box with arguments to x_min, y_min, x_max, y_max to YOLO
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


def extract_lmj_rect_pascalvoc(label_dict):
    """Extracts box coordinates from lmjson labels to pascalvoc

    Args:
        label_dict (dict): lmjson label dictionary

    Returns:
        list: Box coordinates in Pascalvoc
              [x_min, y_min, x_max, y_max]
    """
    x_min = label_dict["points"][0][0]
    y_min = label_dict["points"][0][0]
    x_max = label_dict["points"][1][0]
    y_max = label_dict["points"][1][1]
    return [x_min, y_min, x_max, y_max]


def lmj_rect_yolo(json_file_path, target_dir, class_dict):
    stats = {"converted": 0, "skipped": 0}
    json_dict = json_extract(json_file_path)
    img_width = json_dict["imageWidth"]
    img_height = json_dict["imageHeight"]
    label_list = json_dict["shapes"]
    json_path = Path(json_file_path)
    json_path_txt_suffix = json_path.with_suffix(".txt")
    txt_path = Path(target_dir) / json_path_txt_suffix.name
    txt_outfile = open(txt_path, "a")
    for idv_label in label_list:
        if idv_label["shape_type"] == "rectangle":
            yolo_class = class_dict(idv_label["label"])
            pascalvoc_box = extract_lmj_rect_pascalvoc(idv_label)
            yolo_box = pascalvoc_boxconvert_yolo(img_width, img_height,
                                                 pascalvoc_box)
            yolo_box_str = " ".join([str(val) for val in yolo_box])
            yolo_txt_str = "".join([yolo_class, " ", yolo_box_str, "\n"])
            txt_outfile.write(yolo_txt_str)
            stats["converted"] += 1
        else:
            stats["skipped"] += 1
    return stats
