import unittest
from operation import Operation


class LastOperationsTests(unittest.TestCase):

    def test_operation(self):
        self.assertEqual(Operation({
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }).__repr__(), """
26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 > Счет **9589
31957.58 руб.""")
