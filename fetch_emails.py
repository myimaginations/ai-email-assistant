import os
import sys
import pickle
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaInMemoryUpload
from email.mime.text import MIMEText
import base64

# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from app.email_classifier import predict_urgency, generate_response  # Import functions from email_classifier

def create_message(to, subject, body):
    """
    Create a MIMEText email message.
    """
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_message(service, user_id, message):
    """
    Send an email message using the Gmail API.
    """
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"Message sent successfully: {sent_message['id']}")
    except HttpError as error:
        print(f"An error occurred while sending the message: {error}")

def fetch_and_respond():
    # Load credentials from the 'token.pickle' file
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    try:
        # Initialize Gmail API service
        service = build('gmail', 'v1', credentials=creds)

        # Get unread messages
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
        messages = results.get('messages', [])

        if not messages:
            print("No unread messages found.")
            return

        print(f"Unread Messages Count: {len(messages)}")
        for message in messages:
            # Fetch email content
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            snippet = msg.get('snippet', '')
            sender_email = msg['payload']['headers']
            sender = next((item['value'] for item in sender_email if item['name'] == 'From'), None)

            # Print message snippet
            print(f"\nMessage Snippet: {snippet}")

            # Classify the email snippet
            urgency = predict_urgency(snippet)
            print(f"Predicted Urgency: {urgency}")

            # Generate a response based on urgency
            response = generate_response(urgency)
            print(f"Suggested Response: {response}")

            # Send an automated response
            if sender:
                email_message = create_message(sender, "Re: Your Email", response)
                send_message(service, 'me', email_message)

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == '__main__':
    fetch_and_respond()
