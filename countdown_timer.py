import time
import sys
import winsound

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        sys.stdout.flush()
        time.sleep(1)
        t -= 1

    print("Time's up!")
    # Play a ding sound
    winsound.PlaySound("beep-01a.wav", winsound.SND_FILENAME)

if __name__ == "__main__":
    minutes = input("Enter the number of minutes: ")
    
    if not minutes.isdigit():
        print("Invalid input! Please enter a positive integer.")
    else:
        minutes = int(minutes)
        if minutes > 1440:
            print("Entered minutes is above 24 hours.")
        else:
            countdown(minutes * 60)
