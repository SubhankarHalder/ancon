"""
API Endpoints
"""
from utils import check_input_format, check_names_file_req
from core import file_lmjrect_yolo, dir_lmjrect_yolo


def convert_file(src_fmt, tgt_fmt, src_file, dest_dir,
                 names_file=None, img_file=None):
    """Converts annotation file from one format to another

    Args:
        src_fmt (str): Source annotation format type
        tgt_fmt (str): Target annotation format type
        src_file (str): Path to the annotation file
        dest_dir (str): Path to destination format where
                                  the new annotation file would be saved
        names_file (str): Path to names file that contains list of classes.
                          Required for certain conversions. Defaults to None.
        img_file (str): Path to image file. Required for certain conversions.
                        Defaults to None.
    """
    check_input_format(src_fmt, tgt_fmt)
    check_names_file_req(src_fmt, tgt_fmt, names_file)
    optional_args = {"names": names_file, "img": img_file}
    file_dispatcher = {'lmj-rect': {'yolo': file_lmjrect_yolo}}
    file_dispatcher[src_fmt][tgt_fmt](src_file, dest_dir, optional_args)


def convert_folder(src_fmt, tgt_fmt, src_dir,
                   dest_dir, names_file=None, img_dir=None):
    """Converts annotation files in a folder from one format to another

    Args:
        src_fmt (str): Source annotation format type
        tgt_fmt (str): Target annotation format type
        src_dir (str): Path to the folder containing the annotations files
        dest_dir (str): Path to destination format where
                                  the new annotation files would be saved
        names_file (str): Path to names file that contains list of classes.
                          Required for certain conversions. Defaults to None.
        img_dir (str): Path to folder containing image files.
                        Required for certain conversions. Defaults to None.
    """
    check_input_format(src_fmt, tgt_fmt)
    check_names_file_req(src_fmt, tgt_fmt, names_file)
    optional_args = {"names": names_file, "img": img_dir}
    dir_dispatcher = {'lmj-rect': {'yolo': dir_lmjrect_yolo}}
    dir_dispatcher[src_fmt][tgt_fmt](src_dir, dest_dir, optional_args)
