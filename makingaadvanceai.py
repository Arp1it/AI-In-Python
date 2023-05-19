import openai
import win32com.client
import speech_recognition as sr
import webbrowser
import os
import datetime
import subprocess
import random


chatstr = ""
def chat(query):
    global chatstr

    print(chatstr)

    #get api from https://openai.com/api/
    openai.api_key = "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"

    chatstr += f"User: {query}\n Jarvis: "

    print("chatting...")

    try:
        completion = openai.Completion.create(engine="text-davinci-003", prompt=chatstr, max_tokens=1024, n=1, stop=None, temperature=0.7, frequency_penalty = 0, presence_penalty=0)
    except:
        speak("sorry for some reason i exit.")
        exit()

    try:
        responsee = completion.choices[0].text
        speak(responsee)
    except:
        speak("Please say again sir. I don't understand it")

    chatstr += f"{responsee}\n"
    return responsee

    with open(f"Openai/prompt- {random.randint(3, 2233434234)}", "w") as f:
        f.write(text)

def speak(text):
    print(text)
    if len(text)<100:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(text)

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
            # speak(f"You said: {mytext}")
            print(f"You said: {mytext}")

        except Exception as e:
            print(e)

        return mytext

def ai(prompt):
    prompt = prompt.replace("using a i ", "")
    # print(prompt)

    #get api from https://openai.com/api/
    openai.api_key = "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"

    text = f"Openai response for Prompt: {prompt} \n **************\n\n"

    print("...")

    try:
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7, frequency_penalty = 0, presence_penalty=0)
    except:
        speak("sorry for some reason i exit.")
        exit()

    try:
        responsee = completion.choices[0].text
        speak(responsee)
    except:
        speak("Please say again sir. I don't understand it")

    text += responsee

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt- {random.randint(3, 2233434234)}", "w") as f:
        f.write(text)


if __name__ == "__main__":
    speak("Hello sir. I am Jarvis.")

    while True: 
        try:
            mytex = take_voice()
        except:
            speak("Please say again sir.")
            continue

        sites = [["youtube", "https://www.youtube.com/"], ["google", "https://www.google.com/"], ["wikipedia", "https://www.wikipedia.com/"]]

        for site in sites:
            if f"open {site[0]}" in mytex:
                speak(f"{site[0]} is openning...")
                webbrowser.open(site[1])

        if "play music" in mytex:
            music_path = "C:/Users/Windows/Music/downfall-21371.mp3"
            os.startfile(music_path)
            continue

        if "the time" in mytex:
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strftime}")
            continue

        if "open notepad" in mytex:
            speak("openning...")
            subprocess.Popen("C:/Users/Windows/Desktop/mynotepad.exe")
            continue

        t = ["exit", "bye", "goodbye"]
        for i in t:
            if i in mytex:
                speak("Thanks for giving a time sir.")
                exit()

        if "using a i" in mytex:
            ai(mytex)

        if "reset your data" in mytex:
            chatstr = ""

        else:
            chat(mytex)