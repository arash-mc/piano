import numpy as np

chord_diffs_inversions = {
    "M": [[4, 3], [3, 5], [5, 4]],
    "m": [[3, 4], [4, 5], [5, 3]],
    "dim": [[3, 3], [3, 6], [6, 3]],
    "aug": [[4, 4], [4, 4], [4, 4]],
    "7": [[4, 3, 3], [3, 3, 2], [3, 2, 4], [2, 4, 3]],
    "m7": [[3, 4, 3], [4, 3, 2], [3, 2, 3], [2, 3, 4]],
    "M7": [[4, 3, 4], [3, 4, 1], [4, 1, 4], [1, 4, 3]],
}

three_note_chords = ["M", "m", "dim", "aug"]
four_note_chords = ["7", "m7", "M7"]
inversion = ["", "1st", "2nd", "3rd"]
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def recognize_chords(pressed_keys, note_number=3):
    if len(pressed_keys) < note_number:
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
            return (notes[root_note % 12], key, which_inversion, len(pressed_keys))


def str_chord_data(chord_data):
    return f"{chord_data[0]}{chord_data[1]}{inversion[chord_data[2]]}"


def produce_random_chord_data():
    root = np.random.choice(notes)
    chord_type = np.random.choice(list(chord_diffs_inversions.keys()))
    chord_length = len(chord_diffs_inversions[chord_type])
    which_inversion = np.random.choice(range(chord_length))
    if chord_type == "aug":
        which_inversion = 0
    note_number = 3 if chord_type in three_note_chords else 4
    return (root, chord_type, which_inversion, note_number)


def check_chord_data_equality(pressed_chord_data, random_chord_data):
    return pressed_chord_data == random_chord_data
