import random

class TestClass:
    def print_random_number(self):
        print(f"Random {random.randint(1, 10)}")

# Create an instance of the class
test = TestClass()

# Call the method to print a random number
test.print_random_number()