def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def calculate_phi(n):
    if n == 1:
        return 1
    factors = prime_factors(n)
    #Make factors, so that it contians a key as the factor and value as the power of the factor
    factors = {factor: factors.count(factor) for factor in set(factors)}

    phi = 1
    print(f"φ({n}) =" , end=" ")
    for factor in factors:
        print(f"φ({factor}^{factors[factor]})" , end=" * " if factor != list(factors.keys())[-1] else "\n")
    print(f"φ({n}) =" , end=" ")

    for factor in factors:
        print(f"({factor} - 1)x{factor}^{factors[factor] - 1}" , end=" x " if factor != list(factors.keys())[-1] else "\n")
        phi *= (factor - 1) * factor ** (factors[factor] - 1)
    return int(phi)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    factors = prime_factors(number)
    phi = calculate_phi(number)
    print(f"φ({number}: {phi}")
    print(f"Prime factors of {number}: {factors}")
    factors = {factor: factors.count(factor) for factor in set(factors)}
    print(f"Prime factors of {number} with their powers: {factors}")

