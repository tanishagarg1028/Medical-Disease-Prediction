import customtkinter as ctk


class PatientForm(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="transparent")

        title = ctk.CTkLabel(
            self,
            text="Patient Information",
            font=("Arial", 22, "bold")
        )

        title.pack(anchor="w", pady=(10, 20))

        self.name = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Patient Name"
        )

        self.name.pack(pady=8)

        self.age = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Age"
        )

        self.age.pack(pady=8)

        self.gender = ctk.CTkOptionMenu(
            self,
            values=[
                "Male",
                "Female",
                "Other"
            ]
        )

        self.gender.pack(pady=8)

        self.blood = ctk.CTkOptionMenu(
            self,
            values=[
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ]
        )

        self.blood.pack(pady=8)

        self.height = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Height (cm)"
        )

        self.height.pack(pady=8)

        self.weight = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Weight (kg)"
        )

        self.weight.pack(pady=8)

        self.bp = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Blood Pressure (120/80)"
        )

        self.bp.pack(pady=8)

        self.sugar = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text="Blood Sugar"
        )

        self.sugar.pack(pady=8)

    def get_data(self):

        return {

            "name": self.name.get(),

            "age": self.age.get(),

            "gender": self.gender.get(),

            "blood": self.blood.get(),

            "height": self.height.get(),

            "weight": self.weight.get(),

            "bp": self.bp.get(),

            "sugar": self.sugar.get()

        }