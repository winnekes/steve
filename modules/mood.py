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

    pass

def start_mood_controller(moods_queue):
    robot = Robot()
    states = ['happy', 'tired', 'angry', 'sad', "confused", "asleep", "awake"]
    transitions = [
            { "trigger": "wake_up", "source": "*", "dest": "awake", "after": "after_wake_up" },
            { "trigger": "go_to_sleep", "source": "*", "dest": "asleep", }
    ]

    machine = Machine(model=robot, states=states, queued=True, initial='happy')
    print(robot.state)
#         print("t")
# while true check every second if time = 9.00 if so wake up
# while true check every second if time = 21.00 if so go to sleep
# keep track of every interruption between that time
