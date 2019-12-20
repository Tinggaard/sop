# Implementering af primtalsfaktorisering i Python
import sys

#Fundet på stackoverflow:
#https://stackoverflow.com/questions/15347174/python-finding-prime-factors#22808285

#Nedenstående algoritme virker på baggrund af primtalenes definition.
#Når et tal som går op i n findes, ved vi at det er et primtal,
#ellers ville nogle mindre tal også gå op.
def prime_factors(n):
    i = 2
    factors = []

    while i * i <= n: #Mens i er mindre end sqrt(n)

        if n % i: #Hvis i ikke går op i n
            i+=1 #Øg i med 1

        else: #Hvis i går op i n
            n //= i #Del n med i
            factors.append(i) #tilføj i som faktor

    if n > 1:
        factors.append(n) #Tilføj det sidste tal som

    return factors




if __name__ == '__main__':
    try:
        n = int(sys.argv[1])

    except IndexError:
        print('Angiv venlist et positivt heltal')
        print('Brug:')
        print('$ python prime_factor.py n')
        sys.exit(1)

    except ValueError:
        print('n skal være et positivt heltal')
        sys.exit(1)


    primes = prime_factors(n)

    print('Primtalsfaktorerne i {} er:'.format(n))
    print(primes)
