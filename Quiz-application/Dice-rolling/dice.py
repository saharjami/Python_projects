
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    )
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def parse_input(input_string):
    if input_string in range(1, 5):
        return input_string
    else:
        print("Please choose a number from 1 to 4: ")
        raise SystemExit(1)


def roll_dice(dice_num):
    roll_num = []
    for i in range(dice_num):
        roll = random.randint(1, 6)
        roll_num.append(roll)
    return roll_num


def generate_dice_faces(dice_values):
    dice_faces = []
    for i in dice_values:
        dice_faces.append(DICE_ART[i])
    return dice_faces


def generate_results(dice_faces):
    dice_faces_rows = []
    for i in range(DIE_HEIGHT):
        row_components = []
        for j in dice_faces:
            row_components.append(j[i])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    result = "\n".join(dice_faces_rows)
    return result


dice_num_input = int(input("How many dice do you want to roll [1-4]? "))
dice_num = parse_input(dice_num_input)
roll_list = roll_dice(dice_num)
roll_faces = generate_dice_faces(roll_list)
roll_result = generate_results(roll_faces)
print(roll_result)
