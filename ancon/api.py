""" 
API Endpoints 
"""
def convert_file(source_format, target_format, source_file, destination_folder, names_file=None, img_file=None):
    """Converts annotation file from one format to another

    Args:
        source_format (str): Source annotation format type
        target_format (str): Target annotation format type
        source_file (str): Path to the annotation file
        destination_folder (str): Path to destination format where
                                  the new annotation file would be saved  
        names_file (str): Path to names file that contains list of classes.
                          Required for certain conversions. Defaults to None.
        img_file (str): Path to image file. Required for certain conversions.
                        Defaults to None.
    """
    pass

def convert_folder(source_format, target_format, source_folder, destination_folder, names_file=None, img_folder=None):
    """Converts annotation files in a folder from one format to another

    Args:
        source_format (str): Source annotation format type
        target_format (str): Target annotation format type
        source_file (str): Path to the folder containing the annotations files
        destination_folder (str): Path to destination format where
                                  the new annotation files would be saved  
        names_file (str): Path to names file that contains list of classes.
                          Required for certain conversions. Defaults to None.
        img_file (str): Path to folder containing image files.
                        Required for certain conversions. Defaults to None.
    """
    pass