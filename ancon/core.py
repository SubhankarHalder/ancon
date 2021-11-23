"""
Business Logic
"""
from pathlib import Path
from utils import json_extract, class_values
from utils import pascalvoc_yolo, lmj_pascalvoc
from tqdm import tqdm


def lmj_yolo(json_file_path, target_dir, class_dict):
    """Converts a single LabelMe JSON to YOLO text file

    Args:
        json_file_path (Union[str, PosixPath]): Path to LMJSON file
        target_dir (str): Path to target directory
        class_dict (dict[str: int]): Hash Map containing class names to
                                     integer mapping
    """
    json_dict = json_extract(json_file_path)
    img_width = json_dict["imageWidth"]
    img_height = json_dict["imageHeight"]
    label_list = json_dict["shapes"]
    json_path = Path(json_file_path)
    json_path_txt_suffix = json_path.with_suffix(".txt")
    txt_path = Path(target_dir) / json_path_txt_suffix.name
    txt_outfile = open(txt_path, "a")
    for idv_label in label_list:
        yolo_class = class_dict(idv_label["label"])
        pascalvoc_box = lmj_pascalvoc(idv_label["points"])
        yolo_box = pascalvoc_yolo(img_width, img_height,
                                  pascalvoc_box)
        yolo_box_str = " ".join([str(val) for val in yolo_box])
        yolo_txt_str = "".join([yolo_class, " ", yolo_box_str, "\n"])
        txt_outfile.write(yolo_txt_str)


def preproces_lmj(dest_dir, **kwargs):
    """(1) Creates destination directory
       (2) Gets class labels to integer mapping

    Args:
        dest_dir (str): Output directory where converted
                        annotation file would be dumped

    Returns:
        class_dict(dict): Labels to Integer mapping hash map
    """
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    names_file_path = kwargs["names"]
    class_dict = class_values(names_file_path)
    return class_dict


def file_lmj_yolo(src_file, dest_dir, kwargs_dict):
    """Serves as a wrapper to lmj_yolo function
       for a single annotation file

    Args:
        src_file (str): Path to the annotation file
        dest_dir (str): Output folder where converted
                        annotation file would be dumped
        kwargs_dict (dict): Path to names file for the
                            keyword 'names'
    """
    class_dict = preproces_lmj(dest_dir, kwargs_dict)
    lmj_yolo(src_file, dest_dir, class_dict)


def dir_lmj_yolo(src_dir, dest_dir, kwargs_dict):
    """Serves as a wrapper to lmj_yolo function
       for a folder of annotation files

    Args:
        src_dir (str): Path to folder containing
                       annotation files
        dest_dir (str): Output folder where converted
                        annotation file would be dumped
        kwargs_dict (dict): Path to names file for the
                            keyword 'names'
    """
    class_dict = preproces_lmj(dest_dir, kwargs_dict)
    for file in tqdm(list(Path(src_dir).iterdir())):
        if file.suffix == ".json":
            lmj_yolo(file, dest_dir, class_dict)
