import speech_recognition as sr
import pyttsx4  #text to speech version 4
import pywhatkit  #Library for whatsapp and youtube automation.
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #a listener that will be able to identify your voice.
engine = pyttsx4.init() #Intitialize the text to speech engine.
voices = engine.getProperty('voices') #Give engine a female voice, from all the voices provided by the tts.
engine.setProperty('voice', voices[1].id) #Set the voice to all the voices we get, as the 2nd one, i.e index 1, & its id.

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:    #Create a try block in case the microphone fails to work.
        with sr.Microphone() as source:  #This is the source of our audio.
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '') #Removes alexa from the string. i.e You don't have to call alexa.
                print(command)  
    except:
        pass  #Py doesn't do anything when the exception happens.
    return command

def run_alexa():
    command = take_command() #Takes a command from the user, i.e calls the function above.
    print(command)
    if 'play' in command:
        song = command.replace('play', '') #To remove play from the command.
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'what is the date' in command:
        date = datetime.datetime.now().strftime('%d-%m-%Y')
        print(date)
        talk('The date is ' + date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1) #Prints back 1 line.
        print(info)
        talk(info)
    elif 'what is' in command:
        something = command.replace('what is', '')
        info = wikipedia.summary(something, 1) #Prints back 1 line.
        print(info)
        talk(info)
    elif 'go for a date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with Wi-Fi.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please rephrase that.')

while True: 
    run_alexa()

