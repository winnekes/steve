from transitions import Machine

class Robot(object):
    interruptions = 0

    def increment_interruptions(self):
        self.interruptions += 1

    def after_wake_up(self):
        # check time
        # check interruptions during night time
        # randomise mood
        print("i am awake now")

def start_mood_controller(commands_queue, expressions_queue):
    states = ['happy', 'tired', 'angry', 'sad', "confused", "asleep", "awake"]
    transitions = [
            { "trigger": "wake_up", "source": "*", "dest": "awake", "after": "after_wake_up" },
            { "trigger": "go_to_sleep", "source": "*", "dest": "asleep", "after" }
    ]

    robot = Machine(model=Robot(), states=states, queued=True, initial='happy')

    while True:
        if expressions_queue.empty() is False:

    #     print("t")
# while true check every second if time = 9.00 if so wake up
# while true check every second if time = 21.00 if so go to sleep
# keep track of every interruption between that time
