'''

Roak paper scissors
'''
import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')#used for taking in-build voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said {query}\n')

    except Exception as e:
        # print(e)
        print('Say that again please....')
        return 'None'
    return query


if __name__ == '__main__':

    choice = ['rock','paper','scissor']
    speak("Enter how many times do you want to play with computer")
    n = int(input())
    while n!=0:
        computer = random.choice(choice)
        speak("Speak your choice")
        query = takeCommand().lower()
        if 'rock' in query:
            if computer=='paper':
                speak(f"Computer have won this match with computer's choice being {computer}")


            elif computer=='scissor':
                speak(f"You have won this match with computer's choice being {computer}")
            else:
                speak(f"This match is tied with computer's choice being {computer}")
        elif 'paper' in query:
            if computer == 'scissor':
                speak(f"Computer have won this match with computer's choice being {computer}")

            elif computer == 'rock':
                speak(f"You have won this match with computer's choice being {computer}")
            else:
                speak(f"This match is tied with computer's choice being {computer}")
        elif 'scissor' in query:
            if computer == 'rock':
                speak(f"Computer have won this match with computer's choice being {computer}")
            elif computer == 'paper':
                speak(f"You have won this match with computer's choice being {computer}")
            else:
                speak(f"This match is tied with computer's choice being {computer}")
        else:
            speak(f"You have enter wrong choice so computer have won this match with choice {computer}")

        n = n - 1
        if n!=0:
            speak("Next round.....")


