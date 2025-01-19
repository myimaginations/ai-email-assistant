import pickle

# Load the pre-trained models and vectorizer
with open("models/urgency_model.pkl", "rb") as f:
    urgency_model = pickle.load(f)

with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Function to predict urgency
def predict_urgency(email_content):
    email_vectorized = vectorizer.transform([email_content])
    urgency = urgency_model.predict(email_vectorized)[0]
    return urgency

# Function to generate a suggested response
def generate_response(urgency):
    responses = {
        "High": "Thank you for your urgent request. We'll prioritize this immediately.",
        "Medium": "Thank you for reaching out. We’ll address your request soon.",
        "Low": "Thank you for your email. We’ll respond when possible."
    }
    return responses.get(urgency, "Thank you for your message.")
