import pandas as pd

# Function to add urgency labels
def label_emails():
    # Load the subset dataset
    data = pd.read_csv('data/emails_subset.csv')

    # Define a simple labeling function
    def assign_urgency(content):
        if "urgent" in content.lower() or "asap" in content.lower():
            return "High"
        elif "important" in content.lower():
            return "Medium"
        else:
            return "Low"

    # Apply the labeling function to cleaned content
    data['urgency'] = data['cleaned_content'].apply(assign_urgency)

    # Save the labeled dataset
    data.to_csv('data/emails_labeled.csv', index=False)
    print("Emails labeled and saved successfully as 'emails_labeled.csv'!")

# Main function
if __name__ == "__main__":
    label_emails()
