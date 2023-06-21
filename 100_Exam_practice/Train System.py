class Traveller:
    def __init__(self, name, ticket, totalMoney):
        self.ticket = ticket
        self.name = name
        self.totalMoney = totalMoney


class Ticket:
    def __init__(self, destination, price, cardNum):
        self.destination = destination
        self.prince = price
        self.cardNum = cardNum


def cardCheckerIssued(cardToCheck, listOfCards):
    if cardToCheck in listOfCards:
        return True


def cardCheckerValidity(cardToCheck, sumOfDigits=0):
    for digit in cardToCheck:
        digit = int(digit)
        sumOfDigits += digit
    if sumOfDigits % 7 == 0:
        return True


finalListTravellers = []
listExistingCards = []
listTravellers = []

totalMoneyTicket = float()

# Create list of existing Cards

existingCards = int(input())

for index in range(0, existingCards):
    existingCardsInput = input().split()

    currentName = existingCardsInput[0] + " " + existingCardsInput[1]
    currentCardNum = existingCardsInput[2]

    currentTraveller = Traveller(currentName, currentCardNum, totalMoney="")

    listExistingCards.append(currentTraveller)


dataInput = input()

while dataInput != "time to leave!":

    # Reading Input

    travellersInput = dataInput.split()

    currentName = travellersInput[1] + " " + travellersInput[2]
    currentDestination = travellersInput[3]
    currentCardNum = travellersInput[4]

    # Determine Price of Ticket

    currentPrice = 0

    for item in currentDestination:
        currentPrice += ord(item)
    lastCurrentPrice = 0

    # Determine Card validity

    if cardCheckerValidity(currentCardNum):
        print(f"issuing card {currentCardNum}")
        lastCurrentPrice = currentPrice / 200

    if not cardCheckerValidity(currentCardNum):
        lastCurrentPrice = currentPrice / 100
        print(f"card {currentCardNum} is not valid!")

    currentTicket = Ticket(currentDestination, lastCurrentPrice, currentCardNum)

    # Create list of Travellers with tickets

    currentTraveller = Traveller(currentName, currentTicket, totalMoney="")

    listTravellers.append(currentTraveller)

    dataInput = input()

# Sorting Travellers by name to find those with more than one destination

listTravellers.sort(key=lambda x: x.name)

# Merging Travellers with more than one destination

n = len(listTravellers)

for i in range(0, n - 1):
    if listTravellers[i].name == listTravellers[i + 1].name:
        listTravellers[i].ticket.update(listTravellers[i + 1].ticket)

# Create list with Travellers with unique names

seen = set()
last = list()
for each in listTravellers:
    if each.name in seen:
        continue
    seen.add(each.name)
    last.append(each)

# Getting Total sum of Ticket for each Traveller

for each in last:
    for tick in each.ticket.items():
        i = 1
        totalMoneyTicket += tick[i]
    each.totalMoney = totalMoneyTicket
    totalMoneyTicket = 0

# Sorting Travellers by total Money for ticket

last.sort(key=lambda x: x.totalMoney, reverse=True)

# Print Output

for item in last:
    print(f"{item.name}:")
    for k, v in item.ticket.items():
        print(f"--{k}: {v:.2f}lv")
    print(f"total: {item.totalMoney:.2f}lv")
