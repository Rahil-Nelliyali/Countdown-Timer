# Countdown Timer

A simple countdown timer script written in Python. This script allows you to enter the number of minutes to count down and displays a live countdown on the console. When the countdown reaches zero, it plays a sound to notify you that the time is up.

## Prerequisites

- Python 3.x
- Windows operating system (for the sound playback using `winsound` module)

## Usage

1. Clone the repository or download the script file.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:
    
    python countdown_timer.py

4. Enter the number of minutes to count down when prompted. The countdown will start immediately.

5. Wait for the countdown to finish. When the time is up, you will hear a sound.

## Customization

- Sound File: By default, the script is set to play a sound file named "beep-01a.wav". If you want to use a different sound file, replace the "beep-01a.wav" file in the same directory as the script and update the filename in the `winsound.PlaySound` function call.

## Limitations

- This script uses the `winsound` module, which is only available on Windows. If you are using a different operating system, the sound playback functionality will not work.

- The maximum countdown time is limited to 24 hours (1440 minutes). If you enter a value higher than that, you will receive a message indicating that the entered minutes exceed 24 hours.


