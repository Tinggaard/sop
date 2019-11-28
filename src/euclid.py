#Implementering af Euclids algoritme i Python
import sys

def euclid(a,b):

    orig_a = a
    orig_b = b

    #Hvis b går op i a
    if a % b == 0:
        q = a//b #Kvotient

        print('{a} = {b} * {q} + 0'.format(a=a, b=b, q=q))
        print('({a},{b}) = {res}'.format(a=a, b=b, res=b))
        return b


    while True:
        q = a//b #Kvotient
        r = a-(b*q) #Rest

        #Print inden skift af variabler
        print('{a} = {b} * {q} + {r}'.format(a=a, b=b, q=q, r=r))

        #Største fællesdivisor fundet
        if r == 0:

            print('({a},{b}) = {res}'.format(a=orig_a, b=orig_b, res=b))
            return b

        #Skubber variabler
        a = b
        b = r





if __name__ == '__main__':
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

    except IndexError:
        print('Angiv venlist 2 heltal')
        print('Brug:')
        print('$ python euclid.py a b')
        sys.exit(1)

    except ValueError:
        print('a og b skal begge være heltal')
        sys.exit(1)

    if b > a:
        print('b skal være mindre end a')
        sys.exit(1)

    ### til tests; (324,148) = 4
    # a = 324
    # b = 148


    #Hvis alting virker ok, kør algoritmen
    euclid(a,b)
