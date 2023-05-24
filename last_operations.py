"""
<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>

"""
import json
import os
from zipfile import ZipFile
from operation import Operation

SOURCE_NAME = "operations.zip"
NUMBER_OF_OPERATIONS = 5


def get_operation_from_file(number):
    """
    :param number - number or operations to return

    prints list operations with the format
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """

    list_of_operations = []
    with ZipFile(SOURCE_NAME, "r") as zip_file:
        for i in zip_file.namelist():
            temp_file = zip_file.extract(i)
            with open(temp_file, encoding="utf8", mode="r") as operation_file:
                list_of_operations = [item for item in json.load(operation_file) if
                                      len(item) > 1 and item["state"] == "EXECUTED"]
                list_of_operations.sort(key=lambda item: item["date"], reverse=True)
            if os.path.isfile(temp_file):
                os.remove(temp_file)

    return [Operation(item) for item in list_of_operations[:number]]


operations_executed = [print(item) for item in get_operation_from_file(NUMBER_OF_OPERATIONS)]
