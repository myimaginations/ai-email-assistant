import streamlit as st
import pandas as pd
from email_classifier import predict_urgency, generate_response
import os

# App title
st.title("AI Email Assistant")
st.write(
    "This AI-powered tool classifies email urgency levels, suggests responses, and allows bulk email classification with feedback options."
)

# Email content input for single email classification
st.subheader("Single Email Classification")
email_content = st.text_area("Enter email content:", height=200, key="single_email")

if st.button("Classify Urgency"):
    if email_content.strip():
        # Predict urgency and response for single email
        urgency = predict_urgency(email_content)
        response = generate_response(urgency)

        st.write(f"**Predicted Urgency:** {urgency}")
        st.write(f"**Suggested Response:** {response}")
    else:
        st.warning("Please enter some email content to classify.")

# Bulk Email Classification
st.subheader("Bulk Email Classification")
uploaded_file = st.file_uploader("Upload a CSV file with an 'email_content' column", type=["csv"], key="bulk_email")

if uploaded_file is not None:
    try:
        # Load and display uploaded CSV file
        df = pd.read_csv(uploaded_file)

        if 'email_content' in df.columns:
            # Predict urgency and generate responses for all emails
            df['Predicted Urgency'] = df['email_content'].apply(predict_urgency)
            df['Suggested Response'] = df['Predicted Urgency'].apply(generate_response)

            st.write("**Sorted Emails by Urgency**")
            st.dataframe(df)

            # Downloadable processed CSV file
            st.download_button(
                label="Download Sorted Emails as CSV",
                data=df.to_csv(index=False),
                file_name="sorted_emails.csv",
                mime="text/csv"
            )
        else:
            st.error("The uploaded file must contain an 'email_content' column.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Feedback section 1
st.subheader("Provide Feedback for Single Email")
st.write("Do you agree with the predicted urgency and response? If not, suggest improvements.")
feedback_single = st.text_area("Provide your feedback here:", height=100, key="feedback_single")

if st.button("Submit Feedback for Single Email"):
    if feedback_single.strip():
        # Save feedback to a CSV file
        feedback_file = "feedback.csv"

        # Check if the feedback file exists
        if not os.path.exists(feedback_file):
            # Create a new file with headers if it doesn't exist
            with open(feedback_file, "w") as f:
                f.write("Feedback\n")

        # Append the feedback to the file
        with open(feedback_file, "a") as f:
            f.write(f"{feedback_single}\n")

        st.success("Thank you for your feedback! It has been recorded.")
    else:
        st.warning("Please provide feedback before submitting.")

# Feedback section 2
st.subheader("Provide General Feedback")
st.write("Do you have any general feedback or suggestions?")
feedback_general = st.text_area("Provide your feedback here:", height=100, key="feedback_general")

if st.button("Submit General Feedback"):
    if feedback_general.strip():
        # Save feedback to a CSV file
        feedback_file = "general_feedback.csv"

        # Check if the feedback file exists
        if not os.path.exists(feedback_file):
            # Create a new file with headers if it doesn't exist
            with open(feedback_file, "w") as f:
                f.write("Feedback\n")

        # Append the feedback to the file
        with open(feedback_file, "a") as f:
            f.write(f"{feedback_general}\n")

        st.success("Thank you for your general feedback! It has been recorded.")
    else:
        st.warning("Please provide feedback before submitting.")
