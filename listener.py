import speech_recognition as sr
import time

r = sr.Recognizer()

def listen(actively_listening, set_actively_listening, commands_queue):
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)
            print("Listening")
            audio = r.listen(m, phrase_time_limit=5)
            print("Parsing")

            if actively_listening is False:
                command = r.recognize_sphinx(audio, keyword_entries=[("steve", 0)]).strip().lower()

                if command == "steve":
                    commands_queue.put("listening")
                    set_actively_listening(True)

            if actively_listening is True:
                print("Listening with Google now")
                command = r.recognize_google(audio).strip().lower()
                commands_queue.put(command)
                print("I think you said: " + command)

                if command.lower().strip() == "stop listening":
                    commands_queue.put("not listening")
                    set_actively_listening(False)

    except sr.UnknownValueError:
        print("I could not understand you!")

    except sr.RequestError as e:
        print("I don't feel so good, t-t-try again later; {0}".format(e))

def start_listener(commands_queue):
    actively_listening = False

    def set_actively_listening(value):
        nonlocal actively_listening
        actively_listening = value

    while True:
        listen(actively_listening, set_actively_listening, commands_queue)
        time.sleep(.1)
