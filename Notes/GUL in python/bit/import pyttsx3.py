import pyttsx3

text_to_speak = "."


engine = pyttsx3.init()


engine.setProperty('rate', 150)  
engine.setProperty('volume', 0.9) 


engine.say(text_to_speak)

engine.runAndWait() 