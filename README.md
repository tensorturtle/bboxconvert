# bboxconvert
Minimal library to convert between unrotated rectangular bounding box annotation formats.

Supports python list, numpy array, and pytorch tensor.

## Common Bounding Box Format Specifications

|                	|               Range              	|           Coordinates Format          	|
|--------------:	|:--------------------------------:	|:-------------------------------------:	|
|      **YOLO**      	|         Normalized [0,1]         	| [ x_Center, y_Center, width, height ] 	|
|      **COCO**      	| Pixels [0, width] or [0, height] 	|    [ x_min, y_min, width, height ]    	|
|   **PASCAL_VOC**   	| Pixels [0, width] or [0, height] 	|     [ x_min, y_min, x_MAX, y_MAX ]    	|
| **Albumentations** 	|         Normalized [0,1]         	|     [ x_min, y_min, x_MAX, y_MAX ]    	|

## Shortcut Conversions Between Popular Dataset Formats

| from (column) to (row) 	| YOLO           	| COCO           	| PASCAL_VOC    	| Albumentations 	|
|------------------------:|:---------------:|:---------------:|:--------------: |:---------------:|
| **YOLO**                  	| 🌸              	| yolo_to_coco() 	| yolo_to_voc() 	| yolo_to_A()      	|
| **COCO**                   	| coco_to_yolo() 	| 🌸              	| coco_to_voc() 	| coco_to_A()      	|
| **PASCAL_VOC**            	| voc_to_yolo()  	| voc_to_coco()  	| 🌸             	| voc_to_A()     	|
| **Albumentations**         	| A_to_yolo()    	| A_to_coco()    	| A_to_voc()    	| 🌸              	|

## Implementation

| from (column) to (row) 	|                       YOLO                       	|                        COCO                       	|              PASCAL_VOC              	|          Albumentations          	|
|:----------------------:	|:------------------------------------------------:	|:-------------------------------------------------:	|:------------------------------------:	|:--------------------------------:	|
|               **YOLO** 	| 🌸                                                	| `denormalize(xyXY_to_xywh(xCyCwh_to_xyXY(c),w,h)` 	| `denormalize(xCyCwh_to_xyXY(c),w,h)` 	| `xCyCwh_to_xyXY(c)`              	|
|               **COCO** 	| `normalize(xyXY_to_xCyCwh(xywh_to_xyXY(c)),w,h)` 	| 🌸                                                 	| `xywh_to_xyXY(c)`                    	| `normalize(xywh_to_xyXY(c),w,h)` 	|
|         **PASCAL_VOC** 	| `normalize(xyXY_to_xCyCwh(c),w,h)`               	| `xyXY_to_xywh(c)`                                 	| 🌸                                    	| `normalize(c,w,h)`               	|
|     **Albumentations** 	| `xyXY_to_xCyCwh(c)`                              	| `denormalize(xyXY_to_xywh(c),w,h)`                	| `denormalize(c,w,h)`                 	| 🌸                                	|
