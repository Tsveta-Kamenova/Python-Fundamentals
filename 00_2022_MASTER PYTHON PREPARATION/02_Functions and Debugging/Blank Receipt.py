def header():
    print("CASH RECEIPT", end="\n")
    print("------------------------------", end="\n")


def body():
    print("Charged to____________________", end="\n")
    print("Received by___________________", end="\n")


def footer():
    print("------------------------------", end="\n")
    print("© SoftUni", end="\n")


def print_blank_receipt():
    header()
    body()
    footer()


print_blank_receipt()
