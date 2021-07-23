import speech_recognition as sr
import time

r = sr.Recognizer()

# only listen via google if steve is called

def listen(commands_queue):
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)
            print("Listening")
            audio = r.listen(m, phrase_time_limit=5)
            print("Parsing")
            command = r.recognize_google(audio)
            commands_queue.put(command)
            print("I think you said: " + command)

    except sr.UnknownValueError:
        print("I could not understand you!")

    except sr.RequestError as e:
        print("I don't feel so good, t-t-try again later; {0}".format(e))

def start_listener(commands_queue):
    while True:
        listen(commands_queue)
        time.sleep(.1)
