# Was ist das

Ihr kauft des Öfteren für Kollegen Essen, kocht und esst zusammen. Nächstes Mal
zahlt jemand anderes. Wer schuldet wem nun wie viel Geld?

Zur Ausgabe stehen zur Verfügung:

- Formatiert als Konsolenausgabe
- Im [`ledger`-kompatiblen Format](https://hledger.org/hledger.html#journal-format) (dafür wird aber
  sowohl die Datums- als auch Beschreibungsannotation jeder Transaktion bzw.
  -gruppe benötigt)

Jeder Einkauf (bzw. Teil eines Einkaufs oder Kaufs) wird als Transaktion
gesehen (Betrag, Mitesser, Bezahler):

    m.einkauf(10, ('Person1', 'Person2'), 'Person1')

Da es sich um python handelt, kann man auch gleich Rechnungen (zum Beispiel in
Form mehrerer Posten pro Person anstellen:

    m.einkauf(5.5+6, 'Person1', 'Person2')

Die folgenden zwei Beispiele sind äquivalent:

    m.einkauf(11/2, 'Person1', 'Person1')
    m.einkauf(11/2, 'Person2', 'Person1')

    m.einkauf(11, ('Person1', 'Person2'), 'Person1')

Wenn Geld den Besitzer wechselt, hält man das mit `.bezahlung()` fest:

    m.bezahlung('Bezahler', 'Bezahlter', 5.5)

`.einkauf()` und `.bezahlung()` können entweder individuell mit weiteren
Argumenten (`datum= description= comment=` oder in einem Kontext gesammelt mit
weiteren Informationen (Datum, Beschreibung und Kommentar) angereichert werden:

    with m(datum='2022-02-11', description='Anlass/Gericht', comment='foo'):
    	m.einkauf(1, ('Person1', 'Person2'), 'Person1')

Ein minimales Beispiel:

```
$ cat ledger.py
```
```python
#!/usr/bin/env python3
from mahlzeit import Mahlzeit

m = Mahlzeit()

# Kommentar, worum es hier ging, vielleicht mit Datum
m.einkauf(11, ('Person1', 'Person2'), 'Person1')

m.pretty()
```

Beispiel für die Ausgabe eines `ledger`-kompatiblen Formats inklusive Auswertung
mit `hledger`:

```
python3 basic.py

$ cat ledger.py
#!/usr/bin/env python3
from mahlzeit import Mahlzeit

m = Mahlzeit()

with m(datum='2021/05/02', description='Essen 1'):
	m.einkauf(28.62, ('Jann', 'Flo', 'Max'), 'Flo')
	m.einkauf(2.22, ('Jann', 'Flo', 'Max'), 'Jann')
with m(datum='2021/05/03', description='Essen 2'):
	m.einkauf(14.24, ('Kai', 'Jann', 'Flo', 'Max'), 'Max')
	m.einkauf(2.90, ('Kai', 'Jann', 'Flo', 'Max'), 'Kai')
	m.einkauf(18.73, ('Julie', 'Jann', 'Flo', 'Max'), 'Flo')
with m(datum='2021/05/03', description='Essen 2'):
	m.bezahlung('Max', 'Flo', 5)

m.journal()

# use interactively as
$ hledger -f <(python3 main.py) balance
```

# Installation

Aktuell per `virtualenv`

```
virtualenv -p python3 venv
source venv/bin/activate
python3 setup.py install
python3 example.py
```

# Mehrgewichtige Esser

Ihr habt ein Paar in der Essgruppe, die manchmal Speisen gemeinsam mit einer Art
Gemeinschaftskonto kaufen und deshalb gemeinsam veranlagt werden müssen?
Vielleicht gibt es jemanden, der immer weniger als alle anderen isst, und
deshalb nur mit Faktor 0,5 berechnet werden soll?

```
#!/usr/bin/env python3
from mahlzeit import Mahlzeit, Esser as E

m = Mahlzeit()

m.einkauf(15, ('Laura', 'Nils', E('Katja_Martin', 2), 'Max'), 'Katja_Martin')
m.pprint()
```

```
$ python3 main.py
       Max -3.00
      Nils -3.00
     Laura -3.00
Katja_Martin 9.00
```

# Tests

Tests laufen mit `make test`.
