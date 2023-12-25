from pycocotools.coco import COCO

coco_train = COCO('annotations/train_indoor_dataset_filtered2.json')    #filtered json annotation
cats_id=  [1, 11, 27, 31, 44, 47, 48, 49, 50, 51,                       #categories id to keep
            72, 73, 74, 76, 77, 84, 86, 107, 118, 122,
            133, 171, 175, 176, 177, 186, 190]
for cat in cats_id:
    print('category id: ', cat)
    coco_img_ids = coco_train.getImgIds(imgIds=[], catIds=[cat])
    if coco_img_ids == []:
        print('no images for this category')
    else:
        print("imgs ids:", coco_img_ids)
        print("len of imgs ids:", len( coco_img_ids))
        COCO.download(coco_train,tarDir='train2017',imgIds=coco_img_ids)    #downloading images based on the informations in filtered json annotation only,
                                                                            #saved within tarDir directory