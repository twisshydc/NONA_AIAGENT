import os
import sys
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

# Path Logic
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
ASSETS_DIR = os.path.join(PARENT_DIR, "assets")

# Import Database from the other folder
sys.path.append(PARENT_DIR)
from database.database import signup_user, login_user

class NonaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color="#fffbf0")
        self.title("Main Window")
        self.geometry("402x849+0+0")

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.load_assets()
        self.show_welcome_screen()

    def load_assets(self):
        try:
            self.top_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "top.png")), size=(402, 130))
            self.bottom_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "bottom.png")), size=(402, 100))
            self.wave_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "wave.png")), size=(222, 222))
            self.normal_img = ctk.CTkImage(light_image=Image.open(os.path.join(ASSETS_DIR, "normal.png")), size=(300, 300))
        except:
            self.top_img = self.bottom_img = self.wave_img = self.normal_img = None

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        if self.top_img:
            ctk.CTkLabel(master=self.container, image=self.top_img, text="").place(x=0, y=0)

    def show_welcome_screen(self):
        self.clear_screen()
        if self.bottom_img:
            ctk.CTkLabel(master=self.container, image=self.bottom_img, text="").place(x=0, y=749)
        if self.wave_img:
            ctk.CTkLabel(master=self.container, image=self.wave_img, text="").place(x=80, y=178)
        
        label1 = ctk.CTkLabel(master=self.container, text="Im Nona,", font=ctk.CTkFont(size=50), text_color="#000000")
        label1.place(x=100, y=400)
        label2 = ctk.CTkLabel(master=self.container, text="Your AI Health Assistant", font=ctk.CTkFont(size=30), text_color="#000000")
        label2.place(x=40, y=470)
        
        ctk.CTkButton(master=self.container, text="Next", fg_color="#54c206", command=self.show_age_screen).place(x=130, y=600)

    def show_age_screen(self):
        self.clear_screen()
        if self.bottom_img:
            ctk.CTkLabel(master=self.container, image=self.bottom_img, text="").place(x=0, y=749)
        if self.normal_img:
            ctk.CTkLabel(master=self.container, image=self.normal_img, text="").place(x=80, y=100)
            
        ctk.CTkLabel(master=self.container, text="How old are you?", font=ctk.CTkFont(size=40, weight="bold"), text_color="#000000").place(x=45, y=385)
        self.age_display = ctk.CTkLabel(master=self.container, text="70", text_color="#63b32e", font=ctk.CTkFont(size=80, weight="bold"))
        self.age_display.place(relx=0.5, y=520, anchor="center")
        
        slider = ctk.CTkSlider(master=self.container, from_=50, to=130, width=300, command=lambda v: self.age_display.configure(text=f"{int(v)}"))
        slider.set(70)
        slider.place(relx=0.5, y=620, anchor="center")
        
        ctk.CTkButton(master=self.container, text="Confirm", fg_color="#54c206", command=self.show_signup_screen).place(x=130, y=700)

    def show_signup_screen(self):
        self.clear_screen()
        if self.bottom_img:
            ctk.CTkLabel(master=self.container, image=self.bottom_img, text="").place(x=0, y=700)
        
        # EXACT SIGNUP DESIGN
        ctk.CTkLabel(master=self.container, text="Register", font=ctk.CTkFont(size=50), text_color="#000000").place(x=110, y=145)
        ctk.CTkLabel(master=self.container, text="First Name", font=ctk.CTkFont(size=15), text_color="#000000").place(x=15, y=250)
        ctk.CTkLabel(master=self.container, text="Last Name", font=ctk.CTkFont(size=15), text_color="#000000").place(x=200, y=250)
        ctk.CTkLabel(master=self.container, text="Password", font=ctk.CTkFont(size=15), text_color="#000000").place(x=15, y=350)
        fn = ctk.CTkEntry(master=self.container,fg_color="#ffffff", font=ctk.CTkFont(size=20), text_color="#000000", placeholder_text="First Name", width=171, height=53)
        fn.place(x=15, y=282)
        ln = ctk.CTkEntry(master=self.container,fg_color="#ffffff", font=ctk.CTkFont(size=20), text_color="#000000", placeholder_text="Last Name", width=171, height=53)
        ln.place(x=200, y=282)
        pw = ctk.CTkEntry(master=self.container, placeholder_text="Password", width=355, height=60,font=ctk.CTkFont(size=20), fg_color="#ffffff", text_color="#000000", show="*")
        pw.place(x=15, y=380)

        def reg():
            if signup_user(fn.get(), ln.get(), pw.get()):
                messagebox.showinfo("Nona", "Success!")
                self.show_login_screen()
            else:
                messagebox.showwarning("Nona", "Error")

        ctk.CTkButton(master=self.container, text="Signup", fg_color="#54c206", font=ctk.CTkFont(size=20),command=reg).place(x=146, y=490)
        
        # LINK TO LOGIN
        ctk.CTkButton(master=self.container, text="I have an account", fg_color="transparent", text_color="black", 
                      command=self.show_login_screen).place(x=130, y=630)

    def show_login_screen(self):
        self.clear_screen()
        if self.bottom_img:
            ctk.CTkLabel(master=self.container, image=self.bottom_img, text="").place(x=0, y=749)
            
        # YOUR EXACT LOGIN DESIGN CODE
        ctk.CTkLabel(master=self.container, text="Login", width=233, height=83, text_color="#000000", font=ctk.CTkFont(size=50)).place(x=66, y=170)
        ctk.CTkLabel(master=self.container, text="Username", width=20, height=20, text_color="#000000", font=ctk.CTkFont(size=20)).place(x=15, y=250)
        ctk.CTkLabel(master=self.container, text="Password", width=20, height=20, text_color="#000000", font=ctk.CTkFont(size=20)).place(x=15, y=350)

        u = ctk.CTkEntry(master=self.container, placeholder_text="Username", width=372, height=60, fg_color="#ffffff", text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff")
        u.place(x=15, y=282)
        p = ctk.CTkEntry(master=self.container, placeholder_text="Password", width=372, height=60, fg_color="#ffffff", text_color="#000000", corner_radius=5, border_width=2, border_color="#ffffff", show="*")
        p.place(x=15, y=404)

        def log():
            if login_user(u.get(), p.get()):
                messagebox.showinfo("Nona", "Welcome!")
            else:
                messagebox.showerror("Nona", "Wrong!")

        ctk.CTkButton(master=self.container, text="Login", fg_color="#54c206", hover_color="#007914", width=94, height=37, command=log).place(x=146, y=509)

if __name__ == "__main__":
    app = NonaApp()
    app.mainloop()