#always listen and look for keyword to initiate 
import pyaudio
import speech_recognition as sr 
r = sr.Recognizer()

with sr.Microphone as src:
    audio = r.listen(src)

def always_listen():
    #def keyword
    kw = "Hey doc"
    audio = r.recognize_google(src)
    
    if audio==kw:
        print("Hello, How can i help you feel better today?")
        audio = r.recognize_google(src)
        print(audio)
}

while True:
    always_listen()