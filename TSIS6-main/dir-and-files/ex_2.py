import os

def check(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist")
        return

    if os.access(path, os.R_OK):
        print(f"Path '{path}' is readable")
    else:
        print(f"Path '{path}' is not readable")
    
    
    if os.access(path, os.W_OK):
        print(f"Path '{path}' is writable")
    else:
        print(f"Path '{path}' is not writable")
    

    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable")
    else:
        print(f"Path '{path}' is not executable")

path_check = "/path/to/your/file_or_directory"
check(path_check)