n = int(input())


def number_sign(num):
    if num == 0:
        print(f"The number {num} is zero.")
    elif num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")


number_sign(n)