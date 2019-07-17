#!/usr/bin/env python
# Martin Kersner, m.kersner@gmail.com
# 2016/03/17

from __future__ import print_function
import os
import glob
import scipy.io
from PIL import Image as PILImage
input_path = "./VOC2012_AUG/VOC_aug/dataset/cls/"
output_path = "./VOC2012_AUG/VOC_aug/dataset/cls_png/"

# Mat to png conversion for http://www.cs.berkeley.edu/~bharath2/codes/SBD/download.html
# 'GTcls' key is for class segmentation
# 'GTinst' key is for instance segmentation
def mat2png_hariharan(mat_file, key='GTcls'):
    mat = scipy.io.loadmat(mat_file, mat_dtype=True, squeeze_me=True, struct_as_record=False)
    return mat[key].Segmentation

def main():
    mat_files = glob.glob(os.path.join(input_path, '*.mat'))
    convert_mat2png(mat_files, output_path)


def convert_mat2png(mat_files, output_path):
    if not mat_files:
        help('Input directory does not contain any Matlab files!\n')

    for mat in mat_files:
        numpy_img = mat2png_hariharan(mat)
        pil_img = PILImage.fromarray(numpy_img)
        pil_img.save(os.path.join(output_path, modify_image_name(mat, 'png')))

# Extract name of image from given path, replace its extension with specified one
# and return new name only, not path.
def modify_image_name(path, ext):
    return os.path.basename(path).split('.')[0] + '.' + ext


if __name__ == '__main__':
    main()
