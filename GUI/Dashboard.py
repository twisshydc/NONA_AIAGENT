import customtkinter as ctk
from PIL import Image
import os

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW CONFIGURATION ---
        self.geometry("402x874")
        self.title("Dashboard")
        self.configure(fg_color="#fffbf0")

        # --- 2. DYNAMIC PATH SETUP ---
        CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
        PARENT_DIR = os.path.dirname(CURRENT_DIR)
        ASSETS_DIR = os.path.join(PARENT_DIR, "assets")

        # --- 3. LOAD IMAGES ---
        try:
            self.top_img = ctk.CTkImage(
                light_image=Image.open(os.path.join(ASSETS_DIR, "top.png")), 
                size=(402, 130) 
            )
            self.bottom_img = ctk.CTkImage(
                light_image=Image.open(os.path.join(ASSETS_DIR, "bottom.png")), 
                size=(402, 100)
            )

            # --- MAXIMUM SIZE FOR 2-COLUMN GRID ---
            
            icon_size = (200, 200) 
            self.cam_icon = ctk.CTkImage(Image.open(os.path.join(ASSETS_DIR, "camera.png")), size=icon_size)
            self.med_icon = ctk.CTkImage(Image.open(os.path.join(ASSETS_DIR, "check.png")), size=icon_size)
            self.side_icon = ctk.CTkImage(Image.open(os.path.join(ASSETS_DIR, "medicine.png")), size=icon_size)
            self.chat_icon = ctk.CTkImage(Image.open(os.path.join(ASSETS_DIR, "chatter.png")), size=icon_size)
            
        except Exception as e:
            print(f"Error: {e}")

        # --- 4. BANNERS ---
        if hasattr(self, 'top_img'):
            ctk.CTkLabel(self, image=self.top_img, text="").place(x=0, y=0)   
            ctk.CTkLabel(self, image=self.bottom_img, text="").place(x=0, y=729)

        # --- 5. GRID CONTAINER ---
        self.grid_container = ctk.CTkFrame(self, fg_color="transparent")
        # padx=0 allows the images to reach the very edges of the screen
        self.grid_container.pack(fill="both", expand=True, padx=0, pady=(135, 100))
        
        self.grid_container.columnconfigure((0, 1), weight=1)
        self.grid_container.rowconfigure((0, 1, 2, 3), weight=0)

        # Styling
        hover_style = "#E6E2B2" 
        text_font = ctk.CTkFont(size=18, weight="bold")

        # --- 6. MAX SIZE BUTTONS & LABELS ---

        # CAMERA
        self.btn_cam = ctk.CTkButton(self.grid_container, text="", image=self.cam_icon, 
                                     fg_color="transparent", hover_color=hover_style,
                                     width=200, height=200, command=lambda: self.clicked("Camera"))
        self.btn_cam.grid(row=0, column=0, padx=0, pady=0)
        self.lbl_cam = ctk.CTkLabel(self.grid_container, text="CAMERA", font=text_font, text_color="#000000", cursor="hand2")
        self.lbl_cam.grid(row=1, column=0, pady=(0, 10))
        self.lbl_cam.bind("<Button-1>", lambda e: self.clicked("Camera"))

        # CHECK
        self.btn_med = ctk.CTkButton(self.grid_container, text="", image=self.med_icon, 
                                     fg_color="transparent", hover_color=hover_style,
                                     width=200, height=200, command=lambda: self.clicked("Check"))
        self.btn_med.grid(row=0, column=1, padx=0, pady=0)
        self.lbl_med = ctk.CTkLabel(self.grid_container, text="CHECK", font=text_font, text_color="#000000", cursor="hand2")
        self.lbl_med.grid(row=1, column=1, pady=(0, 10))
        self.lbl_med.bind("<Button-1>", lambda e: self.clicked("Check"))

        # MEDICINE
        self.btn_side = ctk.CTkButton(self.grid_container, text="", image=self.side_icon, 
                                      fg_color="transparent", hover_color=hover_style,
                                      width=200, height=200, command=lambda: self.clicked("Medicine"))
        self.btn_side.grid(row=2, column=0, padx=0, pady=0)
        self.lbl_side = ctk.CTkLabel(self.grid_container, text="MEDICINE", font=text_font, text_color="#000000", cursor="hand2")
        self.lbl_side.grid(row=3, column=0, pady=(0, 10))
        self.lbl_side.bind("<Button-1>", lambda e: self.clicked("Medicine"))

        # CHATTER
        self.btn_chat = ctk.CTkButton(self.grid_container, text="", image=self.chat_icon, 
                                      fg_color="transparent", hover_color=hover_style,
                                      width=200, height=200, command=lambda: self.clicked("Chatter"))
        self.btn_chat.grid(row=2, column=1, padx=0, pady=0)
        self.lbl_chat = ctk.CTkLabel(self.grid_container, text="CHATTER", font=text_font, text_color="#000000", cursor="hand2")
        self.lbl_chat.grid(row=3, column=1, pady=(0, 10))
        self.lbl_chat.bind("<Button-1>", lambda e: self.clicked("Chatter"))

    def clicked(self, name):
        print(f"{name} Clicked!")

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()