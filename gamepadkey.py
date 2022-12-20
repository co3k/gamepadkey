import ctypes
import time
from sdl2 import *
import pyautogui

from mappings import *

class StickStatus:
    def __init__(self):
        self.direction = { "up": 0, "left": 0, "right": 0, "down": 0 }

    def set_direction(self, value, keys):
        self.direction[keys[0]] = 0
        self.direction[keys[1]] = 0

        if value < STICK_MIN:
            self.direction[keys[0]] = value * -1
        elif STICK_MIN < value:
            self.direction[keys[1]] = value

    def vertical(self, value):
        self.set_direction(value, ["up", "down"])

    def horizontal(self, value):
        self.set_direction(value, ["left", "right"])

    def reset(self):
        self.direction = self.direction.fromkeys(self.direction, 0)

    def current_direction(self):
        max_key, max_value = max(self.direction.items(), key=lambda x: x[1])

        if max_value < STICK_THRESHOLD:
            return ""

        return max_key

def match_flags(mapping, flags):
    return [k for k in mapping.keys() if k == flags]

class Gamepad:
    def __init__(self):
        self.previous = 0
        self.current = 0
        self.num = 0

        self.hold = set()

        self.left_stick_status = StickStatus()
        self.right_stick_status = StickStatus()

        self.mode = ["mouse", "keyboard"]
        self.current_mode = "mouse"

        self.event_count = 0

        SDL_Init(SDL_INIT_JOYSTICK)

    def handle_special(self, command):
        if command == "_mode":
            self.current_mode = self.mode[(self.mode.index(self.current_mode) + 1) % (len(self.mode))]
            print("Changed current mode to " + self.current_mode)
        if command == "_hanzen":
            pyautogui.hotkey('ctrl', 'space')

    def update_current_stick_status(self, mapping, status):
        self.current = (self.current & ~sum(mapping.values())) | mapping.get(status, 0)

    def update(self):
        self.event_count = 0
        self.previous = self.current
        event = SDL_Event()

        while SDL_PollEvent(ctypes.byref(event)) != 0:
            self.event_count += 1

            if event.type == SDL_JOYDEVICEADDED:
                self.device = SDL_JoystickOpen(event.jdevice.which)
                print(self.device)
            elif event.type == SDL_JOYHATMOTION:
                self.update_current_stick_status(DPAD_FLAG_MAPPING, event.jhat.value)
            elif event.type == SDL_JOYAXISMOTION:
                if event.jaxis.axis == 0:
                    self.left_stick_status.horizontal(event.jaxis.value)
                elif event.jaxis.axis == 1:
                    self.left_stick_status.vertical(event.jaxis.value)
                elif event.jaxis.axis == 2:
                    self.right_stick_status.horizontal(event.jaxis.value)
                elif event.jaxis.axis == 3:
                    self.right_stick_status.vertical(event.jaxis.value)
            elif event.type == SDL_JOYBUTTONDOWN:
                self.current |= BUTTON_FLAG_MAPPING.get(event.jbutton.button, 0)
                modifier_flag = MODIFIER_FLAG_MAPPING.get(event.jbutton.button, 0)
                if modifier_flag != 0:
                    modifier = BUTTON_MODIFIER_MAPPING[modifier_flag]
                    pyautogui.keyDown(modifier)
            elif event.type == SDL_JOYBUTTONUP:
                self.current -= self.current & BUTTON_FLAG_MAPPING.get(event.jbutton.button, 0)
                modifier_flag = MODIFIER_FLAG_MAPPING.get(event.jbutton.button, 0)
                if modifier_flag != 0:
                    modifier = BUTTON_MODIFIER_MAPPING[modifier_flag]
                    pyautogui.keyUp(modifier)

            self.update_current_stick_status(LEFT_STICK_FLAG_MAPPING, self.left_stick_status.current_direction())
            self.update_current_stick_status(RIGHT_STICK_FLAG_MAPPING, self.right_stick_status.current_direction())

        if self.previous == self.current:
            self.num += 1
        else:
            self.num = 0

        if self.previous != 0:
            if self.num > 10:
                for flag in match_flags(BUTTON_KEY_MAPPING, self.current):
                    if self.current_mode == "keyboard":
                        target = BUTTON_KEY_MAPPING.get(flag, "")
                        if not target.startswith("_"):
                            pyautogui.keyDown(target)
                            self.hold.add(target)
                    if self.current_mode == "mouse":
                        target = BUTTON_MOUSE_KEY_MAPPING.get(flag)
                        if target is not None:
                            pyautogui.mouseDown(button=target)
                            self.hold.add(target)
            elif self.previous != self.current:
                for flag in match_flags(BUTTON_KEY_MAPPING, self.previous):
                    if not (self.current & flag):
                        key_target = BUTTON_KEY_MAPPING.get(flag, "")
                        mouse_target = BUTTON_MOUSE_KEY_MAPPING.get(flag)
                        mouse_num = 1

                        if mouse_target == "left left":
                            mouse_target = "left"
                            mouse_num = 2

                        if self.current_mode == "keyboard":
                            if key_target.startswith("_"):
                                self.handle_special(key_target)
                            elif key_target in self.hold:
                                pyautogui.keyUp(key_target)
                                self.hold.remove(key_target)
                            else:
                                pyautogui.press(key_target)
                        elif self.current_mode == "mouse" and mouse_target is not None:
                            if mouse_target.startswith("_"):
                                self.handle_special(mouse_target)
                            elif mouse_target in self.hold:
                                pyautogui.mouseUp(button=mouse_target)
                                self.hold.remove(mouse_target)
                            else:
                                pyautogui.click(button=mouse_target, clicks=mouse_num, interval=0.2)

        if self.current_mode == "mouse":
            w, h = pyautogui.size()
            x = ((self.left_stick_status.direction["right"] - self.left_stick_status.direction["left"]) / STICK_MAX) * 10 ** 2
            y = ((self.left_stick_status.direction["down"] - self.left_stick_status.direction["up"]) / STICK_MAX) * 10 ** 2
            pyautogui.move(x, y)

def main():
    gamepad = Gamepad()

    while True:
        gamepad.update()
        time.sleep(0.005 if gamepad.current_mode == "mouse" else 0.04 * (gamepad.event_count + 1))

if __name__ == "__main__":
    main()
