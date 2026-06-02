# Welcome to the bacteria-image_binarizer repository

In this repository, tou can find an image binarizer. 

This work is primary made for bacterial study made in the TakeuchiLab (https://lab.kaztake.org/takeuchi.html)

## Needed libraries 

To be sure the code is running well, please be sure the following libraries are installed on your computer and that python can call them : 
- Numpy
- Matplotlib
- Pandas
- CustomTkinter
- Tkinter
- Tifffile
- Skimage (Scikit-image)

To know if these libraries are installed, in your terminal type `python -V` to access the python version then, `python` and when you enter in the python environment, please test all libraries by the command `import XXlibraryXX`. 

## What this GUI App does for the moment

This GUI App is made to binarize tiff images already croped and centered with Fiji (ImageJ). It sould take an 5D image (t, Z, channel, X, Y) and display it. Click on 'RUN BINARIZATION' to apply a Otsu threshold and see the result next to the original image. You can navigate in Z and t positions. 

## Details : How it works

This section will be updated soon... 

## Inputs / Outputs 

Inputs : Take a 5D image (t, Z, channel, X, Y). The fluorescent channel needs to be the first one. If images shape is different, plese reach out for bug correction. 
Outputs : Give a 4D binarized image (t, Z, X, Y). A Otsu Threshold is applied here. The image is saved as *"Your_file_name_bin.tif"* If it's not relevant or not accurate, please reach out for bug correction.