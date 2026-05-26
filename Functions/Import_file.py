import customtkinter as ctk
from tkinter import filedialog


def import_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tif")])
    if file_path:
        self.file_path = file_path