import gtts
import os

tts = gtts.gTTS("hey, whats'up?")
tts.save("temp-voice.mp3")
os.system("mpg123 " + "temp-voice.mp3")
os.remove("temp-voice.mp3")
