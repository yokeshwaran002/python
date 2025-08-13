import pyttsx3

text_to_speak = "welcome to great show."


engine = pyttsx3.init()


engine.setProperty('rate', 160)
engine.setProperty('volume', 0.9) 


engine.say(text_to_speak)

engine.runAndWait() 