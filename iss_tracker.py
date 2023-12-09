import requests
import csv
import time

def fetch_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    return data['iss_position']['latitude'], data['iss_position']['longitude']

def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(data)

if __name__ == "__main__":
    csv_filename = "iss_positions.csv"

    while True:
        try:
            latitude, longitude = fetch_iss_position()
            position_data = [latitude, longitude, time.strftime("%Y-%m-%d %H:%M:%S")]
            write_to_csv(csv_filename, position_data)
            print(f"Data written to {csv_filename}: {position_data}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(5)
