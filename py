def berechne_gesamtpreis(artikel, anzahl):
    if artikel == "Apfel":
        preis = 1.5 * anzahl
    elif artikel == "Banane":
        preis = 2.0 * anzahl
    elif artikel == "Orange":
        preis = 1.8 * anzahl
    else:
        preis = 0
    return preis

def drucke_rechnung(artikel, anzahl):
    if artikel == "Apfel":
        gesamtpreis = 1.5 * anzahl
    elif artikel == "Banane":
        gesamtpreis = 2.0 * anzahl
    elif artikel == "Orange":
        gesamtpreis = 1.8 * anzahl
    else:
        gesamtpreis = 0
    print(f"{anzahl} {artikel}: {gesamtpreis} Euro")
