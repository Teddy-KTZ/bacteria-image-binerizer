import numpy as np
from tifffile import imread, imwrite, TiffFile
from skimage.filters import threshold_otsu
from skimage.util import img_as_ubyte
import pandas as pd

def binerize(filename):

    stack = imread(filename)

    stack_fluo = stack[:, :, 0, :, :]
    stack_fluo_bin = np.zeros_like(stack_fluo, dtype=np.uint8)

    for i in range(stack_fluo.shape[0]):
        for j in range(stack_fluo.shape[1]):

            im = stack_fluo[i, j, : , :]
            thresh = threshold_otsu(im)
            bin_im = im > thresh
        
            bin_im = img_as_ubyte(bin_im)  # Convert to uint8 for saving
            stack_fluo_bin[i, j, :, :] = bin_im
        print(f"Processed frame {i+1}/{stack_fluo.shape[0]}")
    
    return stack_fluo_bin