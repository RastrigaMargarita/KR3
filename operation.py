from datetime import datetime


class Operation:
    """Contains an operation data
    :param `id` — id транзакциии
    :param  `date` — информация о дате совершения операции
    :param  `operationAmount` — сумма операции и валюта
        :param  `amount` — сумма перевода
        :param  `currency` — валюта перевода
    :param  `description` — описание типа перевода
    :param  `from` — откуда (может отсутстовать)
    :param  `to` — куда
    """

    def __init__(self, dict_to_parse):
        self.op_id = dict_to_parse["id"]
        self.date = datetime.fromisoformat(dict_to_parse["date"]).date().strftime("%d.%m.%Y")
        self.operation_amount = dict_to_parse["operationAmount"]
        self.description = dict_to_parse["description"]
        if "from" in dict_to_parse.keys():
            self.tr_from = dict_to_parse["from"]
        else:
            self.tr_from = ""
        self.tr_to = dict_to_parse["to"]

    def __repr__(self):
        from_splitted = self.tr_from.split(" ")
        if len(from_splitted) == 2:
            from_formatted = f"{from_splitted[0]} {from_splitted[1][:4]} " \
                             f"{from_splitted[1][4:6]}** **** {from_splitted[1][-4:]}"
        else:
            from_formatted = "-"
        to_splitted = self.tr_to.split(" ")
        if len(to_splitted) == 2:
            to_formatted = f"{to_splitted[0]} **{to_splitted[1][-4:]}"
        else:
            to_formatted = f"{to_splitted[0]}"
        return f"""
{self.date} {self.description}
{from_formatted} > {to_formatted}
{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}"""
