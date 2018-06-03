import speech_recognition as sr

# create a recognizer
r = sr.Recognizer()
mic = sr.Microphone()


print('Bonjour')
def inquire(x):
    L= x
    while L=='':

        with mic as source:
            audio = r.listen(source)
        try:
            L=r.recognize_google(audio,language='fr-FR')
        except sr.UnknownValueError:
            print('Desole, je n\'ai rien compris')
    if L!='Bonjour':print(L)
    return L
L = inquire('')


if L == 'Bonjour':
    print('Est ce que je peux vous aider?')
    inquire('')
#elif L!='': print('Vous N\'avais rien dit')
#elif L=='':print('Vide')