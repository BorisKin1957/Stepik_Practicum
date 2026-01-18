'''

Реализуйте класс Person, который принимает имя, фамилию и возраст человека при
создании экземпляра. У объекта этого класса должны быть:

    Свойство full_name, которое возвращает полное имя в формате: <имя> <фамилия>.

    Свойство age, которое возвращает возраст.

Вводить и выводить ничего не нужно, ваша задача только реализовать класс.

Sample Input:

Sample Output:

OK

'''

class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def age(self):
        return self._age

# Не изменяйте написанный ниже код
def run_tests():
    try:
        matz = Person('Yukihiro', 'Matsumoto', 47)
        assert matz.full_name == 'Yukihiro Matsumoto'
        assert matz.age == 47

        joe = Person('Joe', 'Smith', 30)
        assert joe.full_name == 'Joe Smith'
        assert joe.age == 30

        print("OK")

    except AssertionError:
        print("Failed")

run_tests()