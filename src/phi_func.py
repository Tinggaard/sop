# Eulers phi-funktion i Python
import sys
from prime_factor import prime_factors

def phi(n): #Eulers phi-funktion
    #Giver p-1 for alle primfaktorerne
    return produkt([p-1 for p in prime_factors(n)]) #Og ganger dem så sammen


def produkt(liste): #Returnerer produktet af en liste
    n = 1
    for i in liste:
        n *= i
    return n



if __name__ == '__main__':
    try:
        n = int(sys.argv[1])

    except IndexError:
        print('Angiv venlist et positivt heltal')
        print('Brug:')
        print('$ python phi_func.py n')
        sys.exit(1)

    except ValueError:
        print('n skal være et positivt heltal')
        sys.exit(1)


    phi = phi(n)

    print('Antallet af tal som er indbyrdes primiske med {} er:'.format(n))
    print(phi)
