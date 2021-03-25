import multiprocessing
import threading
import listener
import time
from face import start_face
from dotenv import load_dotenv
load_dotenv()
from controller import start_controller


def main():
    expressionsQueue = multiprocessing.Queue()
    commandsQueue = multiprocessing.Queue()

    faceThread = threading.Thread(target=start_face, args=(expressionsQueue,))
    controlThread = threading.Thread(target=start_controller, args=(commandsQueue, expressionsQueue,))

    faceThread.start()
    controlThread.start()

    while True:
        time.sleep(1)
        listener.listen(commandsQueue)


if __name__ == "__main__":
    main()
