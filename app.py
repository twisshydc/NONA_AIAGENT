import customtkinter as ctk

class MobileApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Set the 'Phone' dimensions (Portrait mode)
        self.geometry("375x667") 
        self.title("Mobile UI")
        self.configure(fg_color="#ffffff") # Deep dark background

        # 2. Header / Status Bar Area
        self.header = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color="#2b2b2b")
        self.header.pack(fill="x", side="top")
        
        self.title_label = ctk.CTkLabel(self.header, text="My AI App", 
                                        font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.6, anchor="center")

        # 3. Content Area (Scrollable like a feed)
        self.feed = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.feed.pack(fill="both", expand=True, padx=10, pady=10)

        # Let's add some "Cards" to the feed
        for i in range(5):
            self.add_card(f"AI Update #{i+1}", "This is a mobile-style card component.")

        # 4. Bottom Navigation / Input Area
        self.bottom_bar = ctk.CTkFrame(self, height=70, corner_radius=20, fg_color="#2b2b2b")
        self.bottom_bar.pack(fill="x", side="bottom", padx=10, pady=10)

        self.entry = ctk.CTkEntry(self.bottom_bar, placeholder_text="Message AI...", 
                                  border_width=0, corner_radius=15, width=250)
        self.entry.place(relx=0.4, rely=0.5, anchor="center")

        self.send_btn = ctk.CTkButton(self.bottom_bar, text="↑", width=40, 
                                      corner_radius=20, font=("Arial", 20))
        self.send_btn.place(relx=0.88, rely=0.5, anchor="center")

    def add_card(self, title, text):
        card = ctk.CTkFrame(self.feed, corner_radius=15, fg_color="#333333")
        card.pack(fill="x", pady=10)
        
        lbl_title = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(weight="bold"))
        lbl_title.pack(padx=15, pady=(10, 0), anchor="w")
        
        lbl_body = ctk.CTkLabel(card, text=text, text_color="gray")
        lbl_body.pack(padx=15, pady=(0, 10), anchor="w")

if __name__ == "__main__":
    app = MobileApp()
    app.resizable(False, False) # Lock it so it stays phone-shaped
    app.mainloop()