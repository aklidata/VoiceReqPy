import speech_recognition as sr

# create a recognizer
r = sr.Recognizer()
mic = sr.Microphone()

L=''
while L=='':
    print('Bonjour!')
    with mic as source:
        audio = r.listen(source)
    try:
        L=r.recognize_google(audio,language='fr-FR')
    except sr.UnknownValueError:
        print('Desole, je n\'ai rien compris')
print(L)
if L == 'Bonjour':
    print('Est ce que je peux vous aider?')
elif L!='': print('Vous N\'avais rien dit')
elif L=='':print('empty')