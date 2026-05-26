import customtkinter as ctk

from Functions.Import_file import import_file
from Functions.Binerize import binerize
from Functions.Save_bin import save_bin

from GUI.Panel import ButtonPanel, FigurePanel


class Application(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Image Binarization")
        self.geometry("400x200")

        self.import_button = ButtonPanel(self, command=import_file, text="Import TIFF file")
        self.import_button.pack(pady=20)
        
        
