
import customtkinter as ctk

class ButtonPanel(ctk.CTkFrame):
    def __init__(self, master=None, command=None, text=None, **kwargs):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(command, text=text, **kwargs)

    def create_widgets(self, command=None, **kwargs):
        self.import_button = ctk.CTkButton(self, command=command, **kwargs)
        self.import_button.pack()

class FigurePanel(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self, im1, im2, **kwargs):
        self.fig, self.axes = plt.subplots(1, 2, figsize=(10, 5), **kwargs)
        self.axes[0].imshow(im1, cmap='gray')
        self.axes[0].set_title("Original image")

        self.axes[1].imshow(im2, cmap='gray')
        self.axes[1].set_title("Binarized image")
