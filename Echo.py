import speech_recognition as sr

import os

from gtts import gTTS

from playsound import playsound


def TTS(speak):

    text = speak

    tts = gTTS(text=text, lang='ko')

    tts.save("Hello.mp3")

    playsound("Hello.mp3")

    os.remove('Hello.mp3')


while True:

    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:

        audio = r.listen(source)

    try:
        result = r.recognize_google(audio, language='ko-KR')

    except Exception:

        print("error")

    else:

        print(type(result))

        if result == "에코":

            TTS("네 말씀하세요")


