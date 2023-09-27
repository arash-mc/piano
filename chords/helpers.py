import numpy as np

chord_diffs_inversions = {
    "M": [[4, 3], [3, 5], [5, 4]],
    "m": [[3, 4], [4, 5], [5, 3]],
    "dim": [[3, 3], [3, 6], [6, 3]],
    "aug": [[4, 4], [4, 4], [4, 4]],
}
inversion = ["", "1st", "2nd"]
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def recognize_chords(pressed_keys):
    if len(pressed_keys) < 3:
        return
    pressed_keys.sort()
    chord_diffs = [
        pressed_keys[i + 1] - pressed_keys[i] for i in range(len(pressed_keys) - 1)
    ]
    for key, value in chord_diffs_inversions.items():
        if chord_diffs in value:
            which_inversion = value.index(chord_diffs)
            root_note = pressed_keys[0 - which_inversion]
            chord_data = (notes[root_note % 12], key, which_inversion)
            print(str_chord_data(chord_data))
            return (notes[root_note % 12], key, which_inversion)


def str_chord_data(chord_data):
    return f"{chord_data[0]}{chord_data[1]}{inversion[chord_data[2]]}"


def produce_random_chord_data():
    root = np.random.choice(notes)
    chord_type = np.random.choice(list(chord_diffs_inversions.keys()))
    which_inversion = np.random.choice(range(3))
    if chord_type == "aug":
        which_inversion = 0
    return (root, chord_type, which_inversion)


def check_chord_data_equality(pressed_chord_data, random_chord_data):
    return pressed_chord_data == random_chord_data
