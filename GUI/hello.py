import os
import customtkinter as ctk
from PIL import Image

# 1. FIXED PATH LOGIC
# This is the 'GUI' folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# This goes UP one level to the 'pythonss' folder
PARENT_DIR = os.path.dirname(CURRENT_DIR)
# This joins 'pythonss' with 'assets'
ASSETS_DIR = os.path.join(PARENT_DIR, "assets")

hello = ctk.CTk()
hello.configure(fg_color="#fffbf0")
hello.title("Main Window")
hello.geometry("402x849")
hello.update_idletasks()

# Center window logic
geometryX = 0
geometryY = 0
hello.geometry("+%d+%d"%(geometryX, geometryY))

# --- LOAD ASSETS DYNAMICALLY ---
try:
    top_img = ctk.CTkImage(
        light_image=Image.open(os.path.join(ASSETS_DIR, "top.png")), 
        size=(402, 130) 
    )
    bottom_img = ctk.CTkImage(
        light_image=Image.open(os.path.join(ASSETS_DIR, "bottom.png")), 
        size=(402, 100)
    )
    wave_img = ctk.CTkImage(
        light_image=Image.open(os.path.join(ASSETS_DIR, "wave.png")), 
        size=(222, 222) 
    )
except Exception as e:
    # This will print the actual path it tried to use so you can see it in the terminal
    print(f"Failed to find assets at: {ASSETS_DIR}")
    print(f"Error: {e}")
    top_img = None
    bottom_img = None

# --- PLACE TOP IMAGE ---
if top_img:
    top_label = ctk.CTkLabel(master=hello, image=top_img, text="")
    top_label.place(x=0, y=0)

# --- PLACE BOTTOM IMAGE ---
if bottom_img:
    bottom_label = ctk.CTkLabel(master=hello, image=bottom_img, text="")
    # Placed at 749 to stick to the bottom (849 height - 100 image height)
    bottom_label.place(x=0, y=749)

if wave_img:
    wave_label = ctk.CTkLabel(master=hello, image=wave_img, text="")
    # Placed at 749 to stick to the bottom (849 height - 100 image height)
    wave_label.place(x=80, y=128+50)





# --- LABELS ---
label = ctk.CTkLabel(master=hello, text="Im Nona,")
label.configure( fg_color= "transparent",text_color="#000000", font=ctk.CTkFont(size=50))
label.place(x=100, y=350+50)

label = ctk.CTkLabel(master=hello, text="Your AI Health Assistant")
label.configure(fg_color= "transparent",text_color="#000000", font=ctk.CTkFont(size=30))
label.place(x=40, y=420+50)



hello.mainloop()