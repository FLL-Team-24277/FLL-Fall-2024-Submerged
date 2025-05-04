import os
import subprocess

import time


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        seconds -= 1


robot_name = os.getenv("robotName")

if robot_name:
    print(f"\033[92mYour robot name is {robot_name}\033[0m")
else:
    print(
        "\033[91mYour robotName environment variable has not been set\033[0m"
    )

print("git pull in five seconds")
countdown(5)
subprocess.run(["git", "pull"])
