from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted)
    return current_date

def calculate_future_date(current_date):
    days_to_add = input("Enter the number of days to add to the current date: ")
    future_date = current_date + timedelta(days= days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date 