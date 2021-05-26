# MC-alfa_homeworks
homework assignments from MC alfa web programming course

#django webpage
Lejupielādē un uzstādi mariadb serverī parauga datu bāzi (nation.sql) no https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/ . 

Izveido Django tīmekļa vietni, kas atbilst šādām prasībām:
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
