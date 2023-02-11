import openai
import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voicess = engine.getProperty('voices')
engine.setProperty('voice', voicess[1].id)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")

        try:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            print("Recognizing...")
            mytext = r.recognize_google(audio, language="en-in")
            mytext = mytext.lower()
            speak(f"You said: {mytext}")

        except Exception as e:
            print(e)

        return mytext

#get api from https://openai.com/api/
openai.api_key = "your_api_key"

while True:
    model_engine = "text-davinci-003"

    try:
        mytex = take_voice()
        print(mytex)
    except:
        speak("please say again sir...")
        continue

    # promptt = input("Enter: ")

    if mytex == 'exit' or mytex == 'quit' or "bye" in mytex:
        speak("Thanks for giving a time sir")
        break

    if "open youtube" == mytex:
        speak("youtube is openning...")
        webbrowser.open("https://www.youtube.com/")
        continue


    completion = openai.Completion.create(engine=model_engine, prompt=mytex, max_tokens=1024, n=1, stop=None, temperature=0.5)

    responsee = completion.choices[0].text

    speak(responsee)