# Automate Task and Reminder Management

This project is a Python-based solution to automate task reminders and prioritization using the Google Calendar API. It fetches upcoming events, categorizes tasks by urgency, and sends daily notifications to help users stay organized.

## Features

- **Fetch Upcoming Tasks**: Connects to Google Calendar to retrieve tasks and deadlines.
- **Task Prioritization**: Categorizes tasks as "High Priority" or "Low Priority" based on due dates.
- **Daily Notifications**: Sends prioritized task lists via email every day.
- **Customizable Scheduler**: Automates daily reminders at a predefined time using Python's `schedule` library.

## Project Structure

```
Automate-Task-and-Reminder-Management/
├── credentials.json    # Google API credentials for calendar access
├── token.pickle        # Saved authentication token for the Google Calendar API
├── automate_tasks.py   # Main script to fetch, prioritize, and notify
└── README.md           # Documentation file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Prathamesh326/Automate-Task-and-Reminder-Management.git
   cd Automate-Task-and-Reminder-Management
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Google Calendar API:
   - Enable the [Google Calendar API](https://console.cloud.google.com/) on your Google Cloud account.
   - Download the `credentials.json` file and place it in the root directory.

## Usage

1. **Run the script**:
   ```bash
   python automate_tasks.py
   ```

2. The script will:
   - Fetch events from your Google Calendar.
   - Prioritize tasks.
   - Send a detailed task list via email.

3. **Automate daily reminders**:
   The script uses the `schedule` library to send notifications every day at 8:00 AM. You can modify the time in the script.

## Configuration

- **Email Setup**:
  Update the `send_email` function in `automate_tasks.py` with your email credentials.

- **Change Notification Time**:
  Modify the `schedule.every().day.at("08:00").do(main)` line to your preferred time.

## Technologies Used

- **Python**: Core programming language.
- **Google Calendar API**: Fetches event data.
- **SMTP**: Sends email notifications.
- **Schedule**: Automates daily task execution.

## Future Improvements

- Integrate with Slack or Telegram for task notifications.
- Add support for multiple task management platforms like Trello or Notion.
- Implement Natural Language Processing (NLP) for smarter task categorization.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
