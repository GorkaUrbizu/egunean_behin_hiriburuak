# Egunean behin wikidata hiriburuak non?
Munduko herrialde ezberdinetako hiriburuen kokapenari buruzko galderak egin ditugu, Wikipedian oinarrituta. Hiru hiriburu(+herrialde) eman, eta zein hiriburu dagoen [ipar|hego|mendeb|eki]aldeen galdetuko dugu. Horretarako, Wikidatatik hiriburuaren koordenatuak erauzi, eta 3 hiriburu ausaz hartuko dira, eta norabide horretarago (iparralderago adib) kokatzen dena (5ºko marginarekin) izango da erantzun egokia.

Zein hiriburu dago Iparralderago?

-Helsinki (Finlandia) [Z]
-Tokio (Japonia) [O]
-Lisboa (Portugal) [O]

horrela, miloika galdera ezbedin sortu daitezke (4 norazko, 200 herrialde).

Hurbilpen bera erabili liteke, euskal herriko herriekin, edota, munduko hirien koordenatuak hartu ordez, itsaso mailarekiko altuera erabiliz.


## Wikidatako kontsulta
Wikipediako datuak ateratzeko, Wikidatako Query sisteman kontsulta bat idatzi dugu.:

#List of present-day countries and capital(s) + coordinates
SELECT DISTINCT ?country ?countryLabel ?capital ?capitalLabel ?coordinates ?lon ?lat
WHERE
{
  ?country wdt:P31 wd:Q3624078 .
  #not a former country
  FILTER NOT EXISTS {?country wdt:P31 wd:Q3024240}
  #and no an ancient civilisation (needed to exclude ancient Egypt)
  FILTER NOT EXISTS {?country wdt:P31 wd:Q28171280}
  ?country wdt:P36 ?capital .
  ?capital wdt:P625 ?coordinates .
  ?capital p:P625 ?coordinate .
  ?coordinate psv:P625 ?coordinate_node .
  ?coordinate_node wikibase:geoLatitude ?lat .
  ?coordinate_node wikibase:geoLongitude ?lon .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "eu" }
}
ORDER BY ?countryLabel



Honek egiten duena da Wikidatako elementuak arakatu, eta honako datuak eskuratzen ditugu konsultarekin.
- Herrialdea
- Hiriburua (herrialdearena)
- Koordenatuak (hiriburuarenak)
- Latitudea (koordenatuarenak)
- Longitudea (koordenatuarenak)

## Konsultako datuetatik galderak idaztera

python3 galderakSortu.py 

exekutatuta, csv fitxategitik wikipediatik erauzitako informazioa hartu eta galderak sortuko dira.

100K galdera segundu bakarrean sortzen dira.

Oharra, programak ez du dependentziarik, baina python3.6 behar du, f"string"ak erabiltzeko.
