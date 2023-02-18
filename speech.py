from win32com.client import constants, Dispatch

def speak(name):
    speaker = Dispatch("SAPI.SpVoice")
    a = f"Shoutout to {name}"
    speaker.Speak(a)
    print(a)

msg = input("enter names with quammas for shoutout: ")
msg = msg.split(",")

for name in msg:
    speak(name)