# poznan-trams-network-analysis
Dane z:
https://www.ztm.poznan.pl/pl/rozklad-jazdy/16


Przystanki:
Każdy przystanek ma swój kod i nazwę, np. Franowo (FRWO42) przy czym kod jednoznacznie identyfikuje przystanek. 

Do zebrania potrzebne sa pliki:
1) Mapowanie kod-nazwa, w formacie:
```
kod, nazwa, x, y
FRWO42, Franowo, ?, ?
SZWA42, Szwajcarska, ?, ?
...
```

2) Następnie dla każdej linii, np. 16 dwa pliki: 16there oraz 16back, a wewnątrz po kolei kody przystanków.


# Setup
```
pip install -r requirements.txt
jupyter notebook
```