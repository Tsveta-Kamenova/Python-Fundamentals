class Gladiator:
    def __init__(self, name, skill, totalSkillPoints):
        self.name = name
        self.skill = skill
        self.totalSkillPoints = totalSkillPoints


listGladiators = []
currentSkill = {}

dataInput = input()

while dataInput != "Ave Cesar":
    splitDataInput = dataInput.split(" -> ")

    currentName = splitDataInput[0]
    current_technique = splitDataInput[1]
    currentSkillPoints = int(splitDataInput[2])

    currentSkill[current_technique] = currentSkillPoints

    currentGladiator = Gladiator(name=currentName, skill=currentSkill, totalSkillPoints=currentSkillPoints)

    if len(listGladiators) == 0:
        listGladiators.append(currentGladiator)

    if currentGladiator.name not in [x.name for x in listGladiators]:
        listGladiators.append(currentGladiator)
    else:
        newSkill = currentGladiator.skill
        newPoints = currentGladiator.totalSkillPoints

    dataInput = input()

for item in listGladiators:
    print(f"{item.name}: {item.skill} skill")