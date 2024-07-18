import time
import speech_recognition
import pyttsx3
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


timestamp=time.strftime("%H:%M:%S")
hour=time.strftime("%H")
minute=time.strftime("%M")
second=time.strftime("%S")
print(timestamp)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


name=input("Enter your name: ")
if(hour>="04" and hour<="11"):
    speak(f"Good Morning {name}")
    print(f"Good Morning {name}")
elif(hour>="12" and hour<="16"):
    speak(f"Good Afternoon {name}")
    print(f"Good Afternoon {name}")
elif(hour>="17" and hour<="20"):
    speak(f"Good Evening {name}")
    print(f"Good Evening {name}")
else:
    speak(f"Good Night {name}, Sweet Dreams, Bye {name}")
    print(f"Good Night {name}")