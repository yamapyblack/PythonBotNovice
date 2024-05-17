import time
import lib.utils as utils

time_interval = 600 #10min

def main():
    print("main start")

if __name__ == "__main__":
    while True:
        try:
            main()
            time.sleep(time_interval)
        except Exception as e:
            utils.notify_discord(f"Error: {e}")
            time.sleep(time_interval)
        