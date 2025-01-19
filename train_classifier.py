import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# Train urgency classifier
def train_urgency_classifier():
    # Load labeled dataset
    data = pd.read_csv('data/emails_labeled.csv')

    # Features and labels
    X = data['cleaned_content']
    y = data['urgency']

    # Text vectorization using TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X_tfidf = vectorizer.fit_transform(X)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save the trained model and vectorizer
    with open('models/urgency_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    with open('models/tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    print("Model and vectorizer saved successfully!")

# Main function
if __name__ == "__main__":
    train_urgency_classifier()
