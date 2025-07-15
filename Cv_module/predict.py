import random
def predict_disease(image_path):
    # Fake disease database
    diseases = {
        "Leaf Blight": "Spray neem oil weekly. Remove infected leaves.",
        "Powdery Mildew": "Use sulfur-based fungicide.",
        "Bacterial Spot": "Clean tools and remove plant debris."
    }

    prediction = random.choice(list(diseases.keys()))
    treatment = diseases[prediction]

    return {
        "disease": prediction,
        "treatment": treatment
    }
