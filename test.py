import speech_recognition as sr

# create a recognizer
r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
L=''
while L=='':
    print('Hello tell me how you\'re feeling today')
    with mic as source:
        audio = r.listen(source)
    try:
        L=r.recognize_google(audio)
    except sr.UnknownValueError:
        print('Sorry I could not hear you. Could you please repeat?')
print("I will try and help you with".L)
