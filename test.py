import speech_recognition as sr

# create a recognizer
r = sr.Recognizer()
mic = sr.Microphone()

L=''
while L=='':
    print('say something')
    with mic as source:
        audio = r.listen(source)
    try:
        L=r.recognize_google(audio)
    except sr.UnknownValueError:
        print('Sorry we didnt capture your words')
print(L)
if L == 'hello':
    print('hey pal')
elif L!='': print('nothing')
elif L=='':print('empty')