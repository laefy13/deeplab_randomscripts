from PIL import Image
import os
def bmp_to_png(input_path, output_path):
    # Open BMP image
    bmp_image = Image.open(input_path)

    # Save as PNG
    bmp_image.save(output_path, "PNG")

# Example usage

for root,dir,files in os.walk('datasets/mask1'):
    for file in files:
        og_path = root+ '/' + file
        nahh = f'datasets/VOCdevkit/VOC2012/SegmentationClass/{file[:-3]}png'
        # print(nahh)
        # exit()
        bmp_to_png(og_path, nahh)
