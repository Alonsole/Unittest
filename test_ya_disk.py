import unittest
import requests
from unittest import TestCase


class Test_yadisk(TestCase):
    def test_create_folder(self):
        self.headers = {
            'Authorization': 'Ваш Токен'
        }
        ya_message = [['path', 'Image', 201],
                ['path', 'Image', 409],
                ['pat', 'Music', 400]]
        for i, (path, folder_name, expected) in enumerate([
            (ya_message[0][0], ya_message[0][1], ya_message[0][2]),
            (ya_message[1][0], ya_message[1][1], ya_message[1][2]),
            (ya_message[2][0], ya_message[2][1], ya_message[2][2])
        ]):
            with self.subTest(i):
                params = {
                            ya_message[i][0]: ya_message[i][1]
                        }
                response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                                                    params=params,
                                                                    headers=self.headers)

                self.assertEqual(expected, response.status_code)

if __name__ == "__main__":
    unittest.main()