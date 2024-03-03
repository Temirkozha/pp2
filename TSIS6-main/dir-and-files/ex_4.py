def Count(file_path):
    try:
        with open(file_path, "r") as file:
            line_count = 0
            for x in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        return -1

file_path = "ex_8.py"
num_line = Count(file_path)
if num_line != -1:
    print(f"Number of lines in '{file_path}': {num_line}")