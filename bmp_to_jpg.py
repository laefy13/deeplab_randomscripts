from PIL import Image
import os
def bmp_to_jpg(input_path, output_path):
    # Open BMP image
    bmp_image = Image.open(input_path)

    # Save as JPG
    bmp_image.convert("RGB").save(output_path, "JPEG")

# Example usage

for root,dir,files in os.walk('datasets/mask1'):
    for file in files:
        og_path = root+ '/' + file
        nahh = f'datasets/VOCdevkit/VOC2012/SegmentationClass/{file[:-3]}jpg'
        # print(nahh)
        # exit()
        bmp_to_jpg(og_path, nahh)
