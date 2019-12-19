# TODO
* **Læs nu lige igennem, for sammenhæng**
* **flere referencer!**
* kode til kryptering i Python
* Flyt evt. hashcat til sektion 2
* haveibeenpwned.com
* beviser i bilag
* fjern bilag som ikke er i brug
* Sammenhæng mellem afsnit, tak!
* nummer på definitioner
* kollision af hashfunktioner
* dobbelt Z til phi
* \\equiv ved inv mod
* fag på forside

## inden aflevering
* skriv resume
* formatering ved sideskift ovs

# opgaveformulering
* Redegør for talteorien bag RSA kryptering. Forklar nødvendigheden af primtal og hvordan RSA metoden fungerer.
* Gør kort rede for hashing.
* Analyser forskellen på hashing og kryptografi og hvilken rolle de har i forhold til sikkerhed.
* Vurder hvorfor RSA er vigtigt i forbindelse med sikkerhed ved logins

## stikord
- [x] rainbowtables
- [x] brute force
- [x] hashtable
- [x] gpg
- [x] http vs https
- [x] certifikater
- [x] 2fa
- [x] kvantecomputere
- [x] DES-key
- [x] password managers


## links

pow til Python: https://docs.python.org/3/library/functions.html#pow

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

0. Intro (1)
    - [x] Kryptografi / kryptologi
    - [ ] Hvad er RSA og hvad bygger det på?

1. Talteori (6)
    - [x] Kort intro til mod og primtal (måske for lang)
    - [x] Noget om største fælles divisor og indbyrdes primisk
    - [x] Dernæst eulers funktion
    - [x] Så til de sætninger som er vigtige...

2. Hashing (2)
    - [x] Hvad er hashing - pseudorandom - envejs
    - [x] Evt. forskellige hashfunktioner
    - [x] Noget om hashtabeller?

3. Forskel (5)
    - [x] Hvad er en protokol?
    - [x] Hvad er kryptografi?
    - [x] En protokol for kryptografi
    - [x] Hvordan man faktisk bruger RSA
    - [x] Derefter et eksempel på hashing og kodeord, herunder rainbowtables, salt og hashcat
    - [x] Brute-force (hvor er det defineret?)
    - [x] Så hvordan man bruger begge dele i hverdagen, til verificering, gpg, samt certifikater
    - [ ] En opsumering?

4. RSA (4)
    - [ ] Hvor bruger man det?
    - [x] Matematikken bag RSA, samt beviset herfor.
    - [x] Eksempel på RSA, herunder https
    - [x] UNI login som eks re: `[a-z]{3}[0-9]{2}[a-z]{3}`
    - [x] Hvordan verden ville være uden RSA

5. Konklusion (1)
    - [x] Kort opridsning af de 4 hovedpunkter
    - [ ] En, ja... konklusion (Skriv lidt mere, tak!)
