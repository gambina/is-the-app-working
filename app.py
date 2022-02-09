import time
import random


def run():
    while True:
        if random.random() < 0.01:
            print('Warning: Data integrity has been comprimised')
        else:
            print('The "app" is up-to-date')
        time.sleep(5)


if __name__ == "__main__":
    run()
