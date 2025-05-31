import datetime
current_time = datetime.datetime.now()
print(f"The current date and time is: {current_time}")
print(f"The current dae in MM-DD-YYYY format is: {current_time.strftime("%x")}")
print(f"The current number of the weekday is: {current_time.strftime("%w")}")
print(f"The current name of the weekday is: {current_time.strftime("%A")}")
