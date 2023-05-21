import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-20)
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    while True:
        x = input("Enter what do you want me to speak: ")
        speak(x)