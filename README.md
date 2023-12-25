Before you can run the program, you need to download the 2017 Panoptic train/val annotations zip file in the [COCO website] (https://cocodataset.org/#download).

To use the filter, follow this following steps:
1. Run 'panoptic_filter.py' to filter the json annotation based on image size, categories to keep, and categories not to keep.
2. Run 'get_image_id.py' to download images data from COCO based on the information of the filtered json annotation, without needing to download the full images data.
3. Run 'copy_ann_png.py' to copy png annotations from the full version of png annotations folder to the filtered folder based on the information of the filtered json annotation.

**Optional:**
Some panoptic architecure needs json annotation for instance segmentation. Therefore you have to download the 2017 train/val annotations, then you can run 'instance_filter.py', which is to filter instance json annotation based on the filtered panoptic json annotation.
