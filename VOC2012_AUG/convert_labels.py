#!/usr/bin/env python
#Martin Kersner, m.kersner@gmail.com
#2016/01/25

from __future__ import print_function
import os
import sys
import numpy as np
from skimage.io import imread, imsave

path = "./VOC2012_AUG/VOC2012_orig/SegmentationClass/"
txt_file = "./VOC2012_AUG/VOC2012_orig/ImageSets/Segmentation/trainval.txt"
path_converted = "./VOC2012_AUG/VOC2012_orig/SegmentationClass_1D_new"
def pascal_palette():
  palette = {(  0,   0,   0) : 0 ,
             (128,   0,   0) : 1 ,
             (  0, 128,   0) : 2 ,
             (128, 128,   0) : 3 ,
             (  0,   0, 128) : 4 ,
             (128,   0, 128) : 5 ,
             (  0, 128, 128) : 6 ,
             (128, 128, 128) : 7 ,
             ( 64,   0,   0) : 8 ,
             (192,   0,   0) : 9 ,
             ( 64, 128,   0) : 10,
             (192, 128,   0) : 11,
             ( 64,   0, 128) : 12,
             (192,   0, 128) : 13,
             ( 64, 128, 128) : 14,
             (192, 128, 128) : 15,
             (  0,  64,   0) : 16,
             (128,  64,   0) : 17,
             (  0, 192,   0) : 18,
             (128, 192,   0) : 19,
             (  0,  64, 128) : 20 }

  return palette

def convert_from_color_segmentation(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)
    palette = pascal_palette()

    for c, i in palette.items():
        m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
        arr_2d[m] = i

    return arr_2d


def main():
    ##
    ext = '.png'

    # Create dir for converted labels
    if not os.path.isdir(path_converted):
        os.makedirs(path_converted)

    with open(txt_file, 'rb') as f:
        for img_name in f:
            img_base_name = img_name.strip()
            img_base_name = img_base_name.decode()
            img_name = os.path.join(path, img_base_name) + ext
            img = imread(img_name)
            #img = cv2.imread(img_name)

            if (len(img.shape) > 2):
                img = convert_from_color_segmentation(img)
                imsave(os.path.join(path_converted, img_base_name) + ext, img)
            else:
                print(img_name + " is not composed of three dimensions, therefore " 
                "shouldn't be processed by this script.\n"
                "Exiting." , file=sys.stderr)
                exit()

if __name__ == '__main__':
    main()
