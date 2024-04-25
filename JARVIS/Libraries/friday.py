import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
print(voices[1].id)  # Check the name of the person by index value
engine.setProperty('voice',voices[1].id)

email = {
    'suraj sahu' : 'sahusuraj1776@gmail.com',
    'niraj sahu' : 'nirajsahu189@gmail.com',
    'gautam sahu' : 'gautamsahu112@gmail.com',
    'prerna pal' : 'prernapal03@gmail.com',
    'varun sampath':'varun.sampat0504@gmail.com'
}

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sahusuraj1776@gmail.com','wvjhfssmwkpnwajw')
    server.sendmail('sahusuraj1776@gmail.com',to,content)
    server.close()

    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour > 12 and hour<= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Friday Sir, Please tell me how may I can help you.")
    
def takeCommand():
    # It takes microphone input from user and returns string as output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = 'en-in')
        
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def main():
    wishMe()
    count = 0
    while (count != 4):
        query = takeCommand().lower()
    
    #Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia...')
            print(results)
            speak(results)
            count = 0
                  
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            count = 0
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            count = 0
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            count = 0
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Sahu Suraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            count = 0
            
        elif 'search' in query:
            query = query.replace('search','')
            webbrowser.open('https://www.google.com/search?q='+query)
            count = 0
            
        elif 'play music on youtube' in query:
            webbrowser.open("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
            count = 0
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\Sahu Suraj\\Music\\Favourite songs"
            songs = os.listdir(music_dir)
            index = random.randint(0,20)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[index]))
            count = 0
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            count = 0
        
        elif 'a mail' in query:
            try:
                speak("To whom you want to send mail?")
                to = takeCommand().lower()
                speak("What shold i say?")
                content = takeCommand()
                recever = email[to]
                sendEmail(recever,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I'm unable to send email!")
            count = 0
        
        elif 'random password' in query:
            speak("What is the length of password you required?")
            x = takeCommand()
            passlen = int(x)
            s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*!"
            p="".join(random.sample(s,passlen))
            print(p)
            count = 0
            
        elif 'alarm' in query:
            speak("Enter the Time !")
            time = input(": Enter the Time:")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                
                if now == time:
                    speak("Time to wake up Sir!!")
                    playsound("C:\\Users\\Sahu Suraj\\Music\\Favourite songs\\Senorita.mp3")
                    break
            count = 0
                
        elif 'quit' in query:
            break
        
        else:
            count = count + 1