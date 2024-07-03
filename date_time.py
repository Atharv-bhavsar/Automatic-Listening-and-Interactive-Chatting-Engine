# File to see the current date and time

# Import necessary modules
import ai_speak  # Module for AI voice output
import datetime  # Module for handling date and time
import re  # Module for regular expressions


# Function to display the current date


def current_date():
    # Get the current date
    date = datetime.datetime.now().date()
    # Print the current date
    # print(f"Current Date: {date}")
    # Speak the current date
    # ai_speak.speak(f"Today's date is, {date}")
    return date


# Function to display the current time
def current_time():
    # Get the current time
    time = datetime.datetime.now().time()
    # Format the time as HH:MM
    formatted_time = time.strftime("%H:%M")
    # Print the current time
    # print(f"Current Time: {formatted_time}")
    # Replace colons and commas with spaces in the formatted time
    # formatted_time = re.sub(r'[:,]', ' ', formatted_time)
    # Speak the current time
    # ai_speak.speak(f"The time is, {formatted_time}")
    return formatted_time
