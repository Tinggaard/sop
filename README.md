# TODO
* Billede af pgp fra hashcat
* Antal bits (MD5 128 bit)
* faktoere ved login:
    * kodeord
    * Kryptering
    * hashing
    * 2fa
* kode til kryptering i Python
* hashlib ved MD5
* protokol env
* Hvad er en protokol?
* Flyt evt. hashcat til sektion 2

**Læs nu lige igennem, for sammenhæng**

## stikord
- [x] rainbowtables
- [x] brute force
- [x] hashtable
- [x] gpg
- [x] http vs https
- [ ] certifikater
- [ ] 2fa
- [ ] kvantecomputere
- [x] DES-key


## links

pow til Python: https://docs.python.org/3/library/functions.html#pow

primtal: https://primes.utm.edu/lists/small/millions/

hashcat pgp https://hashcat.net/hashcat/

uni login: https://viden.stil.dk/pages/viewpage.action?pageId=70582342

re: https://docs.python.org/3.8/library/re.html#regular-expression-syntax


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
    - [x] Kryptografi / kryptologi
    - [ ] Hvad er RSA og hvad bygger det på?

1. Talteori
    - [x] Kort intro til mod og primtal (måske for lang)
    - [x] Noget om største fælles divisor og indbyrdes primisk
    - [x] Dernæst eulers funktion
    - [ ] Så til de sætninger som er vigtige...

2. Hashing
    - [x] Hvad er hashing - pseudorandom - envejs
    - [ ] Evt. forskellige hashfunktioner
    - [x] Noget om hashtabeller?

3. Forskel
    - [ ] Hvad er en protokol?
    - [x] Hvad er kryptografi?
    - [x] En protokol for kryptografi
    - [x] Hvordan man faktisk bruger RSA
    - [x] Derefter et eksempel på hashing og kodeord, herunder rainbowtables, salt og hashcat
    - [x] Brute-force (hvor er det defineret?)
    - [x] Så hvordan man bruger begge dele i hverdagen, til verificering, gpg
    - [ ] Til sidst en vurdering - hvis ikke først til sidst.

4. RSA
    - [ ] Hvor bruger man det?
    - [x] Matematikken bag RSA, samt beviset herfor.
    - [x] Eksempel på RSA, herunder https og certifikater (mangler!)
    - [ ] Hvordan verden ville være uden RSA
    - [ ] UNI login som eks re: `[a-z]{3}[0-9]{2}[a-z]{3}`

5. Konklusion
