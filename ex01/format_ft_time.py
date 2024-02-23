import time
from datetime import datetime

# Get the current time in seconds since the epoch
current_time = time.time()

# Print the current time in seconds and in scientific notation
print(f"Seconds since January 1, 1970: {current_time} or {current_time:.2e} in scientific notation")

# Get the current date
current_date = datetime.now()

# Print the current date in the format 'Oct 21 2022'
print(current_date.strftime('%b %d %Y'))
