import os

def del_file(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted")
        except PermissionError:
            print(f"You do not have permission to delete '{file_path}'")
        except OSError as e:
            print(f"Error occurred while deleting '{file_path}': {e}")
    else:
        print(f"The file '{file_path}' does not exist")

if __name__ == "__main__":
    file_path = input()
    del_file(file_path)