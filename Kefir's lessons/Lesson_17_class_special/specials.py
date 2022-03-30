




def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

# print(lcm(9,12))

class ZeroDenominatorError(Exception):
    def __init__(self):
        super(ZeroDenominatorError, self).__init__('на ноль делить низя')


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ZeroDenominatorError()

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_denominator = lcm(self.denominator, other.denominator)
            new_numerator = int(self.numerator * (new_denominator / self.denominator)\
                            + other.numerator * (new_denominator / other.denominator))
        elif isinstance(other, int):
            new_denominator = self.denominator
            new_numerator = int(self.numerator + other.numerator * self.denominator)
        elif isinstance(other, float):
            raise TypeError(other)
        else:
            raise Exception('Not int or Fraction value.')

        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        return self + other

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __float__(self):
        return self.numerator / self.denominator


frac1 = Fraction(2,9)
frac2 = Fraction(5,12)

frac1 += frac2

# print(str(frac1))
# print(str(frac2))
# print(str(frac1 + frac2))
# print(float(frac1 + frac2))

try:
    print(frac2 + '1.0')
except TypeError as e1:
    print('че ты мне флот суешь')
except Exception as e:
    print('че ты мне строку суешь')        # лучше избегаит и старатьсь обрабатывать на месте возникновения



print(str(frac1))
print(str(frac2))
print(str(frac1 + frac2))


# try:
#     print(frac2 + 1.0)
#     print(str(frac1))
#     print(str(frac2))
#     print(str(frac1 + frac2))
# except Exception as e:
#     print('нет такова')        # можно сразу весь код, но лучше локализовано ловить ошибку