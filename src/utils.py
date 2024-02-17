import os
import time


def get_timestamp(start_time: float = time.perf_counter()) -> tuple[int, int, int]:
    now = max(int(time.perf_counter() - start_time), 0)
    seconds = now % 60
    minutes = (now // 60) % 60
    hours = (now // 3600) % 24
    return (seconds, minutes, hours)


def terminate_program(start_time: float):
    seconds, minutes, hours = get_timestamp(start_time)
    print(f"AFK farm session lasted for {hours}h {minutes}m {seconds}s")
    os._exit(0)