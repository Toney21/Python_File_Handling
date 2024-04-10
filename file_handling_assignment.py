def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1.\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 987\n")
        print("File created successfully.")
    except IOError as e:
        print(f"Error creating the file: {e}")
    finally:
        file.close()

def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError as e:
        print(f"Error reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("Another appended line with numbers: 54321\n")
            file.write("Appending one more line for good measure.\n")
        print("Content appended to the file successfully.")
    except PermissionError as e:
        print(f"Error appending to the file: {e}")
    finally:
        file.close()

# Task 1: Create the file
create_file()

# Task 2: Read and display the file
read_and_display_file()

# Task 3: Append to the file
append_to_file()
