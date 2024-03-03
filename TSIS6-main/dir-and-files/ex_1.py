import os

def list_directories_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all_directories_and_files(path):
    for root, dirs, files in os.walk(path):
        print(f"Directory: {root}")
        print("Files:")
        for file in files:
            print(os.path.join(root, file))
        print()

if __name__ == "__main__":
    path = input()

    print("\n Displaying only directories and files:")
    list_directories_and_files(path)

    print("\n Displaying all directories and files:")
    list_all_directories_and_files(path)