import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import requests
from bs4 import BeautifulSoup
import re


def TTS(speak):
    text = speak

    tts = gTTS(text=text, lang='ko')

    tts.save("Hello.mp3")

    playsound("Hello.mp3")

    os.remove('Hello.mp3')


def search_result(speak):
    List = list(speak)

    for i in range(0, len(List)):

        if List[i] == '검' and List[i + 1] == '색' and List[i + 2] == '해' and List[i + 4] == '줘':
            return True

    return False


def search_contents(speak):
    List = list(speak)

    for i in range(0, len(List)):

        if List[i] == '검' and List[i + 1] == '색' and List[i + 2] == '해' and List[i + 4] == '줘':
            del List[i:]

            break

    joined_str = "".join(List)

    return joined_str


def convert(s):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣|.]+')  # 한글과 띄어쓰기를 제외한 모든 글자

    result_hangul = hangul.sub('', s)  # 한글과 띄어쓰기를 제외한 모든 부분을 제거

    Hangul = result_hangul.replace("   ", "")

    List_hangul = list(Hangul)

    for i in range(0, len(List_hangul)):

        if List_hangul[i] == '.':
            del List_hangul[i + 1:]

            break

    joined_hangul = "".join(List_hangul)

    return joined_hangul


def wiki(text):
    req = requests.get("https://ko.wikipedia.org/wiki/" + text)

    html = req.text

    Soup = BeautifulSoup(html, 'html.parser')

    if Soup.find('p').findAll('span'):

        result_wiki = Soup.findAll('p')[1]

        return convert(result_wiki.text)

    else:

        result_wiki = Soup.find('p')

        return convert(result_wiki.text)


def recognizing():
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:

        audio = r.listen(source)

    try:
        result = r.recognize_google(audio, language='ko-KR')

        return result

    except Exception:

        print("error")

        return False


while True:

    Mike = recognizing()

    if Mike == "에코":
        TTS("네 말씀하세요")

        Echo_mike = recognizing()

        if search_result(Echo_mike):
            contents = search_contents(Echo_mike)

            final_result = wiki(contents)

            print(final_result)

            TTS(contents + "에 대하여 검색합니다.")

            TTS(final_result)

            continue

        else:

            continue

    elif Mike == "에코 안녕":
        TTS("안녕하세요")

        continue

    else:

        continue
