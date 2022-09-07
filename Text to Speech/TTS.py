import pyttsx3

# Initialize pyttsx3
engine = pyttsx3.init()

# Chaning the speed rate
engine.setProperty('rate',150)

engine.say("Hello my name is linux")
engine.runAndWait()
