import customtkinter as ctk


class Dashboard(ctk.CTkFrame):

    def __init__(self, master, username):
        super().__init__(master)

        self.master = master
        self.username = username

        self.pack(fill="both", expand=True)

        # ===========================
        # Sidebar
        # ===========================

        sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        ctk.CTkLabel(
            sidebar,
            text="🏥\nMedical AI",
            font=("Arial", 24, "bold")
        ).pack(pady=30)

        ctk.CTkButton(
            sidebar,
            text="🏠 Dashboard",
            width=180,
            state="disabled"
        ).pack(pady=8)

        ctk.CTkButton(
            sidebar,
            text="🩺 Disease Prediction",
            width=180,
            command=self.open_prediction
        ).pack(pady=8)

        ctk.CTkButton(
            sidebar,
            text="📜 Prediction History",
            width=180,
            command=self.open_history
        ).pack(pady=8)

        ctk.CTkButton(
            sidebar,
            text="📄 PDF Reports",
            width=180,
            command=self.open_reports
        ).pack(pady=8)

        ctk.CTkButton(
            sidebar,
            text="🚪 Logout",
            width=180,
            fg_color="red",
            hover_color="#AA0000",
            command=self.logout
        ).pack(side="bottom", pady=20)

        # ===========================
        # Main Area
        # ===========================

        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            main,
            text="AI Medical Disease Prediction System",
            font=("Arial", 30, "bold")
        ).pack(anchor="w")

        ctk.CTkLabel(
            main,
            text=f"Welcome, {username}",
            font=("Arial", 18)
        ).pack(anchor="w", pady=(0, 25))

        cards = ctk.CTkFrame(main)
        cards.pack(fill="x")

        self.create_card(cards, "Patients", "--").pack(side="left", padx=10)
        self.create_card(cards, "Predictions", "--").pack(side="left", padx=10)
        self.create_card(cards, "Reports", "--").pack(side="left", padx=10)

        ctk.CTkButton(
            main,
            text="🩺 Start Disease Prediction",
            width=350,
            height=55,
            font=("Arial", 18, "bold"),
            command=self.open_prediction
        ).pack(pady=50)

    # ===========================

    def create_card(self, parent, title, value):

        frame = ctk.CTkFrame(
            parent,
            width=180,
            height=120
        )

        frame.pack_propagate(False)

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Arial", 18)
        ).pack(pady=10)

        ctk.CTkLabel(
            frame,
            text=value,
            font=("Arial", 28, "bold")
        ).pack()

        return frame

    # ===========================

    def open_prediction(self):

        self.destroy()

        from ui.prediction import PredictionFrame

        PredictionFrame(
            self.master,
            self.username
        ).pack(fill="both", expand=True)

    # ===========================

    def open_history(self):

        self.destroy()

        from ui.history import HistoryFrame

        HistoryFrame(
            self.master,
            self.username
        ).pack(fill="both", expand=True)

    # ===========================

    def open_reports(self):

        self.destroy()

        from ui.reports import ReportsFrame

        ReportsFrame(
            self.master,
            self.username
        ).pack(fill="both", expand=True)

    # ===========================

    def logout(self):

        self.destroy()

        from ui.login import LoginFrame

        LoginFrame(
            self.master
        ).pack(fill="both", expand=True)