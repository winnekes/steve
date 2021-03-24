import threading
import listener
import multiprocessing
from face import start_face


def main():
    expressionsQueue = multiprocessing.Queue()
    t1 = threading.Thread(target=start_face,args=(expressionsQueue,))
    t1.start()
    while True:
       listener.listen(expressionsQueue)


if __name__ == "__main__":
    main()
