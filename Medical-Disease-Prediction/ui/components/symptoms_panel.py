import customtkinter as ctk


class SymptomsPanel(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="transparent")

        ctk.CTkLabel(
            self,
            text="Symptoms",
            font=("Arial", 22, "bold")
        ).pack(anchor="w", pady=(10, 15))

        self.search = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="🔍 Search symptom..."
        )

        self.search.pack(pady=(0, 15))

        self.search.bind("<KeyRelease>", self.filter_symptoms)

        self.scroll = ctk.CTkScrollableFrame(
            self,
            width=420,
            height=500
        )

        self.scroll.pack(fill="both", expand=True)

        self.symptom_list = [

            "Fever",
            "High Fever",
            "Low Fever",
            "Dry Cough",
            "Wet Cough",
            "Sneezing",
            "Runny Nose",
            "Sore Throat",
            "Chest Pain",
            "Shortness of Breath",
            "Wheezing",
            "Palpitations",
            "Headache",
            "Migraine",
            "Dizziness",
            "Blurred Vision",
            "Eye Pain",
            "Eye Redness",
            "Loss of Vision",
            "Ear Pain",
            "Hearing Loss",
            "Fatigue",
            "Weakness",
            "Muscle Pain",
            "Joint Pain",
            "Back Pain",
            "Neck Pain",
            "Body Pain",
            "Abdominal Pain",
            "Stomach Pain",
            "Heartburn",
            "Nausea",
            "Vomiting",
            "Diarrhea",
            "Constipation",
            "Loss of Appetite",
            "Weight Loss",
            "Weight Gain",
            "Frequent Urination",
            "Burning Urination",
            "Blood in Urine",
            "Excessive Thirst",
            "Skin Rash",
            "Itching",
            "Swelling",
            "Chills",
            "Night Sweats",
            "Anxiety",
            "Depression",
            "Insomnia",
            "Loss of Smell",
            "Loss of Taste",
            "Cold Hands",
            "Cold Feet",
            "Difficulty Breathing",
            "High Blood Pressure",
            "Low Blood Pressure",
            "Confusion",
            "Seizures",
            "Fainting"
        ]

        self.variables = {}

        self.draw_symptoms(self.symptom_list)

    def draw_symptoms(self, symptoms):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        self.variables = {}

        for symptom in symptoms:

            var = ctk.BooleanVar()

            chk = ctk.CTkCheckBox(
                self.scroll,
                text=symptom,
                variable=var
            )

            chk.pack(
                anchor="w",
                padx=10,
                pady=4
            )

            self.variables[symptom] = var

    def filter_symptoms(self, event=None):

        keyword = self.search.get().lower()

        filtered = []

        for symptom in self.symptom_list:

            if keyword in symptom.lower():

                filtered.append(symptom)

        self.draw_symptoms(filtered)

    def get_selected(self):

        selected = []

        for symptom, var in self.variables.items():

            if var.get():

                selected.append(symptom)

        return selected