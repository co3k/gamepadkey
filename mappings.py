from sdl2 import *

STICK_MAX = 32760
STICK_THRESHOLD = 16380
STICK_MIN = 128

LEFT_STICK_UP, LEFT_STICK_LEFT, LEFT_STICK_RIGHT, LEFT_STICK_DOWN = [1 << i for i in range(4)]
RIGHT_STICK_UP, RIGHT_STICK_LEFT, RIGHT_STICK_RIGHT, RIGHT_STICK_DOWN = [1 << i for i in range(4, 8)]
BUTTON_A, BUTTON_B, BUTTON_X, BUTTON_Y = [1 << i for i in range(8, 12)]
LEFT_SHOULDER, RIGHT_SHOULDER, LEFT_TRIGGER, RIGHT_TRIGGER = [1 << i for i in range(12, 16)]
BUTTON_OPTIONS, BUTTON_MENU, BUTTON_HOME, BUTTON_LEFT_STICK, BUTTON_RIGHT_STICK = [1 << i for i in range(16, 21)]
DPAD_UP, DPAD_LEFT, DPAD_RIGHT, DPAD_DOWN = [1 << i for i in range(21, 25)]


LEFT_STICK_FLAG_MAPPING = {
    "up": LEFT_STICK_UP,
    "left": LEFT_STICK_LEFT,
    "right": LEFT_STICK_RIGHT,
    "down": LEFT_STICK_DOWN,
}

RIGHT_STICK_FLAG_MAPPING = {
    "up": RIGHT_STICK_UP,
    "left": RIGHT_STICK_LEFT,
    "right": RIGHT_STICK_RIGHT,
    "down": RIGHT_STICK_DOWN,
}

DPAD_FLAG_MAPPING = {
    SDL_HAT_UP: DPAD_UP,
    SDL_HAT_LEFT: DPAD_LEFT,
    SDL_HAT_RIGHT: DPAD_RIGHT,
    SDL_HAT_DOWN: DPAD_DOWN,
}

BUTTON_FLAG_MAPPING = {
    0: BUTTON_A,
    1: BUTTON_B,
    3: BUTTON_X,
    4: BUTTON_Y,
    12: BUTTON_HOME,
    13: BUTTON_LEFT_STICK,
    14: BUTTON_RIGHT_STICK,
}

MODIFIER_FLAG_MAPPING = {
    6: LEFT_SHOULDER,
    7: RIGHT_SHOULDER,
    8: LEFT_TRIGGER,
    9: RIGHT_TRIGGER,
    10: BUTTON_OPTIONS,
    11: BUTTON_MENU,
}

BUTTON_MODIFIER_MAPPING = {
    LEFT_SHOULDER: "tab",
    LEFT_TRIGGER: "command",
    RIGHT_SHOULDER: "esc",
    RIGHT_TRIGGER: "shift",
    BUTTON_MENU: "space",
    BUTTON_OPTIONS: "ctrl",
}

BUTTON_MOUSE_KEY_MAPPING = {
    BUTTON_Y: "left",
    BUTTON_A: "right",
    BUTTON_X: "middle",
    BUTTON_B: "left left",
    BUTTON_LEFT_STICK: "left",
    BUTTON_RIGHT_STICK: "right",

    BUTTON_HOME: "_mode",
}

BUTTON_KEY_MAPPING = {
    LEFT_STICK_UP: "k",
    LEFT_STICK_LEFT: "s",
    LEFT_STICK_RIGHT: "t",
    LEFT_STICK_DOWN: "n",

    BUTTON_RIGHT_STICK: "a",
    RIGHT_STICK_LEFT: "i",
    RIGHT_STICK_UP: "u",
    RIGHT_STICK_RIGHT: "e",
    RIGHT_STICK_DOWN: "o",

    (BUTTON_A + LEFT_STICK_UP): "h",
    (BUTTON_A + LEFT_STICK_LEFT): "m",
    (BUTTON_A + LEFT_STICK_RIGHT): "y",
    (BUTTON_A + LEFT_STICK_DOWN): "r",

    (BUTTON_B + LEFT_STICK_UP): "w",
    (BUTTON_B + LEFT_STICK_LEFT): "g",
    (BUTTON_B + LEFT_STICK_RIGHT): "z",
    (BUTTON_B + LEFT_STICK_DOWN): "d",

    (BUTTON_X + LEFT_STICK_UP): "b",
    (BUTTON_X + LEFT_STICK_LEFT): "p",
    (BUTTON_X + LEFT_STICK_RIGHT): "j",
    (BUTTON_X + LEFT_STICK_DOWN): "c",

    (BUTTON_Y + LEFT_STICK_UP): "v",
    (BUTTON_Y + LEFT_STICK_LEFT): "l",
    (BUTTON_Y + LEFT_STICK_RIGHT): "f",
    (BUTTON_Y + LEFT_STICK_DOWN): "q",

    BUTTON_X: "x",

    (DPAD_UP + RIGHT_STICK_UP): "0",
    (DPAD_UP + RIGHT_STICK_LEFT): "1",
    (DPAD_UP + RIGHT_STICK_RIGHT): "2",
    (DPAD_UP + RIGHT_STICK_DOWN): "3",
    (DPAD_LEFT + RIGHT_STICK_UP): "4",
    (DPAD_LEFT + RIGHT_STICK_LEFT): "5",
    (DPAD_LEFT + RIGHT_STICK_RIGHT): "6",
    (DPAD_LEFT + RIGHT_STICK_DOWN): "7",
    (DPAD_RIGHT + RIGHT_STICK_UP): "8",
    (DPAD_RIGHT + RIGHT_STICK_LEFT): "9",
    (DPAD_RIGHT + RIGHT_STICK_RIGHT): "-",
    (DPAD_RIGHT + RIGHT_STICK_DOWN): "/",
    (DPAD_DOWN + RIGHT_STICK_UP): ".",
    (DPAD_DOWN + RIGHT_STICK_LEFT): ",",
    (DPAD_DOWN + RIGHT_STICK_RIGHT): "@",
    (DPAD_DOWN + RIGHT_STICK_DOWN): "^",

    (DPAD_UP + BUTTON_A): "]",
    (DPAD_UP + BUTTON_B): ":",
    (DPAD_UP + BUTTON_X): "\\",
    (DPAD_UP + BUTTON_Y): "[",
    (DPAD_LEFT + BUTTON_A): ";",
    (DPAD_LEFT + BUTTON_B): "_",
    (DPAD_LEFT + BUTTON_X): "",
    (DPAD_LEFT + BUTTON_Y): "",

    BUTTON_A: "enter",
    BUTTON_B: "backspace",
    BUTTON_Y: "",

    DPAD_UP: "up",
    DPAD_LEFT: "left",
    DPAD_RIGHT: "right",
    DPAD_DOWN: "down",

    BUTTON_LEFT_STICK: "_hanzen",
    BUTTON_HOME: "_mode",
}
