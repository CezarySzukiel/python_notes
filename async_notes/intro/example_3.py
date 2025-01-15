import multiprocessing
import os


def hello():
    print(f"Hello from process {os.getpid()}")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=hello)
    p1.start()
    print(f"Hello from process {os.getpid()}")

    p1.join()