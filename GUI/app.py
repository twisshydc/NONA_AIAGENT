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

        # Window Setup
        self.geometry("402x874") 
        self.title("Health Chatter")
        self.configure(fg_color="#fffbf0") # Your original background

        # --- IMAGE LOADING ---
        # Set paths for your images (ensure these exist in your folder)
        self.bot_image_path = "chatter.png" # You need this file!
        self.grandma_image_path = "grandma.jpg" # You need this file!

        # Fallback if images don't exist
        if not os.path.exists(self.bot_image_path): self.bot_image_path = None
        if not os.path.exists(self.grandma_image_path): self.grandma_image_path = None

        # Header (Your original green)
        self.header = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color="#63b32e")
        self.header.pack(fill="x", side="top")
        
        self.title_label = ctk.CTkLabel(self.header, text="Health Journal", 
                                        text_color="white",
                                        font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.6, anchor="center")

        # Chat Feed
        self.feed = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.feed.pack(fill="both", expand=True, padx=10, pady=10)

        # Bottom Bar
        self.bottom_bar = ctk.CTkFrame(self, height=70, corner_radius=20, fg_color="#2b2b2b")
        self.bottom_bar.pack(fill="x", side="bottom", padx=10, pady=10)

        self.entry = ctk.CTkEntry(self.bottom_bar, placeholder_text="Tell me how you feel...", 
                                  border_width=0, corner_radius=15, width=250)
        self.entry.place(relx=0.4, rely=0.5, anchor="center")
        self.entry.bind("<Return>", lambda e: self.send_message())

        self.send_btn = ctk.CTkButton(self.bottom_bar, text="↑", width=40, 
                                      corner_radius=20, font=("Arial", 20),
                                      command=self.send_message)
        self.send_btn.place(relx=0.88, rely=0.5, anchor="center")

        # Initial Greeting
        self.add_chat_bubble("AI", "Good morning, Grandma! How are you feeling today?")

    def get_circular_image(self, image_path, size=(40, 40)):
        """Helper to load and crop an image into a circle."""
        if not image_path: return None # Handle missing image

        # Load and resize
        img = Image.open(image_path).convert("RGBA")
        img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
        
        # Create circular mask
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        
        # Apply mask
        img.putalpha(mask)
        return ctk.CTkImage(light_image=img, dark_image=img, size=size)

    def add_chat_bubble(self, sender, text):
        # Kept your original colors exactly
        is_ai = (sender == "AI")
        bg_color = "#333333" if is_ai else "#63b32e" # Your Dark / Your Green
        
        # A row container for the avatar + bubble
        row = ctk.CTkFrame(self.feed, fg_color="transparent")
        row.pack(fill="x", pady=8)

        # 1. ADDING THE PICTURE
        # Determine which image to load
        img_path = self.bot_image_path if is_ai else self.grandma_image_path
        avatar_img = self.get_circular_image(img_path)

        if avatar_img:
            # Display the real image
            avatar = ctk.CTkLabel(row, image=avatar_img, text="", 
                                  width=40, height=40)
        else:
            # Fallback emoji if no image file is provided
            avatar = ctk.CTkLabel(row, text="🤖" if is_ai else "👵", font=("Arial", 22), 
                                  width=40, height=40, fg_color="#d0d0d0", corner_radius=100)
        
        # 2. Placement Logic (Messenger style but with your green)
        if is_ai:
            avatar.pack(side="left", padx=(5, 10), anchor="s") # Avatar on left
            bubble = ctk.CTkFrame(row, corner_radius=15, fg_color=bg_color)
            bubble.pack(side="left", padx=5)
        else:
            avatar.pack(side="right", padx=(10, 5), anchor="s") # Avatar on right
            bubble = ctk.CTkFrame(row, corner_radius=15, fg_color=bg_color)
            bubble.pack(side="right", padx=5)

        lbl_body = ctk.CTkLabel(bubble, text=text, text_color="white", wraplength=220, justify="left")
        lbl_body.pack(padx=15, pady=10)
        
        # Auto-scroll to bottom
        self.update_idletasks()
        self.feed._parent_canvas.yview_moveto(1.0)

    def send_message(self):
        user_text = self.entry.get()
        if not user_text: return
        self.add_chat_bubble("Grandma", user_text)
        self.entry.delete(0, 'end')
        # ... (Your API call logic remains the same)

if __name__ == "__main__":
    app = MobileApp()
    app.resizable(False, False) 
    app.mainloop()