import shutil
import os
import json

origin = 'train_full/'              #directory of the full version of png annotation
target = 'panoptic_train2017/'        #directory of the filtered version of png annotation

files_ori = os.listdir(origin)
filenames=[]

with open('train_indoor_dataset_filtered2.json', 'r') as json_file:     #filtered json annotation
    panoptic_data = json.load(json_file)

for annotation in panoptic_data['annotations']:
    filename = annotation['file_name']
    filenames.append(filename)

print(filenames)

for file in files_ori:
    if file in filenames:
        shutil.copy2(origin+file, target+file)
print("Files copied succesfully")