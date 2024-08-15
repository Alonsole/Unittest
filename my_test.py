import unittest

from unittest import TestCase

from script1 import check_triangle
from script2 import check_auth
from script3 import get_cost

class Test_check_triangle(TestCase):
    def test_triangle_ok(self):
        triangle = ['Треугольник не существует',
                    'Равносторонний треугольник',
                    'Равнобедренный треугольник',
                    'Треугольник не существует']
        for i, (side1, side2, side3, expected) in enumerate([
            (1, 2, 3,  triangle[0]),
            (3, 3, 3, triangle[1]),
            (3, 3, 4, triangle[2]),
            (1, 2, 3, triangle[3])
        ]):
            with self.subTest(i):
                result = check_triangle(side1, side2, side3)
                self.assertEqual(expected, result)

    @unittest.expectedFailure
    def test_error(self):
        self.assertEqual(check_triangle(3, 4, 5), "Ошибка")

class Test_check_auth(TestCase):
    def test_check_auth(self):
        auth_message = ['Добро пожаловать',
                    'Доступ ограничен',
                    'Ошибка специальная']
        for i, (login, password, expected) in enumerate([
            ('admin','password', auth_message[0]),
            (' ', ' ',  auth_message[1]),
            ('123', ' ', auth_message[2])
        ]):
            with self.subTest(i):
                result = check_auth(login, password)
                self.assertEqual(expected, result)

    @unittest.expectedFailure
    def test_auth_fail(self):
        self.assertEqual(check_auth('admin','pasord'), "Добро пожаловать")


class Test_get_cost(TestCase):
    def test_summarize_with_params(self):
        price = ['Стоимость доставки: 200 руб.', 'Стоимость доставки: 500 руб.']
        for i, (weight, expected) in enumerate([
            (5, price[0]),
            (10, price[0]),
            (11, price[1]),
            (12, price[1])
        ]):
            with self.subTest(i):
                result = get_cost(weight)
                self.assertEqual(expected, result)

    @unittest.expectedFailure
    def test_get_cost_fail(self):
        self.assertEqual(get_cost('10'), "Стоимость доставки: 200 руб.")

if __name__ == "__main__":
    unittest.main()