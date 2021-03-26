import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speech recon
import wikipedia
import smtplib
import webbrowser as wb
import psutil


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("the current time is")
    speak(Time)

def date_():
    year =datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back ganesh!")
   
    

    #Greetings

    hour = datetime.datetime.now().hour

    if hour >=0 and hour<12:
        speak("good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour>=18 and hour<24:
        speak("good evening sir!")
    else:
        speak("Good night sir!")
    speak("jarvis at your service. please tell me how can i help you today?")

def TakeCommand_():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1
        audio =r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()

    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery =psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)
    speak('percentage')

if __name__=="__main__":
    wishme()

    while True:
        query = TakeCommand_().lower()
        #all cmds will stored in lower case query for easy recon
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace('wikipedia',' ')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=TakeCommand_()
                speak("who is the reciever")
                reciever=input("enter reciever's Email:")
                reciever='reciever_is_me@gmail.com'
                to=reciever
                sendEmail(to,content)
                speak(content)
                speak('email has been sent')

            except Exception as e:
                print(e)
                speak("Unable to send Email.")

        elif'search in web' in query:
            speak('What should i search?')
            chromepath = 'C:\Program Files\Mozilla Firefox/firefox.exe %s'

            search = TakeCommand_().lower()
            wb.open('https://www.google.com/search?client=firefox-b-d&q='+search)
        elif 'exit' in query:
            speak('adios amigo')
            exit()
        elif 'cpu' in query:
            cpu()