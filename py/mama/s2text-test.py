import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:

    r.adjust_for_ambient_noise(source, duration=2)
    print("calibrated, say now.")

    audio = r.listen(source)
    myaudio = r.recognize_google(audio)
    myaudio = myaudio.lower()
    print(myaudio)