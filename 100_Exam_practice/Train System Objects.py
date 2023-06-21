class Ticket:
    def __init__(self, name, destination, price, card):
        self.name = name
        self.destination = destination
        self.price = price
        self.card = card


class Traveller(Ticket):
    def __init__(self, name, destination, price, card, totalMoney):
        super().__init__(name, destination, price, card)
        self.totalMoney = totalMoney


def cardCheckerIssued(cardToCheck, listOfCards):
    if cardToCheck in listOfCards:
        return True


def cardCheckerValidity(cardToCheck, sumOfDigits=0):
    for digit in cardToCheck:
        digit = int(digit)
        sumOfDigits += digit
    if sumOfDigits % 7 == 0:
        return True


listExistingCards = []
listTravellers = []
listNames = []

multipleDestinationsListTravellers= []
totalMoneyTicket = float()

# Creating list of Travellers and their cards

existingCards = int(input())

for index in range(0, existingCards):
    existingCardsInput = input().split()

    currentName = existingCardsInput[0] + " " + existingCardsInput[1]
    currentCardNum = [existingCardsInput[2]]

    currentTraveller = Traveller(currentName, destination="", price="", card=currentCardNum, totalMoney="")

    listExistingCards = [currentTraveller]

    for item in listExistingCards:
        if currentName not in listNames:
            listExistingCards.append(currentTraveller)
        elif item.card != currentCardNum:
            item.card += currentCardNum

    listNames.append(currentName)

dataInput = input()

while dataInput != "time to leave!":

    # Reading Input with Travellers and their tickets

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

    else:
        lastCurrentPrice = currentPrice / 100
        print(f"card {currentCardNum} is not valid!")


    # Create list of Travellers with tickets

    currentTraveller = Traveller(currentName, [currentTicket], totalMoney="")

    listTravellers.append(currentTraveller)

    dataInput = input()

# Sorting Travellers by name to find those with more than one destination

listTravellers.sort(key=lambda x: x.name)

# Merging Travellers with more than one destination

n = len(listTravellers)
for i in range(0, n - 1):

    if listTravellers[i].name != listTravellers[i + 1].name:
        multipleDestinationsListTravellers.append(listTravellers[i])
    else:
        firstTicket = listTravellers[i].ticket
        secondTicket = listTravellers[i + 1].ticket
        newTicket = [firstTicket, secondTicket]
        nameNewTraveller = listTravellers[i].name
        totalMoneyNewTraveller = listTravellers[i].totalMoney

        newTraveller = Traveller(nameNewTraveller, newTicket, totalMoneyNewTraveller)

        multipleDestinationsListTravellers.append(newTraveller)

# Making unique list of Travellers and Tickets

seen = set()
uniqueListTravellers = list()
for each in multipleDestinationsListTravellers:
    if each.name in seen:
        continue
    seen.add(each.name)
    uniqueListTravellers.append(each)

# Getting Total sum of Ticket for each Traveller


# Sorting Travellers by total Money for ticket

uniqueListTravellers.sort(key=lambda x: x.totalMoney, reverse=True)

# Print Output
for item in uniqueListTravellers:
    print(f"{item.name}:")
    for tick in item.ticket:
        print(f"{tick.destination}")