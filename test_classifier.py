import pandas as pd
import pickle

# Test the trained model
def test_classifier():
    # Load the vectorizer and model
    with open('models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    with open('models/urgency_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Test data
    test_data = [
        "This is urgent, please respond ASAP.",
        "Important update on the project timeline.",
        "Let's schedule the meeting for next week."
    ]

    # Preprocess and predict
    test_tfidf = vectorizer.transform(test_data)
    predictions = model.predict(test_tfidf)

    # Display predictions
    for email, urgency in zip(test_data, predictions):
        print(f"Email: {email}")
        print(f"Predicted Urgency: {urgency}\n")

# Main function
if __name__ == "__main__":
    test_classifier()
