
from dataclasses import dataclass

@dataclass
class Triangle():
    n_dots = 3
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_p(self):
        self.p = 1/2 * (a + b + c)


tr_1 = Triangle(1, 2, 2.5)
tr_2 = Triangle(6, 8, 1)