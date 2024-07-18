# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce:
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()