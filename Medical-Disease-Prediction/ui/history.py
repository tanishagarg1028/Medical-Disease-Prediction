import customtkinter as ctk
from utils.database import get_connection


class HistoryFrame(ctk.CTkFrame):

    def __init__(self, master, username):
        super().__init__(master)

        self.master = master
        self.username = username

        self.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self,
            text="📜 Prediction History",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        self.history_box = ctk.CTkTextbox(
            self,
            width=900,
            height=450
        )
        self.history_box.pack(padx=20, pady=20)

        self.load_history()

        ctk.CTkButton(
            self,
            text="⬅ Back",
            width=250,
            command=self.back
        ).pack(pady=15)

    def load_history(self):

        self.history_box.delete("1.0", "end")

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT patient, disease, doctor, created_at
                FROM predictions
                ORDER BY id DESC
            """)

            rows = cursor.fetchall()

        except Exception:
            rows = []

        conn.close()

        if len(rows) == 0:
            self.history_box.insert(
                "end",
                "No prediction history found."
            )
            return

        for patient, disease, doctor, created_at in rows:

            self.history_box.insert(
                "end",
                f"""
========================================

Patient : {patient}

Disease : {disease}

Doctor : {doctor}

Date : {created_at}

========================================

"""
            )

        self.history_box.configure(state="disabled")

    def back(self):

        self.destroy()

        from ui.dashboard import Dashboard

        Dashboard(
            self.master,
            self.username
        ).pack(fill="both", expand=True)