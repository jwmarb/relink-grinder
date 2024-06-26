import time
from typing import Callable
import pyautogui
import win32gui
import constants
import vgamepad


class Macros:
    _relink_hwnd: int | None = None
    _gamepad = vgamepad.VX360Gamepad()

    @staticmethod
    def _find_window(name: str):
        return win32gui.FindWindow(None, name)

    @staticmethod
    def _get_relink_hwnd():
        """
        Gets the relink hwnd
        """
        if Macros._relink_hwnd is None:
            Macros._relink_hwnd = Macros._find_window(constants.HWND_NAME)
            if Macros._relink_hwnd == 0:
                raise Exception('"Granblue Fantasy: Relink" not detected')
        return Macros._relink_hwnd

    @staticmethod
    def macro(fn: Callable[[], None]):
        """
        Executes a macro based on virtual gamepad
        """

        def wrapper():
            # Focuses application window, if applicable
            if win32gui.GetForegroundWindow() != Macros._get_relink_hwnd():
                pyautogui.press("alt")
                win32gui.SetForegroundWindow(Macros._get_relink_hwnd())

            fn()

        return wrapper

    @staticmethod
    def delay():
        """
        Forces the thread to sleep so that there is a delay
        """
        time.sleep(constants.INPUT_DELAY)

    @staticmethod
    @macro
    def continue_playing():
        """
        Whenever a popup prompts the user to continue playing the quest, it
        will automatically select yes
        """
        Macros.xbox_dpad_up()
        Macros.xbox_a()

    @staticmethod
    @macro
    def xbox_a():
        """
        Simulates the pressing of the A button on xbox in the application
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def xbox_b():
        """
        Simulates the pressing of the B button on xbox in the application
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
        Macros._gamepad.update()
        Macros.delay()

    def xbox_x():
        """
        Simulates the pressing of the X button on xbox in the application
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def xbox_dpad_up():
        """
        Simulates the pressing of dpad up on xbox in the application
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
        )
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    def release_buttons():
        """
        Releases all buttons
        """
        Macros._gamepad.reset()
        Macros._gamepad.update()
        time.sleep(0.01)

    @staticmethod
    @macro
    def xbox_dpad_left():
        """
        Simulates the pressing of dpad left on xbox in the application
        """
        Macros._gamepad.press_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
        )
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
        )
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def xbox_dpad_down():
        """
        Simulates the pressing of dpad down on xbox in the application
        """
        Macros._gamepad.press_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
        )
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
        )
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def xbox_back():
        """
        Simulates the pressing of the back button on xbox in the application
        """
        Macros._gamepad.press_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        Macros._gamepad.update()
        Macros.delay()

    @staticmethod
    @macro
    def repeat_quest():
        """
        Turns on Repeat Quest during the battle results screen
        """
        Macros.xbox_x()
        Macros.xbox_a()

    @staticmethod
    @macro
    def use_sba():
        Macros._gamepad.press_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
        )
        Macros._gamepad.press_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
        )
        Macros._gamepad.update()
        Macros.delay()
        Macros._gamepad.release_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
        )
        Macros._gamepad.release_button(
            vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
        )
        Macros._gamepad.update()
        Macros.delay()
