import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('goood morning sir')
    elif hour >= 12 and hour <= 18:
        speak('good afternoon sir')
    else:
        speak('good evening sir')
    speak("I am Jarvis sir how may i help you!")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of impropervoice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mrcoders88@gmail.com', 'mr.code2000')
    server.sendmail('mrcoders88@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    
    while True:
    # if 1:
        query = takeCommand().lower()

    # for queries
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackover.com")

        elif 'play music' in query:
            music_dir = 'D:\Musics'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H%M%S")
            speak(f'sir, the time is {strtime}')

        elif 'open code' in query:
            codepath = "C:\\Apps\\VSCodeUserSetup-x64-1.68.1.exe"
            os.startfile(codepath)

        elif 'email to darshan' in query:
            try:
                speak('What should I said?')
                content = takeCommand()
                to = "darshanyourEmail@gmail.com"
                # sendEmai(to, content)
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak('sorry sir ,I am not able to send this email.')
        elif 'exit' in query:
            speak("Thank you for using this program!")
            exit()
