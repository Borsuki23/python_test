import sys
import time



def main():
    seconds = int(sys.argv[-1])

    for i in range(1, seconds + 1):
        print(f"Пройшло {i} секунд(а).")
        time.sleep(1)

if __name__ == "__main__":
    main()
