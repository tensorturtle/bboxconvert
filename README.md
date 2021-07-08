# bboxconvert <br /> ⛶🠺🞖
Minimal library to convert between unrotated rectangular bounding box annotation formats.

## Installation

Install with pip:
```
pip install bboxconvert==0.1.0
```

## Usage

There are two ways to use this library:
1. Refer to [popular format shortcuts](#shortcut-functions-for-popular-formats) to find relevant function.
2. Directly use the [basic transformations](bboxconvert/elements.py). See example below.

### Common Bounding Box Formats

|                	|               Range              	|           Coordinates Format          	|
|--------------:	|:--------------------------------:	|:-------------------------------------:	|
|      **YOLO**      	|         Normalized [0,1]         	| `[ x_Center, y_Center, width, height ]` 	|
|      **COCO**      	| Pixels [0, width] or [0, height] 	|    `[ x_min, y_min, width, height ]`    	|
|   **PASCAL_VOC**   	| Pixels [0, width] or [0, height] 	|     `[ x_min, y_min, x_MAX, y_MAX ]`    	|
| **Albumentations** 	|         Normalized [0,1]         	|     `[x_min, y_min, x_MAX, y_MAX ]`    	|

### Shortcut Functions for Popular Formats

| from (column) to (row) 	| YOLO           	| COCO           	| PASCAL_VOC    	| Albumentations 	|
|------------------------:|:---------------:|:---------------:|:--------------: |:---------------:|
| **YOLO**                  	| 🌸              	| `yolo_to_coco()` 	| `yolo_to_voc()` 	| `yolo_to_A()`      	|
| **COCO**                   	| `coco_to_yolo()` 	| 🌸              	| `coco_to_voc()` 	| `coco_to_A()`      	|
| **PASCAL_VOC**            	| `voc_to_yolo()`  	| `voc_to_coco()`  	| 🌸             	| `voc_to_A()`     	|
| **Albumentations**         	| `A_to_yolo()`    	| `A_to_coco()`    	| `A_to_voc()`    	| 🌸              	|

### Example

#### Converting from PASCAL_VOC to YOLO (popular formats)
```python3
from bboxconvert.bboxconvert import *

voc_box = [310,200,350,290] # PASCAL_VOC format
coco_box = voc_to_coco(voc_box) 
```

#### Directly using the normalization function

The basic transformations are available in `bboxconvert.elements`

```python3
from bboxconvert.elements import xyXY_to_xywh, normalize

xyxy_box = [310, 200, 350, 290] # xyxy format
width = 1280 # pixels
height = 720 # pixels
xywh_box = xyXY_to_xywh(xyxy_box)
norm_xywh_box = normalize(xywh_box, width, height)
```


## Implementation Summary

Under the hood, the shortcuts are compositions of simpler functions.
where 
+ `c` = coordinates [a,b,c,d] where a,c are horizontal-related, and b,d are vertical-related
+ `w` = width in pixels
+ `h` = height in pixels

| from (column) to (row) 	|                       YOLO                       	|                        COCO                       	|              PASCAL_VOC              	|          Albumentations          	|
|----------------------:	|:------------------------------------------------:	|:-------------------------------------------------:	|:------------------------------------:	|:--------------------------------:	|
|               **YOLO** 	| 🌸                                                	| `denormalize(xyXY_to_xywh(xCyCwh_to_xyXY(c)),w,h)` 	| `denormalize(xCyCwh_to_xyXY(c),w,h)` 	| `xCyCwh_to_xyXY(c)`              	|
|               **COCO** 	| `normalize(xyXY_to_xCyCwh(xywh_to_xyXY(c)),w,h)` 	| 🌸                                                 	| `xywh_to_xyXY(c)`                    	| `normalize(xywh_to_xyXY(c),w,h)` 	|
|         **PASCAL_VOC** 	| `normalize(xyXY_to_xCyCwh(c),w,h)`               	| `xyXY_to_xywh(c)`                                 	| 🌸                                    	| `normalize(c,w,h)`               	|
|     **Albumentations** 	| `xyXY_to_xCyCwh(c)`                              	| `denormalize(xyXY_to_xywh(c),w,h)`                	| `denormalize(c,w,h)`                 	| 🌸                                	|
