# Programmēšana - pamatkurss.
**Svarīgi**
Autors: **Veronika Kalniņa**
## Kā palaist.
- Atver failu.
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
 1. kad programma prasa ievadīt bāzes punktus (kodā: 'int()'), skaitļa vietā ir ierakstīti burti (piemēram, vārds "desmit"). Kļūda radīsies programmas 2. rindā.
 2. kad programma prasa ievadīt reizinātāju (kodā: 'float()'), skaitlis ir ierakstīts ar latvisko komatu (piemēram, "1,5"), nevis ar punktu.
 ## Secinājums
 Lai programma strādātu bez kļūdām, lietotājs drīkst ievadīt tikai ciparus, ievadot burtus vai daļskaitļus ar komatu punkta vietā, Python nespēj tos konvertēt par matemātiskiem skaitļiem un apstādina darbu ar 'ValueError', jo komats šajā valodā ir datu atdalīšanai.
# int() ap input()
 *Funkcija input() vienmēr nolasa lietotāja ievadi kā tekstu (str), kad izmanto + zīmi starp diviem tekstiem, dators tos nesaskaita bet gan apvieno, rezultātā "5" + "5" kļūst par 55.
 *Funkcija int() paņem lietotāja ievadīto tekstu "5" un pārveido to par matemātiskiem skaitļiem, ar kuriem var veikt kalkulācijas, tātad mainīgajos glabājas īsti skaitļi, un plus zīme veic matemātisko saskaitīšanu: 5 + 5 = 10.
# varoņa lapas testēšanas secinājumi
*Palaižot programmu ar HP vērtību 0, programma nesalūza, bet izskaitļoja '0.0' bojājumu. Spēles loģikā tas nav pareizi, jo ja varoņa nav, tas nevar uzbrukt.
*Palaižot programmu ar HP vērtību -50, programma izskaitļoja '-60.0' bojājumu. Negatīvs bojājums spēlēs nav loģisks (tas darbotos kā dziedināšana).
*Palaižot programmu ar tukšu ievadi (Enter), parādās ValueError, jo funkcijas 'int()'un 'float()' nevar pārvērst tukšumu par skaitli.
*Palaižot programmu ar tekstu 'abc' 'float()' vietā, parādās ValueError, jo funkcija 'float()' nemāk burtus pārvērst par daļskaitli.
# Matemātika un f-string
* **Parastā dalīšana (`/`):** `17 / 5` rezultāts ir **3.4**
* **Veselo skaitļu dalīšana (`//`):** `17 // 5` rezultāts ir **3** (cik pilnas reizes skaitlis ietilpst)
* **Dalīšanas atlikums (`%`):** `17 % 5` rezultāts ir **2** (kas paliek pāri)
* **Kāpināšana (`**`):** `2 ** 3` rezultāts ir **8** (2 pakāpē 3)
Konstrukcija `:.1f` figūriekavās (piemēram, `{videji:.1f}`) **noapaļo decimālskaitli līdz precīzi vienam ciparam aiz punkta**. Pirms labojuma skaitlis bija garš un neprecīzs (`3.4000000000000004`), bet pēc tā – tieši `3.4`.
Kad līmenis pieaug divas reizes (piemēram, no 5 uz 10), spēks pieaug **4 reizes** (no 25 uz 100). 
Tas ir tāpēc, ka formula izmanto kāpināšanu kvadrātā ($2^2 = 4$). Ja līmeni dubulto ($2 \times \text{līmenis}$), tad spēks palielinās par $2^2$ reizēm jeb četrkāršojas.
# Koda stils un komentāri
*Komentāri (# ): Dators tos ignorē, bet tie palīdz cilvēkiem saprast koda nolūku. Jāraksta tas, kāpēc kods kaut ko dara, nevis jāapraksta acīmredzamo.
*Snake Case: Python standarts Variables (mainīgo) nosaukumiem. Visi burti ir mazie un vārdus atdala ar apakšsvītru.
*PEP 8: Oficiālā Python stila rokasgrāmata. Viens no galvenajiem noteikumiem: vienmēr lieto atstarpes ap operatoriem.
*Docstrings (Dokumentācijas virknes) """ : Vairāku rindu komentāri faila sākumā vai funkcijās, lai aprakstītu kopējo mērķi un autorību. 
