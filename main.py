import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    print("Welcome to the Robot Speaker!")
    while True:
        x = input("Enter what you want to speak : ")
        if x.lower() == "q":
            print("Program terminated.")
            break
        speak(x)
