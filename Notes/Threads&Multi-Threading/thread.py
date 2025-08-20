import threading, time

def task(name):
    for i in range(5):
            print(f"{name} running {i}")
            time.sleep(5)
       


t1 = threading.Thread(target=task, args=("Thread 1",))
t2 = threading.Thread(target=task, args=("Thread 2",))
t3 = threading.Thread(target=task, args=("Thread 3",))
t1.start(); t2.start(); t3.start()
t1.join(); t2.join(); t3.join()