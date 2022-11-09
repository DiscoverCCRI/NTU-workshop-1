from datetime import datetime

current_time = datetime.now()
print("The current time is: " + str(current_time))

formatted_time = current_time.strftime("%Y-%m-%d_%H:%M:%S")
print("Formatted timestamp: " + str(formatted_time))
