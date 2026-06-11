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
    def __init__(self, master=None, from_=0, to=100, command=None, label="", **kwargs):
        super().__init__(master)
        self.master = master
        self.label_text = label
        self.create_widgets(from_, to, command, **kwargs)

    def create_widgets(self, from_, to, command=None, **kwargs):
        self.value_label = ctk.CTkLabel(self, text=f"{self.label_text}: 0")
        self.value_label.pack()
        self.slider = ctk.CTkSlider(self, from_=from_, to=to, command=self._on_slide, **kwargs)
        self.slider.pack(fill="x", expand=True)
        self._external_command = command

    def _on_slide(self, value):
        self.value_label.configure(text=f"{self.label_text}: {int(float(value))}")
        if self._external_command:
            self._external_command(value)



class ImagePanel(ctk.CTkFrame):

    def __init__(self, master, image_path=None, Z=0, t=0, **kwargs):
        super().__init__(master, **kwargs)
        
        self.number_plot = 1
        self.Z = Z
        self.t = t
        self.stack = tifffile.imread(image_path) if image_path else None
        
        if self.stack is None : 
            print("No image stack loaded.")
        else :
            # Construction unique de la figure et du canvas
            self.fig, self.ax = plt.subplots(figsize=(8,4))
            self.fig.tight_layout(pad=0)
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)

            print(f"ImagePanel initialized with image_path: {image_path}, Z: {Z}, t: {t}")

            self._render(self.Z, self.t)  # premier rendu

    def _render(self, Z, t):
        """Efface et redessine selon self.channels."""
        self.Z = Z
        self.t = t
        if self.stack is None:
            print("No image stack to render.")
            self.ax.clear()
            self.ax.text(0.5, 0.5, "No image loaded", ha="center", va="center", fontsize=12)
            self.ax.axis("off")
            self.canvas.draw()
            return
        else :
            if self.number_plot == 1:
                self.ax.clear()
                self.ax.axis("off")
                print(self.stack.shape)
                print(len(self.stack.shape))
                if len(self.stack.shape) < 5:
                    img = self.stack[t, Z, :, :]
                else : 
                    img = self.stack[t, Z, 0, :, :]

                self.ax.imshow(img, cmap="gray")
                self.fig.tight_layout(pad=0)
                self.canvas.draw()
                print(f"Rendered image for Z={self.Z} and t={self.t}")
            else :
                self._render_2_plots(self.Z, self.t)

    def _render_2_plots(self, Z, t):
        self.fig.clf()  # Clear the current figure
        self.ax = self.fig.add_subplot(121)  # Add a subplot for the original
        self.ax.imshow(self.stack[self.t, self.Z, 0, :, :], cmap='gray')  # Display the original image
        self.ax.axis('off')  # Hide axes
        self.fig.tight_layout(pad=0)  # Adjust layout
        self.ax = self.fig.add_subplot(122)  # Add a subplot for the binarized image
        self.ax.imshow(self.binarized_image[self.t, self.Z, :, :], cmap='gray')  # Display the binarized image
        self.ax.axis('off')  # Hide axes
        self.fig.tight_layout(pad=0)  # Adjust layout
        self.canvas.draw()  # Redraw the canvas
        print(f"Rendered original and binarized images for Z={self.Z} and t={self.t}")


    def show_binarized_image(self, bin_image, t, Z):
        self.binarized_image = bin_image
        self.number_plot = 2
        print("Binarized image ready to be displayed.")
        self.fig.clf()  # Clear the current figure
        print(f"Shape of original image: {self.stack.shape}")
        self.ax = self.fig.add_subplot(121)  # Add a subplot for the original
        self.ax.imshow(self.stack[t, Z, 0, :, :], cmap='gray')  # Display the original image
        self.ax.axis('off')  # Hide axes
        self.fig.tight_layout(pad=0)  # Adjust layout
        self.ax = self.fig.add_subplot(122)  # Add a subplot for the bin
        print(f"Shape of binarized image: {self.binarized_image.shape}")
        self.ax.imshow(self.binarized_image[t, Z, :, :], cmap='gray')  # Display the binarized image
        self.ax.axis('off')  # Hide axes
        self.fig.tight_layout(pad=0)  # Adjust layout
        self.canvas.draw()  # Redraw the canvas
        print(f"Displayed binarized image for Z={self.Z} and t={self.t}")

