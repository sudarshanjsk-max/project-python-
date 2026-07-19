import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Queue the text you want the computer to say
engine.say("hi my name is Sudarshan and my favourite anime is solo leveling")

# Process and run the speech commands
engine.runAndWait()

import os

# specify the path (use "." for current directory)
path = "/New folder"
# list all files and folders in the directory
contents = os.listdir(path)

# print them one by one
for item in contents:
    print(item)
