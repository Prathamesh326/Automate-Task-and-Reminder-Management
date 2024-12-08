import datetime
import smtplib
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os
import pickle

# Authenticate with Google Calendar API
def get_calendar_events():
    creds = None
    # Load credentials from a file
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes=['https://www.googleapis.com/auth/calendar.readonly']
            )
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Connect to Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    # Fetch events
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    return events

# Prioritize tasks
def prioritize_events(events):
    high_priority = []
    low_priority = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_time = datetime.datetime.fromisoformat(start[:-1])  # Convert ISO format to datetime
        hours_left = (event_time - datetime.datetime.utcnow()).total_seconds() / 3600
        if hours_left <= 24:  # Due within 24 hours
            high_priority.append(event['summary'])
        else:
            low_priority.append(event['summary'])
    return high_priority, low_priority

# Send email notification
def send_email(high_priority, low_priority):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_password"

    subject = "Your Daily Task List"
    body = "Here are your prioritized tasks:\n\n"

    body += "High Priority:\n" + "\n".join(high_priority) + "\n\n"
    body += "Low Priority:\n" + "\n".join(low_priority) + "\n"

    # Set up the email server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        email_message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, email_message)

# Main function
def main():
    events = get_calendar_events()
    high_priority, low_priority = prioritize_events(events)
    send_email(high_priority, low_priority)

if __name__ == "__main__":
    import schedule
    import time

    # Schedule the script to run daily at 8 AM
    schedule.every().day.at("08:00").do(main)

    print("Task Reminder is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)