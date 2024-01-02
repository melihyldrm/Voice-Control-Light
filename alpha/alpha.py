import re
import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)
        command = ""
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        return command


def parse_command(command):
    # Using regular expressions to extract relevant information
    match = re.search(r'(light|open|search|play)\s+(\w+)', command)
    if match:
        action = match.group(1)
        query = match.group(2)
        return action, query
    else:
        return None, None


def perform_action(action, query):
    if action == 'open':
        if query.lower() == 'youtube':
            webbrowser.open('https://www.youtube.com/')
        elif query.lower() == 'best':
            webbrowser.open('https://www.youtube.com/watch?v=J_novHlMsV0')
        # Add more 'open' commands for other applications or websites
    elif action == 'light':
        if query.lower() == 'on':
            webbrowser.open('http://192.168.144.73/on')
        elif query.lower() == 'off':
            webbrowser.open('http://192.168.144.73/off')

if __name__ == "__main__":
    speak("konus")
    while True:
        command = take_command()
        action, query = parse_command(command)

        if action:
            perform_action(action, query)
        elif any(word in command for word in ["exit", "stop", "quit"]):
            speak("Good Bye")
            break
        else:
            print("Recognized command:", command)
            speak("Please try again.")

