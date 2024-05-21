import random
import time
from lobsters import Lobster


def generate_net_capacity():
    # Seed the random number generator and generate a random net capacity
    random.seed(time.time())
    return random.randint(1, 30)


def generate_no_of_lobsters():
    # Seed the random number generator and generate a random number of lobsters
    random.seed(time.time())
    return random.randint(1, 10)


def generate_lobsters(no_of_lobsters):
    # Generate a list of lobsters with random sizes and values
    lobsters = []
    random.seed(time.time())
    for i in range(no_of_lobsters):
        size = random.randint(1, 20)
        value = random.randint(1, 20)
        lobsters.append(Lobster(i + 1, size, value))
    return lobsters
