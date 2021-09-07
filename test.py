import multitasking
import time


multitasking.set_max_threads(2)
@multitasking.task
def tryToSleep(name):
    print(f"спит: {name}")
    time.sleep(2)


while True:
    tryToSleep("Первый")
    tryToSleep("Второй")

