import json
from pathlib import Path

def filter_instance_annotations(input_path, output_path, reference_path):
    # Load the panoptic annotation JSON file
    with open(reference_path, 'r') as json_file:
        panoptic_data = json.load(json_file)

    with open(input_path, 'r') as json_file:
        instance_full = json.load(json_file)

    # Filter category IDs
    new_images_in = []
    new_annotations_in = []
    new_images_in_id = []
    new_categories_in = []

    for image in panoptic_data['images']:
       image_id = image['id']
       for image_in in instance_full['images']:
          image_in_id = image_in['id']
          if image_in_id == image_id:
            new_images_in_id.append(image_in_id)
            if image_in not in new_images_in:
                new_images_in.append(image_in)
            continue


    
    for annotations_in in instance_full['annotations']:
       img_id = annotations_in['image_id']
       if img_id in new_images_in_id:
          new_annotations_in.append(annotations_in)

    for categories_in in panoptic_data['categories']:
       cat_isthing = categories_in['isthing']
       if cat_isthing == 1:
          new_categories_in.append(categories_in)    

    # Create new panoptic annotation data
    new_instance_data = {
        'info': panoptic_data['info'],
        'licenses': panoptic_data['licenses'],
        'images': new_images_in,
        'annotations': new_annotations_in,
        'categories': new_categories_in
    }

    # Save the filtered panoptic annotation JSON to a new file
    with open(output_path, 'w') as output_file:
        json.dump(new_instance_data, output_file)

if __name__ == "__main__":
    input_json_path = Path("instances_train2017_full.json")         #the full instance json annotation
    output_json_path = Path("instances_train2017.json")             #the filtered instance json annotation
    reference_path = Path("panoptic_train2017.json")                #the filtered panoptic json annotation

    filter_instance_annotations(input_json_path, output_json_path, reference_path)
