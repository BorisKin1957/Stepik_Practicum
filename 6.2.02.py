'''

Реализуйте класс Fraction, который принимает два аргумента — числитель и знаменатель.

Ваша задача:

    Сделать дробь представимой в виде строки — при использовании str() или
    print() экземпляра класса, он должен выводиться в виде строки "a/b" (например, "2/3").

    Обеспечить возможность сложения дробей с помощью оператора +.

    Результат сложения должен быть приведён к несократимой (минимальной) форме.

     Нельзя использовать fractions.Fraction из стандартной библиотеки Python.

Sample Input:

Sample Output:

OK
'''
class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        # Находим общий знаменатель и складываем числители
        new_top = self.top * other.bottom + other.top * self.bottom
        new_bottom = self.bottom * other.bottom

        # Сокращаем дробь
        gcd_val = self._gcd(new_top, new_bottom)
        new_top //= gcd_val
        new_bottom //= gcd_val

        return Fraction(new_top, new_bottom)

    def _gcd(self, a, b):
        # Находим наибольший общий делитель (алгоритм Евклида)
        while b != 0:
            a, b = b, a % b
        return a


# Не изменяйте написанный ниже код
def run_tests():
    try:
        assert Fraction(1, 8) + Fraction(4, 5) == Fraction(37, 40)
        assert Fraction(911, 920) + Fraction(980, 906) == Fraction(863483, 416760)
        assert Fraction(610, 941) + Fraction(253, 985) == Fraction(838923, 926885)
        assert Fraction(956, 798) + Fraction(662, 189) == Fraction(16880, 3591)
        assert Fraction(694, 485) + Fraction(853, 861) == Fraction(1011239, 417585)
        assert Fraction(982, 111) + Fraction(219, 561) == Fraction(191737, 20757)
        assert Fraction(344, 873) + Fraction(658, 486) == Fraction(41201, 23571)
        assert Fraction(662, 361) + Fraction(322, 382) == Fraction(184563, 68951)
        assert Fraction(740, 813) + Fraction(184, 348) == Fraction(33926, 23577)
        assert Fraction(579, 441) + Fraction(543, 807) == Fraction(78524, 39543)
        assert Fraction(212, 979) + Fraction(46, 580) == Fraction(83997, 283910)
        print("OK")

    except AssertionError:
        print("Failed")

run_tests()