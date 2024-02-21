import time
import constants
import keyboard
from macros import Macros
import decorators
from utils import get_timestamp, terminate_program, check_granblue_relink
from utils import format_int, is_on_screen


def main():
    # main constants
    QUEST_DONE = (constants.QUEST_COMPLETE_SCREEN, constants.REPLAY_QUEST)
    check_granblue_relink()
    time_start = time.perf_counter()
    keyboard.on_press_key(
        key="escape", callback=lambda _: terminate_program(time_start)
    )
    runs = 0

    def log(msg: str):
        seconds, minutes, hours = get_timestamp(time_start)
        f_seconds = format_int(seconds)
        f_minutes = format_int(minutes)
        f_hours = format_int(hours)
        timestamp = f"{f_hours}:{f_minutes}:{f_seconds}"
        print(f"[{timestamp}]\t{msg}")

    while True:

        @decorators.loop_run_once
        def on_run_complete():
            """
            Does stuff when a run has been completed
            """
            nonlocal runs
            runs += 1
            log(f"Runs Completed: {runs}")

        # When the user successfully completes the quest
        while is_on_screen(*QUEST_DONE):
            on_run_complete()

            # Select replay option first
            if runs == 1:
                if not is_on_screen(constants.REPEAT_QUEST_FIRST_PROMPT):
                    Macros.xbox_a()
                else:
                    Macros.repeat_quest()
            else:
                if is_on_screen(constants.CONTINUE_PLAYING_QUEST):
                    Macros.continue_playing()
                else:
                    Macros.xbox_a()

            time.sleep(0.1)

        # When the user is requires a revive
        while is_on_screen(constants.HP_ZERO):
            Macros.xbox_a()


if __name__ == "__main__":
    main()
