import os
import threading

def hello():
    print(f"Hello from {threading.current_thread()}")

print(f" Python process running with.id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

t1 = threading.Thread(target=hello)  # tworze nowy obekt klasy Thread
t1.start()  #uruchamiam wątek

print(f"Total threads: {total_threads}")
print(f"Current thread name: {thread_name}")

t1.join()  # kończę watek