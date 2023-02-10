import os
import shutil

def sort_files_by_extension(directory, file_endings):
    """
    Sorts the files in the specified directory by file extension.

    Arguments:
    - directory: The path of the directory to be sorted
    - file_endings: A list of file endings to be sorted

    """
    # Check if the directory is valid
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        return

    # Keep track of the number of files moved per file extension
    files_moved = {}
    # Keep track of the number of files not moved in the directory
    files_not_moved = 0

    # Iterate through all the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if the file is a regular file
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            # Check if the file extension is one of the file endings to be sorted
            if file_extension in file_endings:
                subfolder = os.path.join(directory, file_extension[1:].upper())
                # Create the subfolder if it doesn't exist yet
                if not os.path.exists(subfolder):
                    os.makedirs(subfolder)
                # Move the file to the subfolder
                shutil.move(file_path, os.path.join(subfolder, filename))
                # Increase the count of files moved for this file extension
                files_moved[file_extension] = files_moved.get(file_extension, 0) + 1
            else:
                # Increase the count of files not moved
                files_not_moved += 1

    # Print the number of files moved per file extension
    print("Files moved:")
    for file_extension, count in files_moved.items():
        print(f"{file_extension}: {count}")
    # Print the number of files not moved
    print(f"Files not moved: {files_not_moved}")

# Get the directory to be sorted
directory = input("Enter the directory path: ")
# Get the file endings to be sorted
file_endings = [x.strip() for x in input("Enter the file endings to sort (comma-separated): ").split(',')]
# Call the function to sort the files
sort_files_by_extension(directory, file_endings)
