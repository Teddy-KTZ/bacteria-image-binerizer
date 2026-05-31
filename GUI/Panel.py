
import customtkinter as ctk
import tifffile as tifffile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class EntryPanel(ctk.CTkFrame) : 
    
    def __init__(self, master, default=0, **kwargs):
        super().__init__(master, **kwargs)
        self.entry_var = ctk.StringVar(value=str(default))
        ctk.CTkEntry(self, 
                     bg_color="transparent", 
                     textvariable=self.entry_var).pack()

class ButtonPanel(ctk.CTkFrame):
    def __init__(self, master=None, command=None, text=None, **kwargs):
        super().__init__(master)
        self.master = master
        self.create_widgets(command, text=text, **kwargs)

    def create_widgets(self, command=None, **kwargs):
        self.import_button = ctk.CTkButton(self, command=command, **kwargs)
        self.import_button.pack()

class LabelPanel(ctk.CTkFrame):
    def __init__(self, master=None, text=None, **kwargs):
        super().__init__(master)
        self.master = master
        self.create_widgets(text=text, **kwargs)

    def create_widgets(self, text=None, **kwargs):
        self.label = ctk.CTkLabel(self, text=text, **kwargs)
        self.label.pack()

class SliderPanel(ctk.CTkFrame):
    def __init__(self, master=None, from_=0, to=100, command=None, **kwargs):
        super().__init__(master)
        self.master = master
        self.create_widgets(from_, to, command, **kwargs)

    def create_widgets(self, from_, to, command=None, **kwargs):
        self.slider = ctk.CTkSlider(self, from_=from_, to=to, command=command, **kwargs)
        self.slider.pack(fill="x", expand=True)



class ImagePanel(ctk.CTkFrame):

    def __init__(self, master, image_path=None, Z=0, t=0, **kwargs):
        super().__init__(master, **kwargs)
        self.Z = Z
        self.t = t
        self.stack = tifffile.imread(image_path) if image_path else None
        
        if self.stack is None : 
            print("No image stack loaded.")
        else :
            # Construction unique de la figure et du canvas
            self.fig, self.ax = plt.subplots(figsize=(8,8))
            self.fig.tight_layout(pad=0)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)

            print(f"ImagePanel initialized with image_path: {image_path}, Z: {Z}, t: {t}")

            self._render(self.Z, self.t)  # premier rendu

    def _render(self, Z, t):
        """Efface et redessine selon self.channels."""
        if self.stack is None:
            print("No image stack to render.")
            self.ax.clear()
            self.ax.text(0.5, 0.5, "No image loaded", ha="center", va="center", fontsize=12)
            self.ax.axis("off")
            self.canvas.draw()
            return
        else :
            print("AAAAAAAA")
            self.Z = Z
            self.t = t
            self.ax.clear()
            self.ax.axis("off")
            print(self.stack.shape)
            print(len(self.stack.shape))
            if len(self.stack.shape) < 5:
                img = self.stack[self.t, self.Z, :, :]
            else : 
                img = self.stack[self.t, self.Z, 0, :, :]

            self.ax.imshow(img, cmap="gray")


            self.fig.tight_layout(pad=0)
            self.canvas.draw()
            print(f"Rendered image for Z={self.Z} and t={self.t}")

