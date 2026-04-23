import os
import customtkinter as ctk
from PIL import Image

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
        # Go up one level to 'pythonss'
BASE_DIR = os.path.dirname(CURRENT_DIR)
        # Find 'assets' inside 'pythonss'
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

signup = ctk.CTk()
signup.configure(fg_color="#fffbf0")
signup.title("Main Window")
signup.geometry("402x849")
signup.update_idletasks()

geometryX = 0
geometryY = 0
signup.geometry("+%d+%d"%(geometryX, geometryY))

# --- LOAD ASSETS ---
try:
    # Top image (402 width to match window)
    top_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "top.png")), size=(402, 130))
    # Bottom image
    bottom_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "bottom.png")), size=(402, 100))
except Exception as e:
    print(f"Check your assets folder: {e}")
    top_img = None
    bottom_img = None

# --- PLACE TOP IMAGE ---
if top_img:
    top_label = ctk.CTkLabel(master=signup, image=top_img, text="")
    top_label.place(x=0, y=0)

# --- PLACE BOTTOM IMAGE ---
if bottom_img:
    bottom_label = ctk.CTkLabel(master=signup, image=bottom_img, text="")
    bottom_label.place(x=0, y=700) # Placed at bottom (849 height - 100 image height)

# --- YOUR ORIGINAL ENTRIES ---
entry_fn = ctk.CTkEntry(master=signup, placeholder_text="First Name")
entry_fn.configure(fg_color="#ffffff", width=171, height=53, text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff")
entry_fn.place(x=15, y=282)

entry_ln = ctk.CTkEntry(master=signup, placeholder_text="Last Name")
entry_ln.configure(fg_color="#ffffff", width=171, height=53, text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff")
entry_ln.place(x=200, y=282)

entry_pw = ctk.CTkEntry(master=signup, placeholder_text="Password")
entry_pw.configure(fg_color="#ffffff", width=372, height=60, text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff")
entry_pw.place(x=15, y=380)

entry_cp = ctk.CTkEntry(master=signup, placeholder_text="Confirm Password")
entry_cp.configure(fg_color="#ffffff", width=372, height=60, text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff")
entry_cp.place(x=15, y=480)

# --- SIGNUP BUTTON ---
loginbtn = ctk.CTkButton(master=signup, text="Signup")
loginbtn.configure(fg_color="#54c206", hover_color="#007914", width=94, height=37, text_color="#fff", corner_radius=5)
loginbtn.place(x=146, y=570)

# --- LABELS ---
label_title = ctk.CTkLabel(master=signup, text="Register")
label_title.configure(width=233, height=83, text_color="#000000", corner_radius=5, font=ctk.CTkFont(size=50))
label_title.place(x=70, y=145)

label_f = ctk.CTkLabel(master=signup, text="First Name")
label_f.configure(width=20, height=20, text_color="#000000", corner_radius=5, font=ctk.CTkFont(size=12))
label_f.place(x=15, y=260)

label_l = ctk.CTkLabel(master=signup, text="Last Name")
label_l.configure(width=20, height=20, text_color="#000000", corner_radius=5, font=ctk.CTkFont(size=12))
label_l.place(x=200, y=260)

label_p = ctk.CTkLabel(master=signup, text="Password")
label_p.configure(width=20, height=20, text_color="#000000", corner_radius=5, font=ctk.CTkFont(size=12))
label_p.place(x=19, y=360)

label_c = ctk.CTkLabel(master=signup, text="Confirm Password")
label_c.configure(width=20, height=20, text_color="#000000", corner_radius=5, font=ctk.CTkFont(size=12))
label_c.place(x=19, y=460)

signup.mainloop()