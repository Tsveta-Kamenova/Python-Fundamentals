number = int(input())


def sign_number(n):
    if n > 0:
        print(f"The number {n} is positive.")
    elif n == 0:
        print(f"The number {n} is zero.")
    else:
        print(f"The number {n} is negative.")


sign_number(number)
