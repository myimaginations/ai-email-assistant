import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Preprocess email content
def preprocess_email_content(text):
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(cleaned_tokens)

# Load a subset of the dataset
def load_data():
    # Load the first 100,000 rows of the dataset
    data = pd.read_csv('data/emails.csv', nrows=100000)
    
    # Display the first few rows
    print(f"Loaded {len(data)} rows from the dataset:")
    print(data.head())
    return data

# Clean the dataset
def clean_data(data):
    # Drop rows with missing 'message' values
    data = data.dropna(subset=['message'])
    
    # Apply text preprocessing to the email messages
    data['cleaned_content'] = data['message'].apply(preprocess_email_content)
    
    return data

# Save the cleaned subset
def save_subset(cleaned_data):
    cleaned_data.to_csv('data/emails_subset.csv', index=False)
    print("Subset saved successfully as 'emails_subset.csv'!")

# Load, clean, and save the subset
def load_and_clean_data():
    data = load_data()
    cleaned_data = clean_data(data)
    return cleaned_data

# Main function
if __name__ == "__main__":
    # Load and clean the subset
    cleaned_data = load_and_clean_data()
    print("Cleaned data preview:")
    print(cleaned_data.head())
    
    # Save the cleaned subset to a new CSV file
    save_subset(cleaned_data)
