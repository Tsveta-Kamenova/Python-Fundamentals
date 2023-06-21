class ObjectClass():

    def __init__(self):
        self.newAttribute = None
        self.attribute1 = "attribute1"

    def newAttr(self, attr):
        setattr(self, attr, attr)


objectClass = ObjectClass()

print(objectClass.attribute1)
setattr(objectClass, "newAttribute", "new attr")
print(objectClass.newAttribute)