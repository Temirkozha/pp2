def copy_file(s_f, d_f):
    try:
        with open(s_f, 'r') as source:
            with open(d_f, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully")
    except FileNotFoundError:
        print("One of the files does not exist")
    except IOError:
        print("An error occurred while copying the file")

if __name__ == "__main__":
    source_file = input()
    destination_file = input()

    copy_file(source_file, destination_file)