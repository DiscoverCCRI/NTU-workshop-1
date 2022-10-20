### Once a timestamp has been printed, try to reformat the timestamp with .strftime()
### For example: ‘2022-10-20 09:33:35.990909’ --> ‘2022-10-20_09:33:35’

from datetime import datetime

current_time = datetime.now()
print("The current time is: " + str(current_time))

# formatted_time = current_time.strftime("...")
# print("Formatted timestamp: " + str(formatted_time))
