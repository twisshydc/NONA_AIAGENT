import customtkinter as ctk
from PIL import Image
import os

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("375x667")
        self.title("AI Home")
        self.configure(fg_color="#FFFBC6")

        # 1. FIND THE ASSETS FOLDER
        # This gets the path to your 'pythonss' folder
        base_path = os.path.dirname(os.path.realpath(__file__))
        # This points specifically to the 'assets' folder inside it
        assets_path = os.path.join(base_path, "assets")

        # --- 2. LOAD IMAGES FROM ASSETS ---
        try:
            self.chat_icon = ctk.CTkImage(
                light_image=Image.open(os.path.join(assets_path, "camera.png")), 
                size=(150, 150)
            )
            self.gen_icon = ctk.CTkImage(
                light_image=Image.open(os.path.join(assets_path, "medicine.png")), 
                size=(150, 150)
            )
            self.hist_icon = ctk.CTkImage(
                light_image=Image.open(os.path.join(assets_path, "side.png")), 
                size=(150, 150)
            )
            self.set_icon = ctk.CTkImage(
                light_image=Image.open(os.path.join(assets_path, "check.png")), 
                size=(150, 150)
            )
        except Exception as e:
            print(f"Warning: Could not find images in assets folder. Error: {e}")
            self.chat_icon = self.gen_icon = self.hist_icon = self.set_icon = None

        # --- 3. THE GRID ---
        self.grid_container = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_container.pack(fill="both", expand=True, padx=20, pady=20)
        self.grid_container.columnconfigure((0, 1), weight=1)
        self.grid_container.rowconfigure((0, 1), weight=1)

        # --- 4. BUTTONS ---
        self.btn1 = ctk.CTkButton(self.grid_container, text="Camera", image=self.chat_icon, 
                                  compound="top", corner_radius=15, height=140)
        self.btn1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.btn2 = ctk.CTkButton(self.grid_container, text="Medicine", image=self.gen_icon, 
                                  compound="top", corner_radius=15, height=140, fg_color="#2ecc71")
        self.btn2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.btn3 = ctk.CTkButton(self.grid_container, text="History", image=self.hist_icon, 
                                  compound="top", corner_radius=15, height=140, fg_color="#1f1f1f")
        self.btn3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.btn4 = ctk.CTkButton(self.grid_container, text="Checklist", image=self.set_icon, 
                                  compound="top", corner_radius=15, height=140, fg_color="#1f1f1f")
        self.btn4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()