import sys
import numpy as np
import rtmidi
import time
from helpers import *
import time

sart_time = time.time()
goal_score = sys.argv[1]
goal_score = int(goal_score)

midiin = rtmidi.MidiIn()
available_ports = midiin.get_ports()
print(available_ports)
midiin.open_port(0)
pressed_keys = []
random_chord = None
score = 0
right = 0
wrong = 0
while score < goal_score:
    if pressed_keys == [] and random_chord == None:
        random_chord = produce_random_chord_data()
        print(f"please enter {str_chord_data(random_chord)}")
    msg = midiin.get_message()
    if msg:
        message, deltatime = msg
        if message[0] == 144:
            if message[2] > 0:
                pressed_keys.append(message[1])
            else:
                pressed_keys.remove(message[1])
            pressed_chord = recognize_chords(pressed_keys)
            if pressed_chord:
                equality = check_chord_data_equality(pressed_chord, random_chord)
                if equality:
                    print("correct!")
                    random_chord = None
                    score += 1
                    right += 1
                else:
                    print("wrong!")
                    print(f"you pressed {str_chord_data(pressed_chord)}")
                    print(f"please enter {str_chord_data(random_chord)}")
                    score -= 1
                    wrong += 1
                print(
                    f"your score is {score}, ({right} right, {wrong} wrong) ratio: {right/(right+wrong):.2f}\n"
                )

    time.sleep(0.01)
end_time = time.time()
print(
    f"you have reached the goal score {goal_score}! in {end_time-sart_time:.2f} seconds"
)
