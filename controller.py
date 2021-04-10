import time
from modules.spotify import play_song


def start_controller(commandsQueue, expressionsQueue):
    while True:
        if commandsQueue.empty() is False:
            command = commandsQueue.get().lower()
            if is_expression(command):
                expressionsQueue.put(command)
            if is_music(command):
                title = command[5:]
                source = "playlist" if "playlist" in command else "track"
                print(title)
                success, message = play_song(title, source=source)
                print(success)
                print(message)
                if success:
                    expressionsQueue.put("music")
                else:
                    expressionsQueue.put("play dead steve")
                print(success)
        time.sleep(.1)

def is_expression(command):
    return True


def is_music(command):
    return command.startswith("play ")