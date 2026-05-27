import customtkinter as ctk

from Functions.Import_file import import_file
from Functions.Binerize import binerize
from Functions.Save_bin import save_bin

from GUI.Panel import ButtonPanel, ImagePanel, EntryPanel


class Application(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Image Binarization")
        self.geometry("400x200")
        
        self.Z = 0
        self.t = 0
        self.alpha = 0.95

        self.import_button = ButtonPanel(self, command=self.import_button_click, text="Import TIFF file")
        self.erase_button = ButtonPanel(self, command=self.erase_figure, text="Erase figure")

        self.Z_entry = EntryPanel(self, default=self.Z)
        self.alpha_entry = EntryPanel(self, default=self.alpha)    
        self.t_entry = EntryPanel(self, default=self.t)
        #self.wildth_entry = EntryPanel(self, default=self.wildth)
        self.actualize_button = ButtonPanel(self, command=lambda: self.actualize_figure(Z=int(self.Z_entry.entry_var.get()), t=int(self.t_entry.entry_var.get())), text="Actualize figure")
        self.run_button = ButtonPanel(self, command=self.run_binarize, text="Run Binarization")
        

        ## Placing everything thanks to grid
        grid_config = {"padx": 10, "pady": 10}


        self.import_button.grid(row=0, column=0, padx=10, pady=10)
        self.erase_button.grid(row=0, column=1, padx=10, pady=10)
        self.Z_entry.grid(row=1, column=0, padx=10, pady=10)
        self.alpha_entry.grid(row=1, column=1, padx=10, pady=10)
        self.t_entry.grid(row=2, column=0, padx=10, pady=10)
        
        self.actualize_button.grid(row=3, column=0, padx=10, pady=10)
        self.run_button.grid(row=3, column=2, padx=10, pady=10)













    def figure_generation(self):

        self.figure_panel = ImagePanel(self, image_path=self.file_path, Z=self.Z, t=self.t)
        print(self.figure_panel)
        self.figure_panel.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
        print(f"Figure generated for file: {self.file_path} with Z={self.Z} and t={self.t}")        

    def import_button_click(self):
        self.file_path = import_file(self)
        if self.file_path:
            self.figure_generation()
            print(f"File imported: {self.file_path}")


    def run_binarize(self, file_path):
        file_path = self.file_path
        if file_path:
            self.binarized_image = binerize(file_path)
            save_bin(self.binarized_image)
            self.show_binarized_image()
        
    def actualize_figure(self, Z, t):
        self.Z = Z
        self.t = t
        self.figure_panel._render(self.Z, self.t)
        print(f"Actualized figure with Z={self.Z} and t={self.t}")

    def erase_figure(self):
        file_path = None
        actualize_figure(self, Z=0, t=0)