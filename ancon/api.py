"""
API Endpoints
"""
from core import file_lmj_yolo, dir_lmj_yolo


def convert_file(src_fmt, tgt_fmt, src_file, dest_dir,
                 **kwargs):
    """Converts annotation file from one format to another

    Args:
        src_fmt (str): Source annotation format type
        tgt_fmt (str): Target annotation format type
        src_file (str): Path to the annotation file
        dest_dir (str): Path to destination format where
                        the new annotation file would be saved
        kwargs (str): Names file path. Make a dict,
                      kwargs["names":"path/to/file"] and pass **kwargs
    Raises:
        ValueError: For src_fmt and tgt_fmt that are not supported
    """
    file_dispatcher = {'lmj': {'yolo': file_lmj_yolo}}
    try:
        file_dispatcher[src_fmt][tgt_fmt](src_file, dest_dir, kwargs)
    except KeyError:
        raise ValueError(f"{src_fmt} to {tgt_fmt} conversion not supported")


def convert_folder(src_fmt, tgt_fmt, src_dir,
                   dest_dir, **kwargs):
    """Converts annotation files in a folder from one format to another

    Args:
        src_fmt (str): Source annotation format type
        tgt_fmt (str): Target annotation format type
        src_dir (str): Path to the folder containing the annotations files
        dest_dir (str): Path to destination format where
                        the new annotation files would be saved
        kwargs (str): Names file path. Make a dict,
                      kwargs["names":"path/to/file"] and pass **kwargs
    Raises:
        ValueError: For src_fmt and tgt_fmt that are not supported
    """
    dir_dispatcher = {'lmj': {'yolo': dir_lmj_yolo}}
    try:
        dir_dispatcher[src_fmt][tgt_fmt](src_dir, dest_dir, kwargs)
    except KeyError:
        raise ValueError(f"{src_fmt} to {tgt_fmt} conversion not supported")
