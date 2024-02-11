from datetime import datetime, timedelta

current_data = datetime.now()

new_data = current_data - timedelta(days = 5)

print("The current date:", current_data)
print("Date after minus five days:", new_data)