import string

def create_files():
    al = string.ascii_uppercase
    for let in al:
        file_name = let + ".txt"
        with open(file_name, 'w') as file:
            file.write("This is file " + file_name)

if __name__ == "__main__":
    create_files()