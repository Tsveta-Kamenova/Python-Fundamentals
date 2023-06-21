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

list_accounts.sort(key=lambda x: x.name)
list_accounts.sort(key=lambda x: x.balance, reverse=True)


for i in range(0, len(list_accounts)):
    for j in range(i+1, len(list_accounts)):
        if (list_accounts[i].balance == list_accounts[j].balance) and len(list_accounts[i].bank) >= len(list_accounts[j].bank):
            list_accounts[i], list_accounts[j] = list_accounts[j], list_accounts[i]
        else:
            pass

for obj in list_accounts:
    print(f" {obj.name} -> {obj.balance:.2f} ({obj.bank})")



