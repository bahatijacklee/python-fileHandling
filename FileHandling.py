def read_and_modify_file():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")
    
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            # Read the file content
            content = file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()  # or any other modification you like
        
        # Define the new filename for the modified content
        new_filename = "modified_" + filename
        
        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please check the file permissions or try another file.")

# Run the function
read_and_modify_file()
