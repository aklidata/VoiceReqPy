import subprocess
import gtts
from gtts import gTTS
import os
from tempfile import TemporaryFile
#mytext = "Welcome! How can I help you? I am your virtual doctor."
mytext = "Bonjour! puis-je vous aider ? ?"
language = 'fr'

myobj = gTTS(text = mytext, lang = language, slow=False)

#f = TemporaryFile()
myobj.save("f.mp3")
#Play f 
#f.close()
os.system('mpg321 f.mp3')

"""
import pyttsx3
import os
engine = pyttsx3.init()
def SayText(text):
    engine.say(text)
    engine.setProperty('rate,120')
    engine.setProperty('volume',0.9)
    engine.runAndWait()
SayText("Hello, How can i help you feel better today")"""
