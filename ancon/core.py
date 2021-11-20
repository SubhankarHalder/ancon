""" 
Business Logic
"""
def pascalvoc_to_yolo(img_width, img_height, box):
    """Convert a box with arguments to x_min, y_min, x_max, y_max to YOLO format
       The YOLO format is x_center, y_center, width, height (Normalized)

    Args:
        img_width (int): Width of the image
        img_height (int): Height of the image  
        box (List): Bounding Box coordinates in the format
                    x_min, y_min, x_max, y_max

    Returns:
        List: Box coordinates in YOLO format
    """
    x_min, y_min, x_max, y_max = box
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
