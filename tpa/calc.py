import math

class Calc:

    def sum(self, *args):
        sum = 0

        for num in args:
            sum += num

        return sum

    def mult(self, *args):
        result = 1

        for num in args:
            result *= num

        return result

    def sub(self, a, b):
        return a-b

    def div(self, a, b):
        return a/b

    def f(self, num):
        if num < 0:
            raise ValueError('Invalid argument: number must be more or eq of zero')

        if num <= 1:
            return 1
        else:
            return num*self.f(num-1)
