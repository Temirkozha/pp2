from datetime import datetime

current_data = datetime.now()

new_data = current_data.replace(microsecond = 0)

print(current_data)
print(new_data)