from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format into readable form: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:", formatted_date)

    # Return current_date so other parts of the program can use it
    return current_date


def calculate_future_date(current_date):
    # Ask user for number of days
    days = int(input("Enter the number of days to add to the current date: "))

    # Calculate future date
    future_date = current_date + timedelta(days=days)

    # Format it as YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")

    print("Future date:", formatted_future)


today = display_current_datetime()
calculate_future_date(today)
