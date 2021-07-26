from dotenv import load_dotenv

load_dotenv()
import multiprocessing
import threading
from listener import start_listener
from face import start_face
from modules.mood import start_mood_controller
from controller import start_controller

def main():
    expressions_queue = multiprocessing.Queue()
    commands_queue = multiprocessing.Queue()
    moods_queue = multiprocessing.Queue()

    face_thread = threading.Thread(target=start_face, args=(expressions_queue,))
    listener_thread = threading.Thread(target=start_listener, args=(commands_queue,))
    mood_thread = threading.Thread(target=start_mood_controller, args=(moods_queue,))
    control_thread = threading.Thread(target=start_controller, args=(commands_queue, expressions_queue, moods_queue,))

    control_thread.setDaemon(True)
    listener_thread.setDaemon(True)

    control_thread.start()
    face_thread.start()
    listener_thread.start()
    mood_thread.start()

if __name__ == "__main__":
    main()
