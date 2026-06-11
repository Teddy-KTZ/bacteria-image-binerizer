# Welcome to the bacteria-image_binarizer repository

In this repository, you can find an image binarizer.

This work is primarily made for bacterial studies made in the TakeuchiLab (https://lab.kaztake.org/takeuchi.html)

## Needed libraries

To be sure the code is running well, please be sure the following libraries are installed on your computer and that Python can call them :
- Numpy
- Matplotlib
- Pandas
- CustomTkinter
- Tkinter
- Tifffile
- Skimage (Scikit-image)

To know if these libraries are installed, in your terminal type `python -V` to access the Python version then, `python` and when you enter in the Python environment, please test all libraries with the command `import XXlibraryXX`.

## What this GUI App does for the moment

This GUI App is made to binarize TIFF images already cropped and centered with Fiji (ImageJ). It should take a 5D image (t, Z, channel, X, Y) and display it. Click on 'RUN BINARIZATION' to apply an Otsu threshold and see the result next to the original image. You can navigate in Z and t positions.

## Details : How it works

### Image preparation - Fiji (ImageJ)

Bacteria Analyzer needs a 5D image as a .tiff format. The image needs to be cleared from any X/Y drift or any unused area.

To do so, on Fiji, turn your .lif image to a .tiff by making it horizontal (Image>Transform>Rotate) and crop (Ctrl+Shift+X) it with a rectangle to keep a 20 pixel dark border (it allows you to keep information even if there is a bit of X/Y drift due to heat/vibration).

Once your image is well oriented and cropped, save it as a TIFF file. (File>Save As...). Name it the way you want, but keep in mind you will need to remember the position of your image compared to your sample.

### Image binarization

In a terminal or directly in your favorite IDE (VSCode...), reach the current Python code folder with the `cd` command. For example : if the file is in `home/download/bacteria-image_binarizer`, type the following command `cd home/download/bacteria-image_binarizer`.

Run the program with Python with the command `python main.py`. Import your .tif image by clicking on the **Import File** button. The image should display automatically within 30 seconds (1 minute for first use).

You can navigate in Z planes and time t with the sliders. Further improvements would be to display the current plane/time number over the total number. Click on **RUN Binarization** to binarize the stack with an Otsu threshold. The result should be displayed automatically.

*Note : The current step of processing is displayed as a print function, it should appear in your terminal as `Time XX/N treated`*

You can still navigate in Z planes and time t with the sliders and compare your binarization. The binarized image is automatically saved in the same folder as your original file with the suffix *"_bin"* added.


## Inputs / Outputs

Inputs : Takes a 5D image (t, Z, channel, X, Y). The fluorescent channel needs to be the first one. If the image shape is different, please reach out for bug correction.
Outputs : Gives a 4D binarized image (t, Z, X, Y). An Otsu threshold is applied here. The image is saved as *"Your_file_name_bin.tif"*. If it is not relevant or not accurate, please reach out for bug correction.