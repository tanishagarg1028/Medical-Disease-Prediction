import customtkinter as ctk
from config import *
from utils.database import initialize_database
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class MedicalApp(ctk.CTk):
    def __init__(self):
        super().__init__();initialize_database();self.title(APP_NAME);self.geometry(f"{WIDTH}x{HEIGHT}");        from ui.login import LoginFrame
        LoginFrame(self).pack(fill="both",expand=True)
if __name__=="__main__":
 app=MedicalApp();app.mainloop()
