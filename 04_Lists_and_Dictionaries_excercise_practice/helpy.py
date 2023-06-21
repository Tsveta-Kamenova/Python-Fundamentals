import re


class A(object):
    def __init__(self):
        self.myinstatt1 = 'one'
        self.myinstatt2 = 'two'
        self.myinstatt3 = 'two'


a = A()

list = vars(a).items()
print(*list)

#Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
#for item in Dict:
#print("printable string: \n %s" % str(item))


if name not in dict_ref and is_int(values[0]):
    dict_ref[name] = values

elif name in dict_ref:
    dict_ref[name].extend(values)

elif values[0] in dict_ref:
    dict_ref[name] = dict_ref[values[0]]


for item in dict_ref:
    print(f"{item} === ", end="")
    print(", ".join(dict_ref[item]))