# find inverse elementer af a mod n
# fundet her:
# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python#9758173
import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print('Der findes ikke et inverst element for de givne værdier')
        sys.exit(1)
    else:
        return x % m


# finder det inverse element af a mod n
if __name__ == '__main__':
    try:
        a = int(sys.argv[1])
        n = int(sys.argv[2])

    except IndexError:
        print('Angiv venlist 2 heltal')
        print('Brug:')
        print('$ python eulers_sent.py a n')
        sys.exit(1)

    except ValueError:
        print('a og n skal begge være heltal')
        sys.exit(1)


    #Hvis alting virker ok, kør algoritmen
    inv = modinv(a, n)
    print('Det inverse element af {} mod {} er: {}'.format(a, n, inv))
