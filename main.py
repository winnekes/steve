from dotenv import load_dotenv

load_dotenv()

import multiprocessing
import threading

import listener
from face import start_face
from controller import start_controller


def main():
    load_dotenv()
    expressionsQueue = multiprocessing.Queue()
    commandsQueue = multiprocessing.Queue()

    controlThread = threading.Thread(target=start_controller, args=(commandsQueue, expressionsQueue,))
    controlThread.start()

    faceThread = threading.Thread(target=start_face, args=(expressionsQueue,))
    faceThread.start()
    while True:
        listener.listen(commandsQueue)


if __name__ == "__main__":
    main()
