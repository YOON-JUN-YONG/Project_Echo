import requests
from bs4 import BeautifulSoup
import re

def test(s):

    hangul = re.compile('[^ ㄱ-ㅣ가-힣|.]+') # 한글과 띄어쓰기를 제외한 모든 글자

    result_hangul = hangul.sub('', s) # 한글과 띄어쓰기를 제외한 모든 부분을 제거

    Hangul = result_hangul.replace("   ", "")

    List_hangul = list(Hangul)

    for i in range(0,len(List_hangul)):

        if List_hangul[i] == '.':

            del List_hangul[i+1:]

            break

    joined_hangul = "".join(List_hangul)

    return joined_hangul


req = requests.get("https://ko.wikipedia.org/wiki/한국성서대학교")

html = req.text

Soup = BeautifulSoup(html, 'html.parser')

if Soup.find('p').findAll('span'):

    result = Soup.findAll('p')[1]

    print(test(result.text))

else:

    result = Soup.find('p')

    print(test(result.text))
