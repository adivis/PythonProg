import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')#used to take voices
voices = engine.getProperty('voices')
# print(voices)
email_dict = {'name':'send_to@gmail.com'}#list of all email with key as name
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    Tells the time of day and wishs also    
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:#morning
        speak("Good Morning...")
        speak(hour)
    elif hour>=12 and hour<18:
        speak("Good afternoon... ")
    else:
        speak("good Evening...")
    speak("How may I help you?")


def takeCommand():
    '''
        It takes microphone(audio) input from the user and returns string
    '''
    r = sr.Recognizer()#to recognizer audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said",query)

    except Exception as e:
        print(e)

        print("Please..Say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('send_by@gmail.com', 'password-here')
    server.sendmail('send_by@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    
    wishMe()
    while 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching in wikipedia...")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia....")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            # path="C://Program Files//Google//Chrome//Application//chrome.exe"
            webbrowser.get('chrome').open('https://www.youtube.com')

            
        elif 'open google' in query:

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open('https://www.google.com')

            #Another method if having google downloaded in pc
            # codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            # os.startfile(codepath)

            # webbrowser.open('google.com')
        elif 'time' in query:

            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak("Right now time is..")
            speak(current_time)

        elif 'open geeksforgeeks' in query:
            # webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            # webbrowser.get('chrome').open('https://www.youtube.com')
             webbrowser.open('geeksforgeeks.org')

        elif 'play music' in query:

            music_dir = 'C:\\Users\\adivi\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
        elif 'open code' in query:
            codepath = "C:\\Users\\adivi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to aditi' in query:
            try:
                speak("what should I send?")
                content = takeCommand()
                speak("Tell the name of person to whom you have to send the email")
                name = takeCommand().lower()

                to = email_dict[name]
                print(to)
                sendEmail(to, content)
                speak("Email has been sent..")
            except Exception as e:
                print(e)
                speak("Sorry...I am not able to send email")

        elif 'search on google' in query:
            try:
                speak("What you want to search?")
                search = takeCommand().lower()
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open('https://www.google.com/search?q='+''.join(search))
            except Exception as e:
                print(e)
                speak("Sorry...I am not able to send search")

        elif 'quit' in query or 'exit' in query:
            speak("It was nice talking to you....have a good day")
            exit()
