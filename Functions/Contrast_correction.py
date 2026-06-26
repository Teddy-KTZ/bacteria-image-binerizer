## 
## This part of the code corresponding to the correction of fluorescent default has been made by Iris Dauchot (McGill University)



import numpy as np
import matplotlib.pyplot as plt
import tifffile as tiff
import os
from skimage import io
import cv2


def correct_tiff_4d(input_tiff, blur_kernel_size=51):     # ensure blur_kernel_size is odd

    if blur_kernel_size % 2 == 0:
        blur_kernel_size += 1

    with tiff.TiffFile(input_tiff) as tif:
        data = tif.asarray(out='memmap')
        if len(data.shape)==5 : 
            T, Z, C, Y, X = data.shape
            axes = "TZCYX"
        else : 
            T, Z, Y, X = data.shape
            axes = "TZCYX"
        
        print(f"Input shape: {data.shape}")

        corrected_data = np.empty_like(data)

        for t in range(T):
            for z in range(Z):
                img = data[t, z].astype(np.float32)

                # flat-field correction
                background = cv2.GaussianBlur(img, (blur_kernel_size, blur_kernel_size), 0)
                mean_bg = background.mean()
                corrected = img*(mean_bg/(background + 1))
                corrected_data[t, z] = np.clip(corrected, 0, np.iinfo(data.dtype).max).astype(data.dtype)

            print(f"Processed T={t+1}/{T}")

        with tiff.TiffWriter(input_tiff+"_corrected", bigtiff=True, ome=True) as writer:
            writer.write(corrected_data, photometric='minisblack', metadata={"axes": axes})

    print("Done: saved TZYX file")

