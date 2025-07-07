class Calc:
    def __init__(self, x, y, operation="+"):
        self.x = x
        self.y = y
        self.op = operation

    def added(self):
        return self.x + self.y

    def reduce(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def division(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            print("[LOG: WARNING] Деление на ноль")
