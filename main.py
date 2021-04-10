import multiprocessing
import threading
from listener import start_listener
from face import start_face
from dotenv import load_dotenv
load_dotenv()
from controller import start_controller


def main():
    expressionsQueue = multiprocessing.Queue()
    commandsQueue = multiprocessing.Queue()

    faceThread = threading.Thread(target=start_face, args=(expressionsQueue,))
    controlThread = threading.Thread(target=start_controller, args=(commandsQueue, expressionsQueue,))
    listenerThread = threading.Thread(target=start_listener, args=(commandsQueue,))

    controlThread.setDaemon(True)
    listenerThread.setDaemon(True)

    faceThread.start()
    controlThread.start()
    listenerThread.start()


if __name__ == "__main__":
    main()
