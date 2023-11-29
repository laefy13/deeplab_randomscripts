from PIL import Image
import os
def bmp_to_jpg(input_path, output_path):
    # Open BMP image
    bmp_image = Image.open(input_path)

    # Save as JPG
    bmp_image.convert("RGB").save(output_path, "JPEG")

# Example usage
if not os.path.exists('datasets/VOCdevkit/VOC2012/JPEGImages/'):
  os.makedirs('datasets/VOCdevkit/VOC2012/JPEGImages/')
for root,dir,files in os.walk('TongeImageDataset/groundtruth/images'):
    for file in files:
        og_path = root+ '/' + file
        nahh = f'datasets/VOCdevkit/VOC2012/JPEGImages/{file[:-3]}jpg'
        bmp_to_jpg(og_path, nahh)
