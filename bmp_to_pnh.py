from PIL import Image
import os
import shutil
def bmp_to_png(input_path, output_path):
    # Open BMP image
    bmp_image = Image.open(input_path)

    # Save as PNG
    bmp_image.save(output_path, "PNG")

# Example usage

if not os.path.exists('datasets/VOCdevkit/VOC2012/SegmentationClass/'):
  os.makedirs('datasets/VOCdevkit/VOC2012/SegmentationClass/')
for root,dir,files in os.walk('TongeImageDataset/groundtruth/mask1'):
    for file in files:
        og_path = root+ '/' + file
        nahh = f'datasets/VOCdevkit/VOC2012/SegmentationClass/{file[:-3]}png'
        bmp_to_png(og_path, nahh)



if not os.path.exists('datasets/VOCdevkit/VOC2012/ImageSets/Segmentation/'):
  os.makedirs('datasets/VOCdevkit/VOC2012/ImageSets/Segmentation/')
shutil.copy2('./val.txt','datasets/VOCdevkit/VOC2012/ImageSets/Segmentation/val.txt' )
shutil.copy2('./train.txt','datasets/VOCdevkit/VOC2012/ImageSets/Segmentation/train.txt' )