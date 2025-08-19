
def read_and_modify_file(filename):
    #Read content from a file, modifies it, and writes to output.txt."
    with open(filename, "r") as infile:
        content = infile.read()

    #To overwrite file
    with open("output.txt", "w") as outfile:
        outfile.write("Hello world! ")

    print("\n✅ File has been read and modified content saved to 'output.txt'")


def main():
    #Main function to handle user input and errors.
    try:
        # Ask user for a filename
        filename = input("Enter the filename to read: ")

        # Process the file
        read_and_modify_file(filename)

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
