# Noter til fremlæggelse
## Hvad skal jeg snakke om
- Mit emne
- En kort konklusion på emnet
- Delkonklusioner
- Hvordan fagene er brugt, herunder empiri og teori/metode
- Muligheder/begrænsninger ved fagene

## Detaljeret
**Kort intro:**
Jeg har skrevet en opgave som handler om onlinesikkerhed, herunder RSA-metoden og andre sikkerhedsforanstaltninger som blandt andet hashing og online verificering.

**Konklusion:**
Opgaven konkluderes ved en opsumering af hovedpunkterne fra opgaveformuleringen. Derefter konkluderer jeg på at RSA er en helt essentiel del af vores hverdag, stort set uanset hvad vi laver, samt at hashing også er meget vigtig i den digitale hverdag vi lever i. Alt dette bygger på teorien om at det er svært at primtalsfaktorisere et tilpas stort tal, hvis denne teori på den eller eller anden måde brydes, vil hele verden være i en svær knibe.

**Delkonklusioner:**
1. Hashing er (modsat RSA) brugt til at "envejskryptere" data, dette bruges dog stadig f.eks. til at lagre kodeord og autentificering af personer/data online, for at gøre processen nemmere.
2. Samtidig er det vist, hvordan hverken RSA eller hashing ofte er gode at bruge alene, det er vigtigt at man som sikkerhedsudvikler, tager nødvendige foranstaltninger, for at sikre sikkerheden af sine brugere.

#### SOP som metodefag

**Mat:**
- Inden for matematikken har jeg brugt metoder som *talteori*, til at redegøre for hvordan RSA er opbygget og netop den talteori, som ligger bag metoden.
- Dette bygger naturligvis på *deduktion* og *beviser*, hvor jeg altså argumenterer for hvorfor noget virker på netop den måde jeg har beskrevet. Det leder frem til disse *matematiske ræsonnementer*, som altså er en lang række argumenter, som argumenterer for logikken.
- *Analytisk løsning* har også været en stor del af arbejdet med opgaven, da al talteorien ikke blot skal bevises ved ét tilfælde, men ved alle!
- *Eksempelføring* har også fyldt en stor del af opgaven, det er både på det lille og det store plan, blandt andet idet der kommer eksempler på anvendelse af Euclids algoritme. Eller i det sidste afsnit, hvor hele protokollen for RSA bliver gennemgået ved et matematisk eksempel.

**Prg:**
- Metoden *protokoller* fylder også en væsentlig del af opgaven, da RSA er en metode i sig selv, skal der naturligvis opstilles en protokol for anvendelse af denne, samt mange andre metoder i forbindelse med denne.
- Derudover er man også ofte i programmering nødt til at forestille sig hvordan man skal bære sig ad med at *løse et problem, rent logisk* først. Førend at man kan programmere det.
- Slutteligt er det naturligvis nødvendigt at læse en eller anden form for *dokumentation* af et program, inden man kan bruge det. Dette har jeg blandt andet gjort ved `hashcat` og `gpg`, men også biblioteker som `hashlib`. Derudover har det selvfølgelig været læsning af dokumentation på mere officielle ting, såsom *standarder* inden for internetbrug, såsom hvordan man bruger certifikater eller `https` standarden.

**Tværfaglig:**
- *Sammenligning* af metoder eller fremgangsmåder er en metode, som dækkes af begge fagene, det er lidt af en *meta-metode* så at sige, den kan egentlig bruges i alle fag, men er samtidig meget vigtig, for forståelsen af et emne.

#### Empiri
- *Litteratur* er et af de mere overordnede emner inden for empiriet, jeg har brugt udgivede bøger, da jeg på den måde har kunne sikre mig validiteten af det fakta, som står i bogen.
- Som tidligere nævnt er dokumentationslæsning en del af metoderne i programmering, derudover er det også empiri at læse *dokumentation* af et program, for på den måde at blive klogere på hvordan det virker.
- *Virkelighedsdata* er selvfølgelig også en del af den empiri jeg har brugt, det er blandt andet UNI-login informationerne, som jeg har brugt i forbindelse med en vurdering af hvilke faktoere der er vigtige ved login, og hvad man kan gøre for at øge sikkerheden. Derudover ligger virkelighedsdataen bl.a. også i videoen, hvor Prof. Pound illustrerer hvordan man bryder kodeord vha. `hashcat`.








## Overvej
- Hvordan er der samspil mellem fagene
- Er der en rød tråd?
- Det er svært at omskrive matematik, da det er meget fakta.
- Empiri (programmering, UNI-login osv.)
- Kildekritik
- Lidt kodeudtræk?

## Metoder
- Prg
    - Protokoller
    - Trial and error
    - Skitsering af ideer
    - Dokumentationslæsning (biblioteker)
- Mat
    - Beviser
    - Talteori
    - Redegørelse for emne
- Samlet
    - Vurdering
    - Sammenligninger

## Kommentar
Et af bedømmelseskriterierne er evnen til at udvælge de vigtigste konklusioner fra opgaven. Det betød en del, at eleverne valgte ikke at redegøre for alle opgavens mindre detaljer men valgte det vigtigste ud. Ud over en række særfaglige spørgsmål kunne typiske spørgsmål være:

- Hvordan spiller fagene sammen?
    - Programmering er jo i bund og grund anvendt matematik og logik. Hvorfor der på den måde er rigtig godt sammenspil mellem de to fag.
- Hvad ville det give, hvis du havde valgt andre fag?
    - Det ville formentlig være svært at finde to fag der passer bedre på emnet, end lige netop de jeg har valgt...
- Hvilke metoder har du valgt - kunne man have valgt andre?
    - Se metode afsnit
    - Jeg kunne
- Beskriv den empiri du har arbejdet med.
- Hvilke studiemetoder har du valgt at arbejde med og hvorfor?
