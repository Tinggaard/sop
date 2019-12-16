# TODO
* Billede af pgp fra hashcat
* Antal bits (MD5 128 bit)
* faktoere ved login:
    * kodeord
    * Kryptering
    * hashing
    * 2fa

**Læs nu lige igennem, for sammenhæng**

## stikord
* rainbowtables
* brute force
* hashtable
* gpg
* http vs https
* certifikater
* 2fa
* kvantecomputere


## links

pow til pytohn: https://docs.python.org/3/library/functions.html#pow

primtal: https://primes.utm.edu/lists/small/millions/

hashcat pgp https://hashcat.net/hashcat/

unilogin: https://viden.stil.dk/pages/viewpage.action?pageId=70582342


# tegn
```
$ pdftotext main.pdf -enc UTF-8 - | wc -m
```
Eller
```
$ detex file.tex | wc -C
```


# opbygning

0. Intro
    1. [x] Kryptografi / kryptologi
    2. [ ] Hvad er RSA og hvad bygger det på?

1. Talteori
    1. [x] Kort intro til mod og primtal (måske for lang)
    2. [x] Noget om største fælles divisor og indbyrdes primisk
    3. [x] Dernæst eulers funktion
    4. [ ] Så til de sætninger som er vigtige...

2. Hashing
    1. [x] Hvad er hashing - pseudorandom - envejs
    2. [ ] Evt. forskellige hashfunktioner
    3. [ ] Noget om hashtabeller og kodeord?

3. Forskel
    1. [x] Først et eksempel på en protokol med kryptografi
    2. [x] Derefter et eksempel på hashing og kodeord
    3. [x] Brute-force
    4. [x] Så hvordan man bruger begge dele i hverdagen, til verificering
    5. [ ] Til sidst en vurdering - hvis ikke først til sidst.

4. RSA
    1. [ ] Hvor bruger man det?
    2. [x] Eksempel på RSA
    3. [ ] UNI login som eks re: `[a-z]{3}[0-9]{2}[a-z]{3}`
    4. [ ] Hvordan verden ville være uden RSA
    5. [x] Husk: http vs https

5. Konklusion
