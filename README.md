# Programmēšana - pamatkurss.
**Svarīgi**
Autors: **Veronika Kalniņa**
## Kā palaist.
- Atver "sveiciens.py".
- Nospied Run Python File.
## Licence
MIT License ir atvērta programmatūras licence, kas ļauj programmatūru brīvi izmantot, kopēt un modifcēt.

.md nav parasts teksta fails, jo tajā var izmantot Markdown formatējumu, piemēram, treknrakstu un virsrakstus.
## Kāpēc MIT.
Es izvēlējos MIT licenci, jo tā ir vienkārša un ļauj citiem brīvi izmantot un modificēt manu kodu. Man patīk, ka tā ir viegli saprotama un tai ir maz prasību.
## MIT licences prasība
Izplatot programmu, jāsaglabā autortiesību un licences paziņojums.
## GPL licences prasība
Izplatot modificētu programmu, tās pirmkodam jābūt pieejamam ar to pašu GPL licenci.
# 1. uzdevums - Trīs datu tipi ar type()
* a ir str
* b ir int
* c ir float
# 3. uzdevums - Programmas darbības pārtraukšana ar nepareizu ievadi
 1. kad programma prasa ievadīt bāzes punktus (kodā: 'int()'), skaitļa vietā ir jāieraksta burti (piemēram, vārds "desmit"). Kļūda radīsies programmas 2. rindā.
 2. kad programma prasa ievadīt reizinātāju (kodā: 'float()'), skaitlis ir jāieraksta ar latvisko komatu (piemēram, "1,5"), nevis ar punktu.
 ## Secinājums
 Lai programma strādātu bez kļūdām, lietotājs drīkst ievadīt tikai ciparus, ievadot burtus vai daļskaitļus ar komatu punkta vietā, Python nespēj tos konvertēt par matemātiskiem skaitļiem un apstādina darbu ar 'ValueError', jo komats šajā valodā ir datu atdalīšanai.