'''
from tkinter import *
import tkinter as tk
import os
import sys

# Function to create a horizontal gradient effect between two colors
def gradient_background(frame, color1, color2):
    # Update frame dimensions
    frame.update_idletasks()  # Ensures accurate width and height
    
    # Create a canvas to fit the frame, using the exact frame dimensions
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0, 
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

# Helper function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return rgb_to_hex(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Helper function to convert RGB to hex
def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Window info / Control
window = tk.Tk()
window.title('App Title')
window_width = 800
window_height = 500
window.wm_resizable(0, 0)
window.wm_overrideredirect(False)
window.attributes('-fullscreen', True)
window.bind("<Escape>", lambda event: window.destroy())
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Frames / Segments with custom widths
frame1_width = int(screen_width * 0.4)  # 40% of the screen width
frame2_width = int(screen_width * 0.2)  # 20% of the screen width
frame3_width = int(screen_width * 0.4)  # 40% of the screen width

# Create the frames with no borders, padding, or highlight thickness
frame1 = tk.Frame(window, width=frame1_width, height=screen_height, bd=0, highlightthickness=0, bg="red")
frame2 = tk.Frame(window, width=frame2_width, height=screen_height, bd=0, highlightthickness=0, bg="grey")
frame3 = tk.Frame(window, width=frame3_width, height=screen_height, bd=0, highlightthickness=0, bg="blue")

# Packing the frames with no extra padding, ensuring full width and height
frame1.pack(side="left", fill="y", padx=0, pady=0)
frame2.pack(side="left", fill="y", padx=0, pady=0)
frame3.pack(side="left", fill="y", padx=0, pady=0)

# Use a slightly longer delay to ensure frames are rendered before applying the gradient
frame1.after(100, lambda: gradient_background(frame1, "#0000ff", "#808080"))  # Blue to Grey
frame2.after(100, lambda: gradient_background(frame2, "#808080", "#808080"))  # Grey gradient
frame3.after(100, lambda: gradient_background(frame3, "#808080", "#ff0000"))  # Grey to Red

# Boot GUI Startup 
window.mainloop()
'''

'''
from tkinter import *
import tkinter as tk
import os
import sys

# Function to create a horizontal gradient effect between two colors
def gradient_background(frame, color1, color2):
    # Update frame dimensions
    frame.update_idletasks()  # Ensures accurate width and height
    
    # Create a canvas to fit the frame, using the exact frame dimensions
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0, 
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

# Helper function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return rgb_to_hex(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Helper function to convert RGB to hex
def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Window info / Control
window = tk.Tk()
window.title('App Title')
window_width = 800
window_height = 500
window.wm_resizable(0, 0)
window.wm_overrideredirect(False)
window.attributes('-fullscreen', True)
window.bind("<Escape>", lambda event: window.destroy())
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Frames / Segments with custom widths
frame1_width = int(screen_width * 0.4)  # 40% of the screen width
frame3_width = int(screen_width * 0.4)  # 40% of the screen width

# Create the frames with no borders, padding, or highlight thickness
frame1 = tk.Frame(window, width=frame1_width, height=screen_height, bd=0, highlightthickness=0, bg="red")
frame3 = tk.Frame(window, width=frame3_width, height=screen_height, bd=0, highlightthickness=0, bg="blue")

# Packing the frames with no extra padding, ensuring full width and height
frame1.pack(side="left", fill="y", padx=0, pady=0)
frame3.pack(side="left", fill="y", padx=0, pady=0)

# Use a slightly longer delay to ensure frames are rendered before applying the gradient
frame1.after(100, lambda: gradient_background(frame1, "#0000ff", "#808080"))  # Blue to Grey
frame3.after(100, lambda: gradient_background(frame3, "#808080", "#ff0000"))  # Grey to Red

# Boot GUI Startup 
window.mainloop()
'''

from tkinter import *
import tkinter as tk

class BiasGradientGUI:
    def __init__(self, bias_percentage):
        self.bias_percentage = bias_percentage
        self.right_percentage = 100 - bias_percentage
        self.window = tk.Tk()
        self.setup_window()
        self.setup_frames()
        self.add_labels()  # Add both percentages and directions on the same line
        self.window.mainloop()

    def setup_window(self):
        self.window.title('Bias Summary')
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg="black")  # Set window background to black
        self.window.bind("<Escape>", lambda event: self.window.destroy())
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

    def setup_frames(self):
        # Calculate widths based on bias percentage
        frame1_width = int(self.screen_width * (self.bias_percentage / 100))
        frame3_width = self.screen_width - frame1_width

        # Create frames for left (blue) and right (red) bias
        frame1 = tk.Frame(self.window, width=frame1_width, height=self.screen_height, bd=0, highlightthickness=0)
        frame3 = tk.Frame(self.window, width=frame3_width, height=self.screen_height, bd=0, highlightthickness=0)

        # Pack frames to the left and right
        frame1.pack(side="left", fill="y")
        frame3.pack(side="left", fill="y")

        # Apply gradients to frames
        frame1.after(100, lambda: self.apply_gradient(frame1, "#0000ff", "#808080"))  # Blue to Grey
        frame3.after(100, lambda: self.apply_gradient(frame3, "#808080", "#ff0000"))  # Grey to Red

    def apply_gradient(self, frame, color1, color2):
        frame.update_idletasks()
        canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        num_steps = 100
        for i in range(num_steps):
            color = self.interpolate_color(color1, color2, i / num_steps)
            canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                    (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                    outline='', fill=color)

    def interpolate_color(self, color1, color2, factor):
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)
        r = int(r1 + (r2 - r1) * factor)
        g = int(g1 + (g2 - g1) * factor)
        b = int(b1 + (b2 - b1) * factor)
        return self.rgb_to_hex(r, g, b)

    def add_labels(self):
        # Create label frame with a black background to match the window
        label_frame = tk.Frame(self.window, bg='black')  
        label_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centered in the window

        # Create labels for left and right percentages and directions
        left_label = tk.Label(
            label_frame, 
            text=f"{self.bias_percentage}% Left", 
            font=("Helvetica", 30, "bold"), 
            fg="white", 
            bg="black"
        )
        right_label = tk.Label(
            label_frame, 
            text=f"{self.right_percentage}% Right", 
            font=("Helvetica", 30, "bold"), 
            fg="white", 
            bg="black"
        )

        # Pack labels side by side
        left_label.pack(side="left", padx=10)
        right_label.pack(side="left", padx=10)

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Example usage: 20% left, 80% right
app = BiasGradientGUI(bias_percentage=20)
