# В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек. То есть система будет хранить
# данные о своих клиентах и об их финансовых операциях.
#
# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее:
# Клиент "Иван Петров". Баланс: 50 руб.

class Pet_house:
    pass

class E_wallet:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def get_data_client(self):
        return "Клиент \"" + str(self.name) + '"' + "." + " Баланс: " + str(self.balance) + " руб."

client_1 = E_wallet("Иван Петров", 50)

print(client_1.get_data_client())