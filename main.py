from Calculator import Calc
import random
def func(a, b):
    """Dockstring"""
    for _ in range(10):
        a = random.randint(0, 5)
        b = random.randint(0, 3)
        c = Calc(a, b)
        print(c.division(check=True))



if __name__ == "__main__":
    print(func(1, 2))