import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <duration_in_seconds>")
        sys.exit(1)

    duration = int(sys.argv[1])

    for i in range(duration):
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)
