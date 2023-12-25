import json
from pathlib import Path

def filter_panoptic_annotations(input_path, output_path, category_ids_to_keep):
    with open(input_path, 'r') as json_file:
        panoptic_data = json.load(json_file)

    new_images = []
    new_annotations = []
    annotations_per_category = {}
    new_images_id = []
    counter = 0

    for image in panoptic_data['images']:
        image_id = image['id']
        for annotation in panoptic_data['annotations']:
          if image_id == annotation['image_id']:
            if image['width'] == 640 and image['height'] == 480:        #to filter the image size, comment if you don't want to filter image size
              if image_id not in new_images_id:
                new_images_id.append(image_id)
                categories_in_img = []
                
                for annk in annotation['segments_info']:
                    cat_in_img = annk['category_id']
                    categories_in_img.append(cat_in_img)
                print('categories in image info:', categories_in_img)

                checker = []
                for check in categories_in_img:
                   if check in category_ids_not_to_keep:
                      checker.append(1)
                n = 1
                for ann in annotation['segments_info']:
                  if n not in checker:
                    print('OK!')
                    if ann['category_id'] in category_ids_to_keep:
                      if ann['category_id'] not in annotations_per_category:
                        annotations_per_category[ann['category_id']] = 0
                      if annotations_per_category[ann['category_id']] <= max_annotations_per_category:
                        counter += 1
                        annotations_per_category[ann['category_id']] += 1
                  else:
                     print('NOT OK!')
                categories_in_img = []
                checker = []
                if(counter > 0):
                  new_annotations.append(annotation)
                  print("annotations appended")
                  counter = 0
              if image not in new_images:
                new_images.append(image)
                print("Image info appended")
                  
    new_panoptic_data = {
        'info': panoptic_data['info'],
        'licenses': panoptic_data['licenses'],
        'images': new_images,
        'annotations': new_annotations,
        'categories': panoptic_data['categories']
    }

    with open(output_path, 'w') as output_file:
        json.dump(new_panoptic_data, output_file)

if __name__ == "__main__":
    input_json_path = Path("panoptic_train2017.json")                   #the full json annotation
    output_json_path = Path("train_indoor_dataset_filtered2.json")      #the filtered json annotation
    category_ids_to_keep = [1, 11, 27, 31, 44, 47, 48, 49, 50, 51,
                            72, 73, 74, 76, 77, 84, 86, 107, 118, 122,
                             133, 171, 175, 176, 177, 186, 190]
    category_ids_not_to_keep = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
                                13, 14, 15, 16, 17, 18, 19, 20,
                                21, 22, 23, 24, 25, 28, 32, 33,
                                34, 35, 36, 37, 38, 39, 40, 41,
                                42, 43, 46, 52, 53, 54, 55, 56,
                                57, 58, 59, 60, 61, 75, 92, 95,
                                128, 138, 144, 145, 147, 148,
                                149, 151, 154, 155, 156, 159,
                                166, 178, 184, 185, 187, 191, 192,
                                193, 194, 197, 198]

    max_annotations_per_category = 700
    filter_panoptic_annotations(input_json_path, output_json_path, category_ids_to_keep)
