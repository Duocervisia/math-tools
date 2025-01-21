import math

def normal_gcd(a, b):
    while b != 0:
        a, b = b, a % b
        if(b != 0):
            print(str(a) + " = " + str(math.floor(a/b)) + " * " + str(b) + " + " + str(round((a/b - math.floor(a/b))*b)))
    print(f"\n")
    print("ggT: " + str(a))
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    print(f"{gcd} = {x} * {a} + {y} * {b}")
    return gcd, x, y

def onlyEA():
    a = int(input("Gib a: "))
    b = int(input("Gib b: "))
    
    print(f"\n")

    print("Gegeben:")
    print(f"a = {a}")
    print(f"b = {b}")

    print(f"\n")
    print(f"Lösung:")

    print(f"\n")

    print(f"EA:")

    gcd_val = normal_gcd(a, b)
    print(f"\n")
    
    # Using Extended Euclidean Algorithm
    print(f"EA rückwärts:")
    gcd, x, y = extended_gcd(a, b)
    print(f"\n")

if __name__ == "__main__":
    onlyEA()
