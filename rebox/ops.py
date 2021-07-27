import numpy as np
from rebox import BBox
from rebox import BBoxFormat

def iou(a, b):
    """
    Compute the Jaccarrd Index / Intersection over Union of a pair of 2D bounding boxes.

    Args:
        a: BBox object
        b: BBox object

    Returns:
        The IoU of the two bounding boxes.
    """

    # dealing with various formats:
    # unify style to XYXY,
    # keep scale, and account for it in algorithm

    scale = a.format.scale
    style = a.format.style

    unified_format = BBoxFormat("XYXY", scale)

    a = a.as_format(unified_format)
    b = b.as_format(unified_format)

    xA = np.maximum(a.x1, b.x1)
    yA = np.maximum(a.y1, b.y1)
    xB = np.maximum(a.x2, b.x2)
    yB = np.maximum(a.y2, b.y2)

    if scale is None:
        inter_w = xB - xA + 1
    else:
        inter_w = xB - xA

    inter_w = inter_w * (inter_w >= 0)

    if scale is None:
        inter_h = yB - yA + 1
    else:
        inter_h = yB - yA

    inter_h = inter_h * (inter_h >= 0)

    intersection = inter_w * inter_h

    a_area = a.w * a.h
    b_area = b.w * b.h

    iou = intersection / (a_area + b_area - intersection)

    if np.isinf(iou) or np.isnan(iou):
        iou = 0

    return iou






