import multiprocessing
import threading
from listener import start_listener
from face import start_face
from dotenv import load_dotenv
from controller import start_controller

load_dotenv()


def main():
    expressions_queue = multiprocessing.Queue()
    commands_queue = multiprocessing.Queue()

    face_thread = threading.Thread(target=start_face, args=(expressions_queue,))
    control_thread = threading.Thread(target=start_controller, args=(commands_queue, expressions_queue,))
    listener_thread = threading.Thread(target=start_listener, args=(commands_queue,))

    control_thread.setDaemon(True)
    listener_thread.setDaemon(True)

    face_thread.start()
    control_thread.start()
    listener_thread.start()


if __name__ == "__main__":
    main()
