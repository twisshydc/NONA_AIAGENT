import os
import customtkinter as ctk
from PIL import Image

# 1. FIXED PATH LOGIC
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
ASSETS_DIR = os.path.join(PARENT_DIR, "assets")

hello = ctk.CTk()
hello.configure(fg_color="#fffbf0")
hello.title("Main Window")
hello.geometry("402x849")
hello.update_idletasks()

# --- ASSET LOADING ---
try:
    top_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "top.png")), size=(402, 130))
    bottom_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "bottom.png")), size=(402, 100))
    normal_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "normal.png")), size=(300, 300))
except Exception as e:
    print(f"Error loading assets: {e}")
    top_img = bottom_img = normal_img = None

if top_img:
    ctk.CTkLabel(master=hello, image=top_img, text="").place(x=0, y=0)
if bottom_img:
    ctk.CTkLabel(master=hello, image=bottom_img, text="").place(x=0, y=749)
if normal_img:
    ctk.CTkLabel(master=hello, image=normal_img, text="").place(x=80, y=100)

# --- AGE SLIDER LOGIC ---

def slider_event(value):
    # Updates the label text with the integer value of the slider
    age_display.configure(text=f"{int(value)}")

# 1. Question Label
label = ctk.CTkLabel(master=hello, text="How old are you?")
label.configure(fg_color="transparent", text_color="#000000", font=ctk.CTkFont(size=40, weight="bold"))
label.place(x=45, y=385)

# 2. Large Age Number (The display)
age_display = ctk.CTkLabel(master=hello, text="70") # Default starting age
age_display.configure(text_color="#63b32e", font=ctk.CTkFont(size=80, weight="bold"))
age_display.place(relx=0.5, y=520, anchor="center")

# 3. The Slider
# range is 50 to 100, starting at 70
age_slider = ctk.CTkSlider(master=hello, 
                           from_=50, 
                           to=130, 
                           number_of_steps=50,
                           command=slider_event,
                           button_color="#63b32e",      # Green handle
                           button_hover_color="#4d8c24", 
                           progress_color="#63b32e",    # Green track
                           width=300,
                           height=30)                   # Taller bar for easier touch
age_slider.set(70) 
age_slider.place(relx=0.5, y=620, anchor="center")

hello.mainloop()