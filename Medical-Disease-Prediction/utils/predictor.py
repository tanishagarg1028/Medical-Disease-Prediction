import json
import os


DATABASE_FILE = "data/diseases.json"


def load_diseases():

    if not os.path.exists(DATABASE_FILE):
        return []

    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def predict_disease(selected_symptoms):

    diseases = load_diseases()

    selected = set(selected_symptoms)

    predictions = []

    for disease in diseases:

        disease_symptoms = set(disease["symptoms"])

        matched = selected.intersection(disease_symptoms)

        score = len(matched)

        if score == 0:
            continue

        confidence = round(
            (score / len(disease_symptoms)) * 100,
            1
        )

        predictions.append({

            "disease": disease["disease"],

            "doctor": disease["doctor"],

            "severity": disease["severity"],

            "description": disease["description"],

            "precautions": disease["precautions"],

            "confidence": confidence,

            "matched_symptoms": list(matched)

        })

    predictions.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    if len(predictions) == 0:

        return [{
            "disease": "Unknown",
            "doctor": "General Physician",
            "severity": "Unknown",
            "description": "No close match found.",
            "precautions": [
                "Please consult a qualified doctor."
            ],
            "confidence": 0,
            "matched_symptoms": []
        }]

    return predictions[:3]