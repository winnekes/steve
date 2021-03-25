import time
from modules.spotify import play_song


def start_controller(commandsQueue, expressionsQueue):
    while True:
        time.sleep(1)
        if commandsQueue.empty() is False:
            command = commandsQueue.get().lower()
            if isExpression(command):
                expressionsQueue.put(command)
            if isMusic(command):
                title = command[5:]
                print(title)
                success, message = play_song(title, source="track")
                if success:
                    expressionsQueue.put("music")
                else:
                    expressionsQueue.put("unknown")
                print(success)



def isExpression(command):
    return True

def isMusic(command):
    return command.startswith("play ")