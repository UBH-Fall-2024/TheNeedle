import tkinter as tk

# Function to create a horizontal gradient effect between two colors
def gradient_background(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

def gradient_background1(frame, color1, color2):
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(), bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    num_steps = 100
    for i in range(num_steps):
        color = interpolate_color(color1, color2, i / num_steps)
        canvas.create_rectangle(i * frame.winfo_width() / num_steps, 0,
                                (i + 1) * frame.winfo_width() / num_steps, frame.winfo_height(),
                                outline='', fill=color)

    # Dropdown menu and other widgets
    container = tk.Frame(canvas, bg="", highlightthickness=1, highlightbackground="black")
    container.place(relx=0, rely=0.3, width=300, height=325)

    label = tk.Label(container, text="The Needle\nGale Database\nResearch Tool:",
                     font=("Arial", 14, "bold underline"), wraplength=200, bg="#808080", anchor=tk.CENTER)
    label.place(relx=0.5, y=50, anchor="n")

    text_field = tk.Entry(canvas, font=("Arial", 14), width=30)
    text_field.insert(0, "Enter your URL name")
    text_field.config(fg="#C0C0C0", justify=tk.CENTER)

    def clear_hint(event):
        text_field.delete(0, tk.END)
        text_field.config(fg="#000000")

    def add_hint():
        if text_field.get() == "":
            text_field.insert(0, "Enter your URL name")
            text_field.config(fg="#C0C0C0", justify=tk.CENTER)

    text_field.bind("<FocusIn>", clear_hint)
    text_field.bind("<FocusOut>", add_hint)
    text_field.place(relx=0.49, y=450, anchor="center", width=250)

    button = tk.Button(frame, text="Analyze", font=("Arial", 14, 'bold'), fg="white", bg="green", command=your_function)
    button.place(relx=0.5, y=550, anchor="s")

def your_function():
    print("Analyzing URL...")

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

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Start the GUI function
def start_gui():
    window = tk.Tk()
    window.title('App Title')
    window_width = 800
    window_height = 500
    window.wm_resizable(0, 0)
    window.attributes('-fullscreen', True)
    window.bind("<Escape>", lambda event: window.destroy())
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    frame1_width = int(screen_width * 0.4)
    frame2_width = int(screen_width * 0.2)
    frame3_width = int(screen_width * 0.4)

    frame1 = tk.Frame(window, width=frame1_width, height=screen_height, bd=0, highlightthickness=0, bg="red")
    frame2 = tk.Frame(window, width=frame2_width, height=screen_height, bd=0, highlightthickness=0, bg="grey")
    frame3 = tk.Frame(window, width=frame3_width, height=screen_height, bd=0, highlightthickness=0, bg="blue")

    frame1.pack(side="left", fill="y", padx=0, pady=0)
    frame2.pack(side="left", fill="y", padx=0, pady=0)
    frame3.pack(side="left", fill="y", padx=0, pady=0)

    frame1.after(100, lambda: gradient_background(frame1, "#0000ff", "#808080"))
    frame2.after(100, lambda: gradient_background1(frame2, "#808080", "#808080"))
    frame3.after(100, lambda: gradient_background(frame3, "#808080", "#ff0000"))

    window.mainloop()
start_gui()