import os
import random
import sys
import time

def spawn_child():
    status = os.fork()
    if status == 0:
        child_pid = os.getpid()
        pid = os.getppid()
        print(f"Parent{pid}: I ran children process with PID {child_pid}.")
        os.execl(sys.executable, sys.executable, "child.py", str(random.randint(5, 10)))
    elif status > 0:
        pid, status = os.wait()
        print(f"Parent{os.getpid()}: Child with PID {pid} terminated. Exit Status {status}.")
        if status != 0:
           spawn_child()
        return

if __name__ == "__main__":
    num_children = int(sys.argv[1])
    pid = os.getpid()
    for _ in range(num_children):
        spawn_child()
    print("All child processes terminated.")
  
