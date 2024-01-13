import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Потрібно передати одне ціле число як аргумент командного рядка.")
        return
    try:
        seconds = int(sys.argv[1])
    except ValueError:
        print("Аргумент має бути цілим числом.")
        return

    for i in range(1, seconds + 1):
        print(f"Пройшло {i} секунд(а).")
        time.sleep(1)

if __name__ == "__main__":
    main()
