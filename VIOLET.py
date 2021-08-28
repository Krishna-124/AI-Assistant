from selenium import webdriver
from getpass import getpass
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import random

#c_driver = 'Dir of chromedriver.exe'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def intro():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning Sir!")
    elif 12 <= hour < 17:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am Violet! How can I help You")


def say_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 0.6
        r.energy_threshold = 2000
        audio = r.listen(source)

    try:
        print("Recognize.....")
        query = r.recognize_google(audio)
        print(f"User said :{query}\n")

    except Exception as e:
        print(e)
        print("say again sir")
        return "none"
    return query


def time():
    hh = datetime.datetime.now().hour
    ampm = "am"
    if hh > 12:
        hh = hh - 12
        ampm = "pm"
    mm = datetime.datetime.now().minute
    c_time = "time is", hh, mm, ampm
    speak(c_time)


def date():
    m = datetime.date.today()
    speak(m)


while True:
    query = input("say:").lower()

    # print(query)
    # query = say_user().lower()
    query = query.replace("hi violet", "").replace('hey violet', '')
    if 'hello violet' in query or 'initiate ai' in query:
        intro()
    elif 'who created you' in query or 'who are you' in query or 'tell me about yourself' in query:
        speak("I am Violet! your artificial intelligent  , I am created by Krishna Singh Dummagaa")
    elif 'bye violet' in query or 'shutdown' in query or 'ok bye' in query:
        hour = int(datetime.datetime.now().hour)
        if hour >= 20:
            speak('good night sir! sweet dream ')
        else:
            speak('ok bye sir ! have a good day')
        exit()
    elif 'what is time' in query or ('tell' and 'time') in query:
        time()
    elif 'what is date' in query or ('tell' and 'date') in query:
        date()
    elif 'open' and 'youtube' in query:
        speak('what can i search you for sir')
        query = say_user().lower()
        driver = webdriver.Chrome(c_driver)
        driver.get('https://www.youtube.com/')
        youtube_box = driver.find_element_by_id('search')
        youtube_box.send_keys(query)
        login_btn = driver.find_element_by_id('search-icon-legacy')
        login_btn.submit()

    elif 'open google' in query:
        webbrowser.open("google.com")

        '''speak('what can i search for you sir ')
        driver=webdriver.Chrome(c_driver)
        search_box=driver.find_element_by_id('fakebox-input')
        driver.get(query)
        submit_btn=driver.find_element_by_id('')'''

    elif 'play music' in query or 'play song' in query:
        speak("which one ! sir")
        while True:
            #music_dir = "Type dir where your songs are stored stored"
            songs = os.listdir(music_dir)
            #if you want type query = say_user().lower()
            query = input("which...")
            query = query.lower()
            if 'as you like' in query or 'as you want' in query or 'as you want' in query:
                list_len = len(songs) - 2
                r = random.randrange(0, list_len, 1)
                os.startfile(os.path.join(music_dir, songs[r]))
                break
            elif query == 'exit':
                break
            elif 'play' in query:
                query = query.replace("play", "")
                query = query.replace(query[0], "")
                count = 0
                length = len(songs)

                for i in range(0, length, 1):
                    if query in songs[i].lower():
                        os.startfile(os.path.join(music_dir, songs[i]))
                        count = count + 1
                        break
                if count == 0:
                    speak("sorry sir! would you like to play another song")


    elif 'wikipedia' in query:
        lines_wiki = 2
        while True:
            if 'elaborate' not in query and 'ok ' not in query and 'wikipedia' in query:
                try:
                    speak("Searching Wikipedia.....")
                    query = query.replace("wikipedia", "").replace(' in ', ' ')
                    query = query.replace("search", "")
                    result = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia ")
                    print(result)
                    speak(result)
                except Exception as e:
                    print(e)
                    query = say_user()
            elif 'elaborate' in query or 'more info' in query:
                lines_wiki = lines_wiki + 2
                result = wikipedia.summary(query, sentences=lines_wiki)
                speak("According to Wikipedia ")
                print(result)
                speak(result)
            elif 'ok ' in query or 'quit' in query or 'exit' in query:
                break

    elif 'login wi-fi' in query:

        speak('can i know your username and passcode')
        query = say_user().lower()
        # query = input("username...")
        username = input("Enter User name:")
            passcode = getpass('Enter password:')

        driver = webdriver.Chrome(c_driver)
        driver.get('http://172.16.16.16:8090/')
        username_box = driver.find_element_by_name('username')
        username_box.send_keys(username)
        passcode_box = driver.find_element_by_name('password')
        passcode_box.send_keys(passcode)
        login_btn = driver.find_element_by_id('logincaption')
        login_btn.submit()
    elif 'show' in query and 'net' in query and 'speed' in query:
        driver = webdriver.Chrome(c_driver)
        driver.get('https://fast.com/')

    elif 'remind' in query:
        if 'set' in query and 'remind' in query:
            f = open('remind.txt', 'a')
            speak('ok. tell me')
            msg = input('say r') + "\n"
            f.write(msg)
            f.close()
        elif 'remind' in query and 'me' in query:
            count = 0
            f = open('remind.txt', 'r')
            msg = f.readlines()
            for i in msg:
                count = count + 1
            if count == 0:
                speak('you dont set yet')
            else:
                count = 0
                for i in msg:
                    speak(count + 1)
                    speak(msg[count])
                    count = count + 1
                f.close()
        elif 'delete' in query and 'remind' in query:
            f = open('remind.txt', 'a')
            f.close()
            '''speak('Which one say serial no')
            msg = input('say r')
            for a range(1,15,1):
            '''

        else:
            continue


    '''elif 'motivation' in query and 'want' in query:
        speak("you should !")
        moti_dir = 'Type video dir'
        vid = os.listdir(moti_dir)
        lenn = len(vid)
        ran = random.randrange(0, lenn, 1)
        os.startfile(os.path.join(moti_dir, vid[ran]))'''

    '''elif 'rename' in query and 'file' in query:
        i = 1
        path = "Type Dir ,ex="C:\\Users\\abc\\Desktop\\Books\\"""
        for filename in os.listdir(path):
            my_dest = str(i) + ".png"
            my_source = path + filename
            my_dest = path + my_dest
            os.rename(my_source, my_dest)
            i += 1'''