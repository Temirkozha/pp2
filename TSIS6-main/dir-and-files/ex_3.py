import os

def analyze(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists")

        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist")

path = "/path/to/your/file_or_directory"
analyze(path)