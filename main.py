import subprocess
import time

import psutil


def start_process(program):
    print(f"starting {program}")
    subprocess.Popen(program, shell=True)


def monitor_process(target_process, replacement_program):
    all_previous_processes = [
        process.info["name"] for process in psutil.process_iter(["pid", "name"])
    ]

    while True:
        all_current_processes = [
            process.info["name"] for process in psutil.process_iter(["pid", "name"])
        ]

        # Check if the target process was running in the previous iteration but not in the current iteration
        if (
            target_process in all_previous_processes
            and target_process not in all_current_processes
        ):
            print("target process WAS running and closed")
            start_process(replacement_program)
        else:
            print("target process wasn't running and closed")

        all_previous_processes = all_current_processes
        time.sleep(1)  # Adjust the sleep duration based on your needs


if __name__ == "__main__":
    target_process_name = input("When this is closed: ")
    replacement_program_path = input("Start this: ")

    monitor_process(target_process_name, replacement_program_path)
