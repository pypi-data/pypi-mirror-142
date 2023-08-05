class Calculator:
    def __init__(self):
        super().__init__()
        
    def add(self, *args):
        total = 0
        for val in args:
            total += int(val)
        return total

    def subtract(self, *args):
        total = 0
        for val in args:
            total -= val
        return total

    def multiply(self, *args):
        total = 1
        for val in args:
            total *= val
        return total

    def divide(self, *args):
        total = 1
        for val in args:
            total /= val
        return total
