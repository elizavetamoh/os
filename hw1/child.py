import random
import sys
import time

if __name__ == "__main__":
    pid = os.getpid()
    ppid = os.getppid()
    random_number = int(sys.argv[1])
    print(f"Child{pid}: I am started. My PID {pid}. Parent PID {ppid}.")
    time.sleep(random_number)
    exit_status = random.randint(0, 1)
    print(f"Child{pid}: I am ended. PID {pid}. Parent PID {ppid}.")
    sys.exit(random.randint(0,1))



