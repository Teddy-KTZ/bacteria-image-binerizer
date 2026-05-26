from tifffile import TiffFile, imwrite
import numpy as np

def save_bin(stack_fluo_bin, filename):
    # Save the binarized stack as a new TIFF file
    output_filename = filename.replace('.tif', '_bin.tif')
    imwrite(output_filename, stack_fluo_bin)
    print(f"Binarized stack saved as {output_filename}")

    