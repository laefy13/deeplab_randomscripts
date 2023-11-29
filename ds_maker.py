import os


with open('dataset.txt','w') as file:
    for root,dir,files in os.walk('datasets/VOCdevkit/VOC2012/SegmentationClass/'):
        for f in files:
            if str(f).endswith('.bmp'):
                print(f)
                continue
            write_this = f'{f[:-4]}\n'
            file.write(write_this)
        


import sep_this