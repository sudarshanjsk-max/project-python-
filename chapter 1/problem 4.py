import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Queue the text you want the computer to say
engine.say("sudarshan is a good boy")

# Process and run the speech commands
engine.runAndWait()
    


import os

# specify the path (use "." for current directory)
path = "./New folder"
# list all files and folders in the directory
contents = os.listdir(path)

# print them one by one
for item in contents:
    print(item)
    print("is a file" if os.path.isfile(os.path.join(path, item)) else  " is a folder")
    # file modified to pyttsx3 to say the name of the file or folder
    engine .say(item)