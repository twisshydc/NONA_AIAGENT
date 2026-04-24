import os
import cv2
import base64
import customtkinter as ctk
from PIL import Image, ImageTk
from openai import AzureOpenAI  # Use AzureOpenAI for clarity
from openai import OpenAI

# ==========================================================
# 1. AZURE AI CONFIGURATION
# ==========================================================
endpoint = "https://ai-grandma-check-resource.openai.azure.com/openai/v1"
deployment_name = "gpt-5.4-nano-2"
api_key = "<your-api-key>"

client = OpenAI(
    base_url=endpoint,
    api_key="3VfMyRm8upj8zaXlH1tCq6YlmNg0v0zJJYFXG5wVJvgh9EJeLcWAJQQJ99CDACqBBLyXJ3w3AAAAACOG5ZCs",
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

class GrandmaHealthApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # UI Setup
        self.geometry("400x800") 
        self.title("Health Cam")
        self.configure(fg_color="#fffbf0")

        self.cap = None
        self.is_camera_on = False

        # --- 1. HEADER ---
        self.header = ctk.CTkFrame(self, height=70, corner_radius=0, fg_color="#63b32e")
        self.header.pack(fill="x", side="top")
        
        self.title_label = ctk.CTkLabel(self.header, text="Pill Matcher Cam", 
                                        text_color="white",
                                        font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- 2. BOTTOM ACTION BAR (Button Area) ---
        self.bottom_bar = ctk.CTkFrame(self, height=100, corner_radius=0, fg_color="#2b2b2b")
        self.bottom_bar.pack(fill="x", side="bottom")

        self.action_btn = ctk.CTkButton(self.bottom_bar, text="📷 OPEN CAMERA", 
                                        width=280, height=50, corner_radius=25, 
                                        fg_color="#63b32e", font=("Arial", 18, "bold"),
                                        command=self.toggle_camera)
        self.action_btn.place(relx=0.5, rely=0.5, anchor="center")

        # --- 3. MAIN CONTENT AREA ---
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)

        # Viewfinder
        self.viewfinder = ctk.CTkLabel(self.main_container, text="", fg_color="black", corner_radius=15)
        
        # Chat Feed
        self.feed = ctk.CTkScrollableFrame(self.main_container, fg_color="transparent")
        self.feed.pack(fill="both", expand=True)

        self.add_chat_bubble("AI", "Hi Grandma! I'm ready to help you check your pills.")

    def add_chat_bubble(self, sender, text):
        bg_color = "#333333" if sender == "AI" else "#63b32e"
        bubble = ctk.CTkFrame(self.feed, corner_radius=15, fg_color=bg_color)
        bubble.pack(fill="x", pady=8, padx=5)
        
        lbl = ctk.CTkLabel(bubble, text=f"{sender}: {text}", text_color="white", 
                           wraplength=280, justify="left", font=("Arial", 14))
        lbl.pack(padx=15, pady=12)

    def toggle_camera(self):
        if not self.is_camera_on:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.add_chat_bubble("AI", "Could not find your camera.")
                return
            
            self.feed.pack_forget()
            self.viewfinder.pack(fill="both", expand=True)
            self.action_btn.configure(text="🎯 SCAN PILL NOW", fg_color="#ff4b4b")
            self.is_camera_on = True
            self.update_viewfinder()
        else:
            self.capture_and_analyze()

    def update_viewfinder(self):
        if self.is_camera_on:
            ret, frame = self.cap.read()
            if ret:
                # Draw the target box
                h, w, _ = frame.shape
                cv2.rectangle(frame, (w//4, h//4), (3*w//4, 3*h//4), (0, 255, 0), 2)
                
                frame = cv2.flip(frame, 1)
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                img_tk = ImageTk.PhotoImage(image=img)
                self.viewfinder.configure(image=img_tk)
                self.viewfinder.image = img_tk
            self.after(15, self.update_viewfinder)

    def capture_and_analyze(self):
        ret, frame = self.cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            b64 = base64.b64encode(buffer).decode('utf-8')
            
            self.is_camera_on = False
            self.cap.release()
            self.viewfinder.pack_forget()
            self.feed.pack(fill="both", expand=True)
            self.action_btn.configure(text="📷 OPEN CAMERA", fg_color="#63b32e")
            
            self.add_chat_bubble("Grandma", "[Checking pill image...]")
            
            # --- AI CALL ---
            try:
                # Using DEPLOYMENT_NAME in all caps to match the top
                response = client.chat.completions.create(
                    model=DEPLOYMENT_NAME, 
                    messages=[
                        {"role": "system", "content": "You are a health assistant. Identify the pill in the photo."},
                        {"role": "user", "content": [
                            {"type": "text", "text": "What pill is this?"},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
                        ]}
                    ]
                )
                self.add_chat_bubble("AI", response.choices[0].message.content)
            except Exception as e:
                self.add_chat_bubble("AI", f"Sorry Grandma, I couldn't connect: {str(e)}")

if __name__ == "__main__":
    app = GrandmaHealthApp()
    app.mainloop()