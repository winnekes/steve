import speech_recognition as sr

r = sr.Recognizer()


def listen(commandsQueue):
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)
            print("Listening")
            audio = r.listen(m, phrase_time_limit=5)
            print("Parsing")
            command = r.recognize_google(audio)
            commandsQueue.put(command)
            print("I think you said: " + command)

    except sr.UnknownValueError:
        print("I could not understand you!")

    except sr.RequestError as e:
        print("I don't feel so good, t-t-try again later; {0}".format(e))
