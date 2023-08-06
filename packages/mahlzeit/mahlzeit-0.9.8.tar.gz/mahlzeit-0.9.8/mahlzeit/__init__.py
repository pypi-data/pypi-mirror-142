import re
import sys
from decimal import Decimal


class MahlzeitBase():
    def len(self, attribute):
        """
        return the length including gewichtung of attribute (e.g. bezahler or esser)
        """
        return sum([ getattr(e, 'gewichtung', 1) for e in getattr(self, attribute) ])

    def iterate(self, attribute):
        """
        Iterate over an attribute e.g. bezahler, esser, or bezahlter which all can take a
        string or (tuple of strings or Esser) or (list of strings or Esser)
        In case of an Esser, the gewichtung is taken into consideration
        """
        if type(getattr(self, attribute)) is str:
            yield getattr(self, attribute), self.betrag
        else:
            for p in getattr(self, attribute):
                yield getattr(p, 'name', p), Decimal(self.betrag * Decimal(getattr(p, 'gewichtung', 1)))/Decimal(self.len(attribute))


class Esser():
    def __init__(self, name, gewichtung):
        if type(gewichtung) not in (float, int, Decimal):
            raise Exception('gewichtung must be float, int, or Decimal')
        if gewichtung < 0:
            # allow gewichtung 0 for placeholding
            raise Exception('gewichtung muss >= 0 sein')
        if re.search(r' {2,}', name):
            raise Exception('account names cannot have more than two adjacent spaces "{}"'.format(name))
        self.name = name
        self.gewichtung = Decimal(gewichtung)

    def __str__(self):
        return "%s (%.2f)" % (self.name, self.gewichtung)


class Einkauf(MahlzeitBase):
    def __init__(self, betrag, esser, bezahler, datum=None, description=None, comment=None):
        """
        betrag may be negative to indicate income e.g. voucher or thelike
        """
        if type(esser) not in (str, list, tuple):
            raise Exception('esser must be str, list or tuple')
        if type(bezahler) not in (str, list, tuple):
            raise Exception('bezahler must be str, list or tuple')
        self.betrag = Decimal(betrag)
        self.comment = comment
        self.bezahler = bezahler
        self.datum = datum
        self.description = description
        if isinstance(esser, str):
            self.esser = (esser,)
        else:
            self.esser = esser

    def __str__(self):
        return "Einkauf {}; {}; {}".format(self.betrag, ','.join(self.esser), self.bezahler)


class Bezahlung(MahlzeitBase):
    def __init__(self, bezahler, bezahlter, betrag, datum=None, description=None, comment=None):
        if betrag <= 0:
            raise Exception('betrag <= 0')
        if type(bezahler) not in [str, tuple, list]:
            raise Exception('bezahler must be str, tuple, or list')
        if type(bezahlter) not in [str, tuple, list]:
            raise Exception('bezahlter must be str, tuple, or list')
        self.betrag = Decimal(betrag)
        self.bezahler = bezahler
        self.bezahlter = bezahlter
        self.comment = comment
        self.datum = datum
        self.description = description


class Mahlzeit():
    def __init__(self):
        self.einkaeufe = list()
        self.bezahlungen = list()

        # for usage in context
        self.datum = None
        self.description = None
        self.comment = None

    def __call__(self, datum=None, description=None, comment=None):
        self.datum = datum
        self.description = description
        self.comment = comment
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.datum = None
        self.description = None
        self.comment = None

    def einkauf(self, betrag, esser, bezahler, datum=None, description=None, comment=None):
        self.einkaeufe.append(Einkauf(Decimal(betrag), esser, bezahler,
            datum=datum if datum else self.datum,
            description=description if description else self.description,
            comment=comment if comment else self.comment,
        ))

    def bezahlung(self, bezahler, bezahlter, betrag, datum=None, description=None, comment=None):
        self.bezahlungen.append(Bezahlung(bezahler, bezahlter, Decimal(betrag),
            datum=datum if datum else self.datum,
            description=description if description else self.description,
            comment=comment if comment else self.comment,
        ))

    def calc(self):
        ausgleich = dict()
        for e in self.einkaeufe:
            for name, betrag in e.iterate('bezahler'):
                ausgleich[name] = ausgleich.get(name, Decimal(0)) - betrag
            for name, betrag in e.iterate('esser'):
                ausgleich[name] = ausgleich.get(name, Decimal(0)) + betrag
        for b in self.bezahlungen:
            for bzahler, bzahlbetrag in b.iterate('bezahler'):
                ausgleich[bzahler] = ausgleich.get(bzahler, Decimal(0)) - bzahlbetrag
            for bzahlter, bzahlterbetrag in b.iterate('bezahlter'):
                ausgleich[bzahlter] = ausgleich.get(bzahlter, Decimal(0)) + bzahlterbetrag

        # sanity check makes sure that we produce at most 0.01 error per einkauf
        assert sum([ b for _, b in ausgleich.items() ]) <= (Decimal(0.01) * len(self.einkaeufe)), sum([ b for _, b in ausgleich.items() ])

        return ausgleich

    def pretty(self):
        self.pprint()

    def pprint(self):
        for k, v in sorted(self.calc().items(), key=lambda x: -x[1]):
            print("%10s %.2f" % (k, v))

    def reset(self):
        self.einkaeufe = list()
        self.bezahlungen = list()

    def journal(self):
        for eink in self.einkaeufe:
            if not eink.datum and not eink.description:
                print("Datum and description not set for {}. Cannot output journal".format(eink), file=sys.stderr)
                sys.exit(1)
            if eink.comment:
                print(";", eink.comment)
            print(eink.datum, eink.description)
            for name, betrag in eink.iterate('bezahler'):
                print("\t%s:einkauf:bezahler\t\t%.3f" % (name, -betrag))
            for name, betrag in eink.iterate('esser'):
                print("\t%s:einkauf:esser\t\t%.3f" % (name, betrag))
            print("\trounding")
            print()

        for bez in self.bezahlungen:
            if not bez.datum and not bez.description:
                print("Datum and description not set for {}. Cannot output journal".format(eink), file=sys.stderr)
                sys.exit(1)
            if bez.comment:
                print(";", bez.comment)
            print(bez.datum, bez.description)
            for name, betrag in bez.iterate('bezahler'):
                print("\t%s:bezahlung:bezahler\t\t%.3f" % (name, -betrag))
            for name, betrag in bez.iterate('bezahlter'):
                print("\t%s:bezahlung:bezahlter\t\t%.3f" % (name, betrag))
            print("\trounding")
            print()
