import os
import customtkinter as ctk
from tkinter import messagebox


class ReportsFrame(ctk.CTkFrame):

    def __init__(self, master, username):
        super().__init__(master)

        self.master = master
        self.username = username

        self.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self,
            text="📄 PDF Reports",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        self.report_box = ctk.CTkTextbox(
            self,
            width=900,
            height=420
        )

        self.report_box.pack(padx=20, pady=20)

        self.load_reports()

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        ctk.CTkButton(
            button_frame,
            text="Refresh",
            width=180,
            command=self.refresh
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            button_frame,
            text="Open Reports Folder",
            width=180,
            command=self.open_folder
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            button_frame,
            text="Back",
            width=180,
            fg_color="gray",
            command=self.back
        ).pack(side="left", padx=10)

    def load_reports(self):

        self.report_box.delete("1.0", "end")

        os.makedirs("reports", exist_ok=True)

        files = sorted(
            os.listdir("reports"),
            reverse=True
        )

        pdfs = [f for f in files if f.lower().endswith(".pdf")]

        if len(pdfs) == 0:

            self.report_box.insert(
                "end",
                "No PDF reports found."
            )

            self.report_box.configure(state="disabled")
            return

        for file in pdfs:

            self.report_box.insert(
                "end",
                file + "\n"
            )

        self.report_box.configure(state="disabled")

    def refresh(self):

        self.report_box.configure(state="normal")
        self.load_reports()

    def open_folder(self):

        path = os.path.abspath("reports")

        try:
            os.startfile(path)
        except Exception:
            messagebox.showerror(
                "Error",
                f"Cannot open folder:\n{path}"
            )

    def back(self):

        self.destroy()

        from ui.dashboard import Dashboard

        Dashboard(
            self.master,
            self.username
        ).pack(fill="both", expand=True)