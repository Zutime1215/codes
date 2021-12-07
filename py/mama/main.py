import speech_recognition as sr
import gtts
import os



r = sr.Recognizer()

with sr.Microphone() as source:

    r.adjust_for_ambient_noise(source, duration=2)
    print("calibrated, say now.")

    audio = r.listen(source)
    myaudio = r.recognize_google(audio)
    myaudio = myaudio.lower()


    if "ok mama" in myaudio:
        strt = gtts.gTTS("hey mama, how can i help you?")
        strt.save("temp-voice.mp3")
        os.system("mpg123 " + "temp-voice.mp3")
        os.remove("temp-voice.mp3")
    print(myaudio)

    
        