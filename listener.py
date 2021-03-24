import speech_recognition as sr

r = sr.Recognizer()


def listen(queue):
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m)

            print("Listening")
            audio = r.listen(m, phrase_time_limit=5)
            print("Parsing")
            command = r.recognize_google(audio)
            queue.put(command)
            print("Google Speech Recognition thinks you said: " + command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
