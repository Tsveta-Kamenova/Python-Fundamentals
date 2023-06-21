import math


class BankAccount:
    def __init__(self, bank, name, balance):
        self.bank = bank
        self.name = name
        self.balance = balance


data = input()
list_accounts = []


while data != "end":
    split_data = data.split(" | ")
    bank = split_data[0]
    name = split_data[1]
    balance = float(split_data[2])
    balance = balance*100
    balance = round(balance, 0)
    balance = balance/100
    current_account = BankAccount(bank, name, balance)
    list_accounts.append(current_account)

    data = input()

list_accounts = sorted(list_accounts, key=lambda x: (-x.balance, len(x.bank)))

for obj in list_accounts:
    print(f" {obj.name} -> {obj.balance:.2f} ({obj.bank})")



