from tkinter import *
from tkinter.ttk import *
from bs4 import BeautifulSoup
import lxml
import webbrowser
import tkinter.messagebox

global Name_abstract, Name_title # 전역변수 저장

def URL():
    url = "https://ko.wikipedia.org/wiki/" + txt.get() # 인터넷 연결 시 들어갈 url

    webbrowser.open(url) #url 연결


def Search(Name_title, Name_abstract): # 검색 결과 출력 GUI 함수

    ## Window2
    Window2 = Tk()
    Window2.title("위키피디아")
    Window2.resizable(width=FALSE, height=FALSE)

    result = Message(Window2, text=Name_title, width = 300, font=15)
    result.pack(padx=10, pady=10) # 검색한 내용의 title을 출력

    result2 = Message(Window2, text = Name_abstract, width = 300, font=15)
    result2.pack() # 검색한 내용을 message를 통해 여러줄로 출력

    empty = Label(Window2)
    empty.pack() # 여백의 미

    Search_Button1 = Button(Window2, text="인터넷에서 검색", command=URL)
    Search_Button1.pack(side = RIGHT, padx=10, pady=10) # 인터넷을 연결하여 위키백과 검색결과를 보여주는 버튼

    Window2.mainloop()


def NotFound(): # 검색결과가 없을 경우 실행되는 GUI 함수

    # NotFound 함수안에 함수를 정의 했는데 Window3를 읽기 위해서 안으로 들여보냄
    # NEW가 밖에 있으면 Window3를 읽지 못함
    # 같은 이유로 NEW 안에도 함수를 정의했는데 entry에 입력한 내용을 get하기 위해 들여 보냈다.

    def NEW():  # 위키피디아 파일 안에 없는 내용을 추가하기 위한 GUI함수

        Window3.destroy()

        Window4 = Tk()
        Window4.title("위키피디아")
        Window4.geometry('550x450')
        Window4.resizable(width=FALSE, height=FALSE)  # 기본 프레임

        def Append():  # 정보 추가 함수

            ## Append 함수 부분
            if input_title.get() == "" or input_abstract.get() == "":

                tkinter.messagebox.showinfo("위키피디아", "내용을 전부 입력해주세요")

            else:
                File = open('example.xml', 'a', encoding='UTF8')

                File_content = "\n<doc>\n" \
                               "<title>위키백과: " + input_title.get() + "</title>\n" \
                                "<url></url>\n" \
                                "<abstract>" + input_abstract.get() + "</abstract>\n"\
                                "</doc>"
                # get()을 통해 entry로 입력한 값을 불러옴

                File.write(File_content)  # xml 파일에 append로 내용 추가

                File.close()

                Window4.destroy()

                tkinter.messagebox.showinfo("위키피디아", "저장되었습니다\n프로그램을 재시작 해주세요")
                # beautifulsoup parsing을 main 창 실행 전에 하기 때문에 새로 저장된 내용을 반영하기 위해
                # 프로그램 재시작 요구

        ## NEW 함수 부분, Window4
        frame1 = Frame(Window4)
        frame1.pack(fill=X)  # 프래임 묶음

        txt_title = Label(frame1, text="제목", width=10)
        txt_title.pack(side=LEFT, padx=10, pady=10)

        input_title = Entry(frame1, textvariable=TXT)
        input_title.pack(fill=X, padx=10, expand=True)  # 추가할 내용의 제목을 입력

        frame3 = Frame(Window4)
        frame3.pack(fill=BOTH, expand=True)  # 프래임 묶음

        txt_abstract = Label(frame3, text="내용", width=10)
        txt_abstract.pack(side=LEFT, anchor=N, padx=10, pady=10)

        input_abstract = Entry(frame3)
        input_abstract.pack(fill=BOTH, expand=True, pady=10, padx=10)  # 추가할 내용 입력

        frame4 = Frame(Window4)
        frame4.pack(fill=X)

        txt_Save = Button(frame4, text="저장", command=Append)
        txt_Save.pack(side=RIGHT, padx=10, pady=10)  # 저장 버튼을 눌러 Append 함수를 불러와 저장

        Window4.mainloop()


    ## NotFound 함수 부분, Window3
    Window3 = Tk()
    Window3.title("위키피디아")
    Window3.geometry('300x200')
    Window3.resizable(width=FALSE, height=FALSE)

    empty = Label(Window3)
    empty.pack() # 여백의 미

    Not = Label(Window3, text="입력된 검색어를 찾을 수 없습니다", font=15)
    Not.pack(padx=10, pady=10) # 입력된 검색어가 없다는 안내문 출력

    empty2 = Label(Window3)
    empty2.pack() # 여백의 미

    frame = Frame(Window3)
    frame.pack(fill = X) # 프레임 묶음

    Search_Button2 = Button(frame, text="인터넷에서 검색", command=URL)
    Search_Button2.pack(padx=10, pady=10)

    Search_Button3 = Button(frame, text = "새로운 내용 추가", command=NEW)
    Search_Button3.pack(padx = 10, pady=10) # 인터넷에서 검색할지 자신이 새로운 내용을 추가할지 선택

    Window3.mainloop()


def finding(): # 검색 함수

    NOF = 0 # 결과의 유무 판별 변수

    Title = "위키백과: " + txt.get()
    # xml파일에서는 title이 "위키백과: ~~" 로 나오기 때문에 설정

    for title in Soup.findAll('title'):

        print(title.string)
        print(title)

        if title.string == Title: # 검색 결과가 있을 때

            title.parent # title의 부모 트리인 doc 호출

            abstract = title.parent.abstract
            # title의 부모인 doc로 간 후 doc의 또 다른 자식 트리인 abstract 호출

            Name_title = title.string
            Name_abstract = abstract.string # title 과 abstract를 string 으로 저장

            NOF = 1

    if NOF == 1: # 결과가 있을 때

        return Search(Name_title, Name_abstract) # Search() 함수 호출

    elif NOF == 0: # 결과가 없을 때

        return NotFound() # NotFound() 함수 호출

## Main Window
Window = Tk()
TXT = StringVar()
Window.title("위키피디아")
Window.geometry('500x400')
Window.resizable(width=FALSE,height=FALSE) # Main 윈도우 창 (창을 늘릴 수 없게 설정)

file = open('example.xml', encoding='UTF8') # cp949로 인코딩 되어있는 xml 파일을 UTF8로 변경&열기

XML = file.read()

Soup = BeautifulSoup(XML, "lxml") # 파일 읽은 후 beautifulsoup로 parsing

empty = Label(Window)
empty.pack() # 여백의 미

photo = PhotoImage(file = "Wikipedia-ko.svg.png")
image = Label(Window, image = photo)
image.pack() # 위키피디아 이미지 파일 출력

frame = Frame(Window)
frame.pack(fill = X) # 프레임 묶음

txt = Entry(frame)
txt.pack(padx=10) # 검색어 입력

Button1 = Button(frame, text = "검색", command = finding)
Button1.pack(padx=10, pady=10) # 검색 시작 finding 함수 호출

Window.mainloop() # 윈도우 창 출력
