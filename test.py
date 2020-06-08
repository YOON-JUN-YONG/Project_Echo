import speech_recognition as sr

import os

from gtts import gTTS

from playsound import playsound


text = "안녕하세요제이름은윤준용입니다"

tts = gTTS(text=text, lang='ko')

tts.save("Hello.mp3")

playsound("Hello.mp3")

os.remove('Hello.mp3')