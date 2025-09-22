from math import sqrt

def est_premier(n):
    """Teste si n est premier."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def fermat(n):
    """Retourne le n-ième nombre de Fermat : 2^(2^n) + 1."""
    return 2 ** (2 ** n) + 1


def first_non_prime_fermat():
    """Retourne le premier nombre de Fermat non premier."""
    k = 0
    while True:
        F = fermat(k)
        if not est_premier(F):
            return F
        k += 1


def next_prime(n):
    """Retourne le premier nombre premier strictement supérieur à n."""
    m = n + 1
    while not est_premier(m):
        m += 1
    return m


def couple_prime_after(n):
    """Retourne le premier nombre du premier couple de premiers jumeaux après n."""
    m = n + 1
    while True:
        if est_premier(m) and est_premier(m + 2):
            return m
        m += 1


def germain_prime_after(n):
    """Retourne le premier nombre premier de Sophie Germain après n."""
    m = n + 1
    while True:
        if est_premier(m) and est_premier(2 * m + 1):
            return m
        m += 1


def main():
    # Nombres de Fermat
    for i in range(5):
        print(f"F_{i} = {fermat(i)}")

    # Premier nombre de Fermat non premier
    fnp = first_non_prime_fermat()
    print(f"Premier nombre de Fermat non premier : {fnp}")

    # Premier nombre premier après 100000
    p = next_prime(100000)
    print(f"Premier nombre premier après 100000 : {p}")

    # Premier couple de nombres premiers jumeaux après 100000
    twin = couple_prime_after(100000)
    print(f"Premier couple de nombres premiers jumeaux après 100000 : ({twin}, {twin+2})")

    # Premier nombre premier de Sophie Germain après 100000
    g = germain_prime_after(100000)
    print(f"Premier nombre premier de Sophie Germain après 100000 : {g}")


if __name__ == "__main__":
    main()