import requests
import json
from colorama import init
from termcolor import colored
from datetime import datetime
import re

# Initialize colorama
init(autoreset=True)

# Define URLs of our Flask app
PREDICT_URL = "http://127.0.0.1:5000/predict"
SCHEDULE_URL = "http://127.0.0.1:5000/schedule"

def get_answer_from_chatbot(question):
    """Send a question to the chatbot API and return the response."""
    payload = {"text": question}
    headers = {"Content-Type": "application/json"}

    try:
        # Send POST request to Flask API
        response = requests.post(PREDICT_URL, json=payload, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            answer = response.json().get('response')
            return answer
        else:
            error_message = response.json().get('error', "An error occurred.")
            return f"Error: {error_message}"
    except requests.exceptions.RequestException as e:
        return f"Failed to connect to the server: {e}"

def print_bubble(text, is_user=True):
    """Print text in a bubble-like format."""
    if is_user:
      # User's message in blue, left-aligned
        print(colored(f"[User]  {text}", "blue"))
    else:
        # Bot's response in green, right-aligned
        print(colored(f"[Bot]  {text}", "green"))

def validate_email(email):
    """Basic email validation."""
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email)

def validate_phone(phone):
    """Basic phone number validation (international formats)."""
    phone_regex = r"^\+?1?\d{9,15}$"
    return re.match(phone_regex, phone)

def validate_date(date_text):
    """Validate date format YYYY-MM-DD."""
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_time(time_text):
    """Validate time format HH:MM in 24-hour format."""
    try:
        datetime.strptime(time_text, '%H:%M')
        return True
    except ValueError:
       return False

def schedule_appointment():
    """Function to collect appointment details from the user."""
    print(colored("\nLet's schedule your appointment. Please provide the following details.", "cyan"))

    # Collect patient details
    name = input(colored("Enter your name: ", "yellow")).strip()
    phone = input(colored("Enter your phone number (e.g., +1234567890): ", "yellow")).strip()
    email = input(colored("Enter your email: ", "yellow")).strip()
    date = input(colored("Enter preferred date (YYYY-MM-DD): ", "yellow")).strip()
    time = input(colored("Enter preferred time (HH:MM in 24-hour format): ", "yellow")).strip()
    description = input(colored("Describe your problem: ", "yellow")).strip()

    # Validate inputs
    errors = []
    if not name:
        errors.append("Name cannot be empty.")
    if not phone or not validate_phone(phone):
        errors.append("Invalid phone number format.")
    if not email or not validate_email(email):
        errors.append("Invalid email address format.")
    if not date or not validate_date(date):
        errors.append("Invalid date format. Use YYYY-MM-DD.")
    if not time or not validate_time(time):
        errors.append("Invalid time format. Use HH:MM in 24-hour format.")
    if not description:
      errors.append("Problem description cannot be empty.")

    if errors:
        for error in errors:
            print_bubble(error, is_user=False)
        return

    # Prepare the payload
    payload = {
        "name": name,
        "phone": phone,
        "email": email,
        "date": date,
        "time": time,
        "description": description
    }

    headers = {"Content-Type": "application/json"}

    try:
        # Send POST request to /schedule endpoint
        response = requests.post(SCHEDULE_URL, json=payload, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            bot_response = data.get('response', "Your appointment has been scheduled.")
            print_bubble(bot_response, is_user=False)
        else:
          # Handle errors returned by the backend
            data = response.json()
            error_message = data.get('error', "An error occurred while scheduling your appointment.")
            print_bubble(f"Error: {error_message}", is_user=False)
    except requests.exceptions.RequestException as e:
        print_bubble(f"Failed to connect to the server: {e}", is_user=False)

def main():
    print(colored("Good day! Welcome, I am designed by Tosin, Shemaa, and Rihab. How can I help you today?", "magenta"))
    print(colored("Type 'exit' to quit or 'schedule' to book an appointment.", "yellow"))

    while True:
        # Get user input from the terminal
        user_input = input(colored("You: ", "yellow")).strip()

        # Exit condition
        if user_input.lower() == "exit":
            print(colored("Thank you! Goodbye!", "magenta"))
            break

        # Appointment scheduling option
        elif user_input.lower() == "schedule":
            schedule_appointment()
            continue

        # Print user's input as chat bubble
        print_bubble(user_input, is_user=True)

        # Get the answer from the Flask API
        answer = get_answer_from_chatbot(user_input)

        # Print bot's response as chat bubble
        print_bubble(answer, is_user=False)

if __name__ == "__main__":