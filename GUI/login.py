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

login = ctk.CTk()
login.configure(fg_color="#fffbf0")
login.title("Main Window")
login.geometry("402x849")
login.update_idletasks()

# Center window logic
geometryX = 0
geometryY = 0
login.geometry("+%d+%d"%(geometryX, geometryY))

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
except Exception as e:
    # This will print the actual path it tried to use so you can see it in the terminal
    print(f"Failed to find assets at: {ASSETS_DIR}")
    print(f"Error: {e}")
    top_img = None
    bottom_img = None

# --- PLACE TOP IMAGE ---
if top_img:
    top_label = ctk.CTkLabel(master=login, image=top_img, text="")
    top_label.place(x=0, y=0)

# --- PLACE BOTTOM IMAGE ---
if bottom_img:
    bottom_label = ctk.CTkLabel(master=login, image=bottom_img, text="")
    # Placed at 749 to stick to the bottom (849 height - 100 image height)
    bottom_label.place(x=0, y=749)

# --- ENTRIES ---
entry = ctk.CTkEntry(master=login, placeholder_text="Username")
entry.configure(fg_color="#ffffff", width=372, height=60, text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff")
entry.place(x=15, y=282)

entry1 = ctk.CTkEntry(master=login, placeholder_text="Password")
entry1.configure(fg_color="#ffffff", width=372, height=60, text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff", show="*")
entry1.place(x=15, y=404)

# --- BUTTON ---
loginbtn = ctk.CTkButton(master=login, text="Login")
loginbtn.configure(fg_color="#54c206", hover_color="#007914", width=94, height=37, text_color="#fff", corner_radius=5)
loginbtn.place(x=146, y=509)

# --- LABELS ---
label = ctk.CTkLabel(master=login, text="Login")
label.configure(width=233, height=83, text_color="#000000", font=ctk.CTkFont(size=50))
label.place(x=66, y=170)

label_u = ctk.CTkLabel(master=login, text="Username")
label_u.configure(width=20, height=20, text_color="#000000", font=ctk.CTkFont(size=12))
label_u.place(x=15, y=250)

label_p = ctk.CTkLabel(master=login, text="Password")
label_p.configure(width=20, height=20, text_color="#000000", font=ctk.CTkFont(size=12))
label_p.place(x=19, y=375)

login.mainloop()