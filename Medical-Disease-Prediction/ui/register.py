import customtkinter as ctk
from tkinter import messagebox
import bcrypt
from utils.database import get_connection

class RegisterFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        ctk.CTkLabel(self,text="Create Account",font=("Arial",28,"bold")).pack(pady=30)
        self.u=ctk.CTkEntry(self,width=300,placeholder_text="Username");self.u.pack(pady=10)
        self.p=ctk.CTkEntry(self,width=300,placeholder_text="Password",show="*");self.p.pack(pady=10)
        self.c=ctk.CTkEntry(self,width=300,placeholder_text="Confirm Password",show="*");self.c.pack(pady=10)
        ctk.CTkButton(self,text="Register",command=self.save).pack(pady=15)
        ctk.CTkButton(self,text="Back",command=self.back).pack()

    def save(self):
        if self.p.get()!=self.c.get():
            messagebox.showerror("Error","Passwords do not match");return
        conn=get_connection();cur=conn.cursor()
        try:
            hp=bcrypt.hashpw(self.p.get().encode(),bcrypt.gensalt()).decode()
            cur.execute("INSERT INTO users(username,password) VALUES(?,?)",(self.u.get(),hp))
            conn.commit()
            messagebox.showinfo("Success","Registration successful")
            self.back()
        except Exception as e:
            messagebox.showerror("Error",str(e))
        finally:
            conn.close()

    def back(self):
        self.destroy()
        from ui.login import LoginFrame
        LoginFrame(self.master).pack(fill="both",expand=True)
