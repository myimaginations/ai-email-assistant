import random

# Response templates with personalization
response_templates = {
    "High": [
        "We acknowledge the urgency of your request and will prioritize it.",
        "Thank you for your urgent request. We’ll address it immediately.",
        "Your matter is critical, and we’re taking action as soon as possible."
    ],
    "Medium": [
        "Thank you for your email. We’ll get back to you soon.",
        "We’ve received your request and will review it shortly.",
        "Your request is under consideration. Expect a response within 24 hours."
    ],
    "Low": [
        "Thank you for reaching out. We’ll review and respond as needed.",
        "Your email has been noted, and we’ll get back to you in due time.",
        "We’ll address your request soon. Please allow some time for review."
    ]
}

# Add keyword-specific responses
keyword_responses = {
    "meeting": "We’ll schedule a meeting soon. Please suggest your availability.",
    "report": "We’re preparing the required report and will share updates shortly.",
    "update": "Thank you for the update. We’re reviewing the details.",
    "ASAP": "We understand the urgency and will act immediately."
}

def generate_response(email_content, urgency_level):
    """
    Generate a personalized response based on urgency level and keywords.

    Args:
        email_content (str): The email content.
        urgency_level (str): The predicted urgency level (High, Medium, Low).

    Returns:
        str: A generated response.
    """
    # Check for keywords in the email content
    personalized_responses = []
    for keyword, response in keyword_responses.items():
        if keyword.lower() in email_content.lower():
            personalized_responses.append(response)

    # Choose a template response
    template_response = random.choice(response_templates.get(urgency_level, ["Thank you for your email."]))

    # Combine responses
    if personalized_responses:
        final_response = f"{template_response} Additionally: {' '.join(personalized_responses)}"
    else:
        final_response = template_response

    return final_response

# Test the function
if __name__ == "__main__":
    test_email = "We need the report ASAP. Please update me on the progress."
    test_urgency = "High"
    print("Email Content:", test_email)
    print("Generated Response:", generate_response(test_email, test_urgency))
