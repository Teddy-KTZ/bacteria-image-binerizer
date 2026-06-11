import customtkinter as ctk
import tifffile as tifffile

from Functions.Import_file import import_file
from Functions.Binerize import binerize
from Functions.Save_bin import save_bin

from GUI.Panel import ButtonPanel, ImagePanel, EntryPanel, LabelPanel, SliderPanel


class Application(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Image Binarization")
        self.geometry("400x200")
        self.file_path = None
        self.Z = 0
        self.t = 0
        self.alpha = 0.5

        self.Z_to = 0
        self.t_to = 0

        self.import_button = ButtonPanel(self, command=self.import_button_click, text="Import TIFF file")
        self.erase_button = ButtonPanel(self, command=self.erase_figure, text="Erase figure")

        self.Z_slider = SliderPanel(self, from_=0, to=2, command=self.update_Z, label="Z")   
        self.t_slider = SliderPanel(self, from_=0, to=2, command=self.update_t, label="t")


        #self.wildth_entry = EntryPanel(self, default=self.wildth)
        
        self.run_button = ButtonPanel(self, command=self.run_binarize, text="Run Binarization")
        self.info_button = ButtonPanel(self, command=self._show_info, text="Show info")

        ## Placing everything thanks to grid
        grid_config = {"padx": 10, "pady": 10}


        self.import_button.grid(row=0, column=0, padx=10, pady=10)
        self.erase_button.grid(row=0, column=1, padx=10, pady=10)
        self.Z_slider.grid(row=1, column=1, padx=10, pady=10)
        self.t_slider.grid(row=2, column=1, padx=10, pady=10)
        self.run_button.grid(row=3, column=2, padx=10, pady=10)
        self.info_button.grid(row=5, column=0, padx=10, pady=10)



    def update_Z(self, value):
        self.Z = int(float(value))
        self.actualize_figure()


    def update_t(self, value):
        self.t = int(float(value))
        self.actualize_figure()


    def figure_generation(self):

        self.figure_panel = ImagePanel(self, image_path=self.file_path, Z=self.Z, t=self.t)
        print(self.figure_panel)
        self.figure_panel.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
        self.Z_slider.slider.configure(to=self.Z_to)
        self.t_slider.slider.configure(to=self.t_to)
        self.Z_slider.slider.set(self.Z)
        self.t_slider.slider.set(self.t)
                

    def import_button_click(self):
        self.file_path = import_file(self)
        if self.file_path:
            self.stack = tifffile.imread(self.file_path)
            self.Z_to = self.stack.shape[1] - 1
            self.t_to = self.stack.shape[0] - 1
            self.figure_generation()
            print(f"File imported: {self.file_path}")


    def run_binarize(self):
        file_path = self.file_path
        if file_path:
            self.binarized_image = binerize(file_path)
            save_bin(self.binarized_image, self.file_path)
            self.figure_panel.show_binarized_image(bin_image=self.binarized_image, t=self.t, Z=self.Z)
        
    def actualize_figure(self):
        self.figure_panel._render(self.Z, self.t) 

    def erase_figure(self):
        file_path = None
        self.figure_panel.destroy()
        print("Figure erased.")

    def _show_info(self):
        info_text = f"Current file: {self.file_path}\nCurrent Z: {self.Z}\nCurrent t: {self.t}"
        print(info_text)
    
