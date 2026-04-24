import os
import customtkinter as ctk
from openai import AzureOpenAI  # Use AzureOpenAI for clarity
from openai import OpenAI
from PIL import Image, ImageOps, ImageDraw

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

print(completion.choices[0].message)

class MobileApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- TALL & BOLD FONTS ---
        self.chat_font = ctk.CTkFont(family="Arial", size=30, weight="normal") 
        self.title_font = ctk.CTkFont(family="Arial", size=34, weight="bold")
        self.entry_font = ctk.CTkFont(family="Arial", size=24)

        # Window Setup
        self.geometry("402x874") 
        self.title("Health Chatter")
        self.configure(fg_color="#fffbf0") 

        # Header
        self.header = ctk.CTkFrame(self, height=110, corner_radius=0, fg_color="#63b32e")
        self.header.pack(fill="x", side="top")
        
        self.title_label = ctk.CTkLabel(self.header, text="Health Journal", 
                                        text_color="white",
                                        font=self.title_font)
        self.title_label.place(relx=0.5, rely=0.6, anchor="center")

        # Chat Feed
        self.feed = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.feed.pack(fill="both", expand=True, padx=10, pady=10)

        # Bottom Bar
        self.bottom_bar = ctk.CTkFrame(self, height=100, corner_radius=20, fg_color="#2b2b2b")
        self.bottom_bar.pack(fill="x", side="bottom", padx=10, pady=10)

        self.entry = ctk.CTkEntry(self.bottom_bar, placeholder_text="Type here...", 
                                  font=self.entry_font,
                                  border_width=0, corner_radius=15, width=270, height=60)
        self.entry.place(relx=0.4, rely=0.5, anchor="center")
        self.entry.bind("<Return>", lambda e: self.send_message())

        self.send_btn = ctk.CTkButton(self.bottom_bar, text="↑", width=55, height=55,
                                      corner_radius=28, font=("Arial", 32, "bold"),
                                      command=self.send_message)
        self.send_btn.place(relx=0.88, rely=0.5, anchor="center")

        self.add_chat_bubble("AI", "Good morning! How are you feeling?")

    def add_chat_bubble(self, sender, text):
        bg_color = "#333333" if sender == "AI" else "#63b32e"
        align = "w" if sender == "AI" else "e"
        
        bubble = ctk.CTkFrame(self.feed, corner_radius=25, fg_color=bg_color)
        bubble.pack(fill="x", pady=12, padx=5, anchor=align)
        
        lbl_body = ctk.CTkLabel(bubble, text=text, text_color="white", 
                                font=self.chat_font,
                                wraplength=260, justify="left")
        lbl_body.pack(padx=20, pady=20)
        
        self.after(100, lambda: self.feed._parent_canvas.yview_moveto(1.0))

    def send_message(self):
        user_text = self.entry.get()
        if not user_text: return
        
        self.add_chat_bubble("Me", user_text)
        self.entry.delete(0, 'end')

        try:
            response = client.chat.completions.create(
                model=deployment_name,
                messages=[
                    {"role": "system", "content": "You are a friendly caregiver. Use very large text. Keep sentences short."},
                    {"role": "user", "content": user_text}
                ]
            )
            ai_text = response.choices[0].message.content
            self.add_chat_bubble("AI", ai_text)
        except Exception as e:
            self.add_chat_bubble("AI", "I'm having a little trouble connecting!")

if __name__ == "__main__":
    app = MobileApp()
    app.resizable(False, False) 
    app.mainloop()