import time
from modules.spotify import play_song


def start_controller(commands_queue, expressions_queue):
    while True:
        if commands_queue.empty() is False:
            command = commands_queue.get().lower()
            if is_expression(command):
                expressions_queue.put(command)
            if is_music(command):
                title = command[5:]
                source = "playlist" if "playlist" in command else "track"
                print(title)
                success, message = play_song(title, source=source)
                print(success)
                print(message)
                if success:
                    expressions_queue.put("music")
                else:
                    expressions_queue.put("play dead steve")
                print(success)
        time.sleep(.1)


def is_expression(command):
    return True


def is_music(command):
    return command.startswith("play ")
