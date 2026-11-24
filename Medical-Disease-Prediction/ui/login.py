import customtkinter as ctk
from tkinter import messagebox
import bcrypt

from utils.database import get_connection


class LoginFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.pack(fill="both", expand=True)

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="🏥 AI Medical Disease Prediction System",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(50, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Login to continue",
            font=("Arial", 18)
        )
        subtitle.pack(pady=(0, 30))

        # ==========================
        # Username
        # ==========================

        self.username = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        # ==========================
        # Password
        # ==========================

        self.password = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        # ==========================
        # Login Button
        # ==========================

        ctk.CTkButton(
            self,
            text="Login",
            width=300,
            height=40,
            command=self.login
        ).pack(pady=20)

        # ==========================
        # Register Button
        # ==========================

        ctk.CTkButton(
            self,
            text="Create New Account",
            width=300,
            fg_color="green",
            hover_color="darkgreen",
            command=self.open_register
        ).pack()

    # ==========================
    # LOGIN
    # ==========================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if username == "" or password == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        row = cursor.fetchone()

        conn.close()

        if row is None:
            messagebox.showerror(
                "Login Failed",
                "User not found."
            )
            return

        try:

            if bcrypt.checkpw(
                password.encode(),
                row[0].encode()
            ):

                self.destroy()

                from ui.dashboard import Dashboard

                Dashboard(
                    self.master,
                    username
                ).pack(fill="both", expand=True)

            else:

                messagebox.showerror(
                    "Login Failed",
                    "Incorrect password."
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ==========================
    # OPEN REGISTER
    # ==========================

    def open_register(self):

        self.destroy()

        from ui.register import RegisterFrame

        RegisterFrame(
            self.master
        ).pack(fill="both", expand=True)