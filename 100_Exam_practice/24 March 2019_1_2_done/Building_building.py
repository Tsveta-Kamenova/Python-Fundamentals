investor_capital = {}

budget_needed = float(input())
capital = float(input())
count_investors = int(input())

difference = capital - budget_needed

for i in range(1, count_investors+1):
    investor_capital[i] = float(input())

for item in investor_capital:
    difference += investor_capital[item]
    print(f"Investor {item} gave us {investor_capital[item]:.2f}.")
    if difference >= 0:
        break

extra_money = difference

if difference < 0:
    print(f"Project can not start. We need {abs(difference):.2f} more.")
else:
    print(f"We will manage to build it. Start now! Extra money - {extra_money:.2f}.")

