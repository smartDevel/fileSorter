# File Sorter

This script sorts files in a directory into sub-folders by file extension. The file endings to be sorted are queried as input parameters. Not specified file endings will not be moved. The number of files moved per file extension and the number of files not moved in the directory will also be specified.

## Usage

To use the script, run it from the command line and provide the following inputs:

- The path of the directory to be sorted
- A list of file endings to be sorted, separated by commas

The script will then sort the files in the directory and print the number of files moved per file extension and the number of files not moved.

## Example


Enter the directory path: /path/to/directory
Enter the file endings to sort (comma-separated): .txt, .jpg, .png
Files moved:
.txt: 3
.jpg: 2
.png: 1
Files not moved: 4

In this example, 3 .txt files, 2 .jpg files, and 1 .png file were moved to sub-folders named TXT, JPG, and PNG, respectively. There were 4 files in the directory that had file endings other than .txt, .jpg, or .png and were not moved.