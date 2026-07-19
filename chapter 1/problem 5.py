import os  # Import the operating system module

# Specify the path of the directory (here '.' means current directory)
path = "."

# Get a list of all files and folders in the directory
contents = os.listdir(path)

# Print each item in the directory
for item in contents:
    print(item)
