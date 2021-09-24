

# MC-alfa_homeworks
> homework assignments from MC alfa web programming course


## Python basics

* exercise_1 -> 2.1. Uzrakstīt programmu Python valodā, kas prasa lietotājam ievadīt veselu
nenegatīvu skaitli, un pēc tam izdrukā šo skaitli kvadrātā. Piemēram, lietotājs
ievada skaitli 5, programma izvada rezultātu 25.

* exercise_2 -> 2.2. Uzrakstīt programmu Python valodā, kas prasa lietotājam ievadīt atlikušo
degvielas daudzumu auto bākā. Ja atlikušais daudzums ir virs 10 litriem, tad
programma izdrukā vārdu «daudz»; ja daudzums ir <=10, bet lielāks par 0, tad
programma izdrukā «maz»; ja daudzums ir 0, tad izdrukā «nav degvielas».

* exercise_3 -> 2.3. Python valodā uzrakstīt programmu, kas darbojas kā vienkāršs kalkulators.
Lietotājs var ievadīt 2 veselus skaitļus un izvēlēties aritmētisko darbību.
Programma uz ekrāna izdrukā rezultātu, un pēc tam piedāvā vai nu rēķināt no
jauna, vai beigt darbu.

* exercise_4 -> 2.4. Python valodā uzrakstīt programmu, kas prasa ievadīt skaitli n robežās 1-
1000 un pēc tam izdrukā skaitļu virkni 1 2 3 4 5 ..... n. Piemēram, ja ievada n=3,
tad izdrukā 1 2 3.

* exercise_5 -> 2.5. Python valodā uzrakstīt programmu, kas prasa ievadīt skaitli n robežās 1-
1000 un pēc tam izdrukā nepāra skaitļu virkni 1 3 5 7..... n. Piemēram, ja ievada
n=11, tad izdrukā 1 3 5 7 9 11.

* exercise_6 -> 2.6. Python valodā uzrakstīt programmu, kas ļauj 2 lietotājiem spēlēt spēli
«akmens šķēres papīrītis». Lietotāji izdara gājienus, ievadot skaitļus (1-akmens,
2-šķēres, 3-papīrs), un programma nosaka rezultātu. Pēc spēles beigām
programma piedāvā spēlēt vēlreiz vai arī iziet no spēles.


## Python functions

* exercise_1 -> 1. Uzrakstīt funkciju Python valodā, kas kā parametrus saņem divas simbolu virknes, bet kā
rezultātu uz ekrāna izdod šo virkņu «pinumu», kur viens simbols ir no pirmās virknes, bet
otrais no otrās

* exercise_2 -> 2. Uzrakstīt funkciju Python valodā, kas ģenerē funkcijas izsaucēja norādīta skaita nejaušus
skaitļus no 1 līdz 10 un saglabā tos List sarakstā (programmas sākumā lieto komandu import
random un pēc tam funkciju random.randint(1,10), kā arī uzrakstīt Python funkciju, kas
aprēķina List iekļauto skaitļu reizinājumu; abu funkciju rezultātu izvadīt uz ekrāna

* exercise_3 -> 3. Uzrakstīt programmu Python valodā, kas List saglabā 10 nejaušus skaitļus (0-100) un pēc
tam sakārto šo List augošā secībā, izmantojot gan Bubble Sort algoritmu (piem.,
https://www.geeksforgeeks.org/bubble-sort/), kas realizēta kā atsevišķa Python funkcija,
gan izmantojot List iebūvētās iespējas; abus kārtošanu rezultātus izvada uz ekrāna.


## MariaDB SQL querry

> Mājas darbs (datu bāzu programmēšana) Uzdevums
> Lejupielādē un uzstādi mariadb serverī parauga datu bāzi (nation.sql) no https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/

1. Izveido SQL pieprasījumu, kas atgriež sarakstu ar 10 populārākajām valstu oficiālajām valodām (country_languages, languages) pasaulē un saistīto valstu (countries) skaitu un summāro iedzīvotāju skaitu 2018.g. (country_stats). Rezultējošā tabulā ir šādas kolonnas: language_id, language, number_of_countries, population. Saraksts sakārtots pēc population dilstošā secībā.

2. Izveido SQL pieprasījumu, kas atgriež visas valstis (countries) no Eastern Europe reģiona (regions) un pievieno kolonnu ar reģiona nosaukumu un kolonnu ar kontinenta (continents) nosaukumu. Rezultējošā tabulā ir šādas kolonnas: country_id, name, area, gdp (par 2018.g.), population (par 2018.g.), region, continent. Iegūto tabulu saglabāt datu bāzē kā tabulu countries_eastern_europe

3. Izveido SQL pieprasījumu, kas atgriež visu reģionu (regions) sarakstu ar to valstu (countries) skaitu, summāro platību, un summāro iedzīvotāju skaitu 2018. gadā (country_stats). Rezultējošā tabulā ir šādas kolonnas: region_id, name, area, population. Saraksts sakārtots pēc population augošā secībā

Iesniedz kā vienu datni ar 3 SQL skriptiem. Pie attiecīgā skripta piekomentē uzdevuma numuru.


## django webpage
> Lejupielādē un uzstādi mariadb serverī parauga datu bāzi (nation.sql) no https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/ . 
>Izveido Django tīmekļa vietni, kas atbilst šādām prasībām:

1. Ievadot tīmekļa servera adresi, izvadi lapu "Valstis" ar tabulu ar valstu datiem:
a) kolonnas: Valsts [nosaukums], Kods, Platība, Iedz. sk. (2018), Reģions [nosaukums], Kontinents [nosaukums]; 
b) ierakstus sakārto pēc valsts nosaukuma.

2. Valstu tabulā klikšķinot uz valsts nosaukumu, piedāvā lapu valsts ieraksta labošanai:
a) lauki: Nosaukums, Kods (2), Kods (3), Platība, Reģions;
b) reģionu piedāvā izvēlēties no saraksta ar reģionu nosaukumiem;
c) saglabā ar pogu "Saglabāt"; pēc sekmīgas saglabāšanas atgriezies uz valstu tabulu (nefiltrēts);
d) atcel ar pogu "Atcelt" - aizver lapu un atver valstu tabulu (nefiltrēts).

3. Valstu tabulā klikšķinot uz reģiona nosaukumu, tabulā parādi tikai tā reģiona valstis:
a) virs tabulas novieto saiti "Atcelt filtru"; to nospiežot, saiti noņem un atkal parādi visas valstis

4. Valstu tabulā klikšķinot uz kontinenta nosaukumu, tabulā parādi tikai tā kontinenta valstis:
a) virs tabulas novieto saiti "Atcelt filtru"; to nospiežot, saiti noņem un atkal parādi visas valstis.

Pirms iesniegšanas tīmekļa vietnes lapas mapi ar datnēm un apakšmapēm saarhivē un no arhīva lūdzu izņem virtuālās vides ('env') mapi. Iesniedz koriģēto arhīvu. 


