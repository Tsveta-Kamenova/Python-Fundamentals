import math

budget = float(input())
clients_needed = int(input())
gb_data = int(input())
hosts = int(input())
uptime = float(input())

servers_needed = math.ceil(clients_needed/50)
storages_needed = math.ceil(gb_data/0.5)
hourly_cost = (2*servers_needed + 0.5*storages_needed)*24
hosts_cost = 10*hosts
monthly_cost = 30*hourly_cost
total_cost = (monthly_cost+hosts_cost)*uptime/100


if total_cost < budget:
    leftover = round((budget-total_cost), 2)
    print(f"Clouds Ahoy! Monthly cost: ${total_cost:.2f} (${leftover}0 leftover)")
else:
    need = round((total_cost - budget),2)
    print(f"Stay Grounded! Monthly cost: ${total_cost:.2f} (Need ${need}0 more)")
