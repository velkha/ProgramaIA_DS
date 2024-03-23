from Car import Car
import threading
from multiprocessing import Process
import time
# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Using the methods of the Car class
my_car.accelerate(20)


def print_numbers():
    for i in range(10):
        print(f"Cosa {i}")
        time.sleep(.3)

def print_letters():
    for i in range(10):
        print(f"Yupi {i}")
        time.sleep(.4)
        
# Create two threads
#thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# Start the threads
# thread1.start()
# thread2.start()

# Wait for both threads to finish
# thread1.join()
# thread2.join()
if __name__ == '__main__':
    process1 = Process(target=print_numbers)
    process2 = Process(target=print_letters)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

# method to generate a