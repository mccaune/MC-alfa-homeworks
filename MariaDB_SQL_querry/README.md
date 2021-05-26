# MC-alfa_homeworks
homework assignments from MC alfa web programming course

#mariaDB SQL querry

Mājas darbs (datu bāzu programmēšana) Uzdevums

Lejupielādē un uzstādi mariadb serverī parauga datu bāzi (nation.sql) no https://www.mariadbtutorial.com/getting-started/mariadb-sample-database/

1. Izveido SQL pieprasījumu, kas atgriež sarakstu ar 10 populārākajām valstu oficiālajām valodām (country_languages, languages) pasaulē un saistīto valstu (countries) skaitu un summāro iedzīvotāju skaitu 2018.g. (country_stats). Rezultējošā tabulā ir šādas kolonnas: language_id, language, number_of_countries, population. Saraksts sakārtots pēc population dilstošā secībā.

2. Izveido SQL pieprasījumu, kas atgriež visas valstis (countries) no Eastern Europe reģiona (regions) un pievieno kolonnu ar reģiona nosaukumu un kolonnu ar kontinenta (continents) nosaukumu. Rezultējošā tabulā ir šādas kolonnas: country_id, name, area, gdp (par 2018.g.), population (par 2018.g.), region, continent. Iegūto tabulu saglabāt datu bāzē kā tabulu countries_eastern_europe

3. Izveido SQL pieprasījumu, kas atgriež visu reģionu (regions) sarakstu ar to valstu (countries) skaitu, summāro platību, un summāro iedzīvotāju skaitu 2018. gadā (country_stats). Rezultējošā tabulā ir šādas kolonnas: region_id, name, area, population. Saraksts sakārtots pēc population augošā secībā

Iesniedz kā vienu datni ar 3 SQL skriptiem. Pie attiecīgā skripta piekomentē uzdevuma numuru.
