from datetime import datetime

# Test for blog post
datetime.now().strftime('%A')

# Current date and time
now = datetime.now()

# Format the date and time as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)

# Parse a string and convert it to a datetime object
date_string = "2022-01-01 12:00:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed_date)