import random
import time
from lobsters import Lobster


def generate_net_capacity():
    random.seed(time.time())
    return random.randint(1, 30)


def generate_no_of_lobsters():
    random.seed(time.time())
    return random.randint(1, 10)


def generate_lobsters(no_of_lobsters):
    lobsters = []
    random.seed(time.time())
    for i in range(no_of_lobsters):
        size = random.randint(1, 20)
        value = random.randint(1, 20)
        lobsters.append(Lobster(i + 1, size, value))
    return lobsters
