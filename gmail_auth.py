import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# The updated scope for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    """Authenticate the user and save credentials for Gmail API."""
    creds = None
    # Check if token.pickle exists for saved credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials, authenticate the user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Make sure the `credentials.json` is in the same directory as this script
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)  # Fixed port to avoid random URI issues

        # Save the credentials for future use
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            print("Authentication successful. Credentials saved to 'token.pickle'.")

if __name__ == '__main__':
    main()
