import customtkinter as ctk
from tkinter import messagebox

from ui.components.patient_form import PatientForm
from ui.components.symptoms_panel import SymptomsPanel
from utils.predictor import predict_disease


class PredictionFrame(ctk.CTkFrame):

    def __init__(self, master, username):
        super().__init__(master)

        self.master = master
        self.username = username

        self.pack(fill="both", expand=True)

        # ==========================
        # Header
        # ==========================

        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=15, pady=15)

        ctk.CTkLabel(
            header,
            text="🩺 Clinical Decision Support System",
            font=("Arial", 28, "bold")
        ).pack(side="left", padx=20, pady=15)

        # ==========================
        # Main Layout
        # ==========================

        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Left Side
        left = ctk.CTkFrame(body, width=420)
        left.pack(side="left", fill="y", padx=10, pady=10)
        left.pack_propagate(False)

        self.patient_form = PatientForm(left)
        self.patient_form.pack(fill="both", expand=True)

        # Right Side
        right = ctk.CTkFrame(body)
        right.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.symptoms_panel = SymptomsPanel(right)
        self.symptoms_panel.pack(fill="both", expand=True)

        # Bottom Buttons
        bottom = ctk.CTkFrame(self)
        bottom.pack(fill="x", padx=15, pady=15)

        ctk.CTkButton(
            bottom,
            text="🩺 Predict Disease",
            width=220,
            height=45,
            command=self.predict
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            bottom,
            text="⬅ Back",
            width=220,
            height=45,
            fg_color="gray",
            command=self.back
        ).pack(side="left", padx=10)

    # =======================================

    def predict(self):

        patient = self.patient_form.get_data()

        if patient["name"].strip() == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter patient name."
            )
            return

        symptoms = self.symptoms_panel.get_selected()

        if len(symptoms) == 0:
            messagebox.showwarning(
                "Missing Information",
                "Please select at least one symptom."
            )
            return

        predictions = predict_disease(symptoms)

        result = ""

        for i, disease in enumerate(predictions, start=1):

            result += (
                f"{i}. {disease['disease']}\n"
                f"Confidence : {disease['confidence']}%\n"
                f"Severity : {disease['severity']}\n"
                f"Doctor : {disease['doctor']}\n\n"
            )

        best = predictions[0]

        precautions = "\n".join(
            "• " + item for item in best["precautions"]
        )

        matched = "\n".join(
            "✔ " + item for item in best["matched_symptoms"]
        )

        messagebox.showinfo(
            "Prediction Result",
            f"""
Patient : {patient['name']}

=============================

Top Predictions

{result}

=============================

Most Likely Disease

{best['disease']}

Description

{best['description']}

Matched Symptoms

{matched}

Precautions

{precautions}

⚠ Disclaimer

This prediction is generated for educational purposes only and is not a substitute for professional medical diagnosis.
"""
        )

    # =======================================

    def back(self):

        self.destroy()

        from ui.dashboard import Dashboard

        Dashboard(
            self.master,
            self.username
        ).pack(fill="both", expand=True)