def read_file(filename):
    """Read the contents of a file and return it."""
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

def main():
    filename = input("Enter the filename to read and write: ")

    try:
         Attempt to read the input file
        content = read_file(filename)
        print("File read successfully.")

        Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

         Write the modified content back to the same file
        write_file(filename, modified_content)
        print(f"Modified content written back to {filename} successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
