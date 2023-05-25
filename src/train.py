# train.py

from tqdm import tqdm
import time


def run():
    for i in tqdm(range(10)):
        time.sleep(1.0)

    print("Training is done!")


if __name__ == "__main__":
    print("Start training model")
    run()
    input()
