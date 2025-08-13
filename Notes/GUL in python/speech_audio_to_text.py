# Speech_aidio_to_text

'''import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    try:
        audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")


# Speech_text_to_audio

import pyttsx3

text_to_speak = "This is an example of text to speech using pyttsx3."

# Initialize the engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

# Convert text to speech
engine.say(text_to_speak)

# Play the speech
engine.runAndWait()'''

# search for web

import pyttsx3
import speech_recognition as sr
import webbrowser as wb


def speak(text_to_speak):
    engine = pyttsx3.init()
    engine.say(text_to_speak)
    engine.runAndWait()

def voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return " Sorry, could not understand audio."
        except sr.RequestError:
            return " Could not request results from Google Speech Recognition service."

text=voice()
print(text)
if text=="hi":
    speak("hello, welcome to livewire")
elif "search" in text.lower():
    wb.open("https://www.google.com/search?q="+text)

