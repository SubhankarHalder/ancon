""" 
Business Logic
"""
def box_to_yolo(img_width, img_height, box):
    """Convert a box with arguments to x_min, x_max, y_min, y_max to YOLO format
       The YOLO format is x_center, y_center, width, height (Normalized)

    Args:
        img_width (int): Width of the image
        img_height (int): Height of the image  
        box (List): Bounding Box coordinates in the format
                    x_min, x_max, y_min, y_max

    Returns:
        List: Box coordinates in YOLO format
    """
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    
    # Normalize
    x /= img_width 
    w /= img_width
    y /= img_height
    h /= img_height
    
    return [x, y, w, h]

