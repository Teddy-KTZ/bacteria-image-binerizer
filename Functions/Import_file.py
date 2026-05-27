import customtkinter as ctk
from tkinter import filedialog


def import_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tif")])
    return file_path