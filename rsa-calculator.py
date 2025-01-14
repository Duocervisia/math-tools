import math

def normal_gcd(a, b):
    while b != 0:
        a, b = b, a % b
        if(b != 0):
            print(str(a) + " = " + str(math.floor(a/b)) + " * " + str(b) + " + " + str(round((a/b - math.floor(a/b))*b)))

    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    print(f"{gcd} = {x} * {a} + {y} * {b}")
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m

def fast_exp(base, exp, mod, rev = False):
    result = 1
    first_base = base
    base = base % mod
    binary_exp = bin(exp)[2:]  # Binärdarstellung des Exponenten
    if(not rev):    
        print(f"Binärdarstellung von e = {exp} = {binary_exp}")
    else:
        print(f"Binärdarstellung von d = {exp} = {binary_exp}")
    all_steps = []
    used_steps = []
    while exp > 0:
        all_steps.append(base)
        if (exp % 2) == 1:
            result = (result * base) % mod
            used_steps.append(base)
        exp = exp >> 1
        base = (base * base) % mod
    
    # Ausgabe aller Zwischenschritte
    for i, step in enumerate(all_steps):
        print(f"{first_base} exp {2**i} ≡ {step} (mod {mod})")
    
    # Ausgabe der verwendeten Zwischenschritte
    if(not rev):
        print(f"⇒ c = {' ∙ '.join(map(str, used_steps))} ≡ {result} (mod {mod})")
    else:
        print(f"⇒ w' = {' ∙ '.join(map(str, used_steps))} ≡ {result} (mod {mod})")
    return result

def calculate_phi(m):
    phi = 0
    for i in range(1, m):
        if math.gcd(i, m) == 1:
            phi += 1
    return phi

def main():
    m = int(input("Gib m: "))
    e = int(input("Gib e: "))
    w = int(input("Gib w: "))
    
    print(f"\n")

    phi_m = calculate_phi(m)

    print("Gegeben:")
    print(f"m = {m}")
    print(f"e = {e}")
    print(f"w = {w}")

    print(f"\n")
    print(f"Lösung:")

    print(f"φ(m) = φ({m}) = {phi_m}")

    print(f"\n")

    print(f"EA:")

    gcd_val = normal_gcd(e, phi_m)
    print(f"\n")
    
    # Using Extended Euclidean Algorithm
    print(f"EA rückwärts:")
    gcd, x, y = extended_gcd(e, phi_m)
    d = x % phi_m
    print(f"\n")

    print(f"⇒ 1 = e * d ≡ {e} * {x} (mod {phi_m})")
    print(f"⇒ d ≡ {x} ≡ {d} (mod {phi_m})")
    print(f"\n")

    print(f"Verschlüsselungm des Wortes w = {w}:")
    c = fast_exp(w, e, m)
    print(f"\n")

    print(f"Entschlüsselung des Chiffrats c = {c}:")
    w_prime = fast_exp(c, d, m, True)
    print(f"\n")

if __name__ == "__main__":
    main()