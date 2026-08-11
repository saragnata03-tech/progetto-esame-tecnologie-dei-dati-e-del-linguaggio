"""
RQ2 - Analisi lessicale delle sinossi (narrativa vs giallo/thriller)
Input:  dati/03_sinossi_24_titoli.xlsx
Output: statistiche di lunghezza + parole più frequenti per genere,
        con esclusione di stopword e nomi propri (euristica maiuscola
        non a inizio frase).
Esegui con: python analisi_lessicale.py
"""
import openpyxl
import re
from collections import Counter
import statistics
import json

STOPWORDS = set("""
il lo la i gli le un uno una di a da in con su per tra fra e o ma se non
che chi cui come quando dove perché mentre dopo prima poi anche ancora
già mai sempre più meno molto poco tanto tutto tutti tutta tutte
si è sono era erano stato stata stati state essere ha hanno aveva avevano avere
suo sua suoi sue loro lei lui io tu noi voi mi ti ci vi
questo questa questi queste quello quella quelli quelle
al allo alla ai agli alle del dello della dei degli delle nel nello nella nei negli nelle
sul sullo sulla sui sugli sulle col coi un due tre
viene vengono venuto venuta essa essi proprio propria propri proprie
all dell nell sull dall quest cos c' un' e' è dev
può deve dovrebbe fa fare stessa stesso stessi stesse
ogni altro altri altra altre qualche qualcuno qualcosa
""".split())

def trova_nomi_propri(testo):
    segmenti = re.split(r'(?<=[.?!])\s+', testo)
    nomi_propri = set()
    for segmento in segmenti:
        parole = re.findall(r"[A-Za-zàèéìòùÀÈÉÌÒÙ]+(?:['’][A-Za-zàèéìòù]+)?", segmento)
        for i, parola in enumerate(parole):
            if i == 0:
                continue
            if parola[0].isupper():
                nomi_propri.add(parola.lower())
    return nomi_propri

def pulisci_e_tokenizza(testo, stopword_estese):
    testo = testo.lower()
    testo = re.sub(r"[’']", " ", testo)
    parole = re.findall(r"[a-zàèéìòù]+", testo)
    return [p for p in parole if p not in stopword_estese and len(p) > 2]

def main():
    wb = openpyxl.load_workbook("../dati/03_sinossi_24_titoli.xlsx")
    righe = list(wb.active.iter_rows(values_only=True))
    header = righe[0]
    libri = [dict(zip(header, r)) for r in righe[1:] if dict(zip(header, r)).get("sinossi")]

    tutti_nomi_propri = set()
    for l in libri:
        tutti_nomi_propri.update(trova_nomi_propri(l["sinossi"]))
    stopword_estese = STOPWORDS | tutti_nomi_propri

    per_genere = {"narrativa_contemporanea": [], "giallo_thriller": []}
    lunghezze = {"narrativa_contemporanea": [], "giallo_thriller": []}

    for l in libri:
        genere = l["genere"]
        parole = pulisci_e_tokenizza(l["sinossi"], stopword_estese)
        per_genere[genere].extend(parole)
        lunghezze[genere].append(len(l["sinossi"].split()))

    print("=== LUNGHEZZA MEDIA SINOSSI ===")
    for g, lens in lunghezze.items():
        print(f"{g}: {statistics.mean(lens):.0f} parole (n={len(lens)})")

    print("\n=== TOP 15 PAROLE PER GENERE (nomi propri esclusi) ===")
    risultati = {"lunghezze": lunghezze, "top_parole": {}}
    for g, parole in per_genere.items():
        top = Counter(parole).most_common(15)
        risultati["top_parole"][g] = top
        print(f"\n--- {g} ---")
        for parola, freq in top:
            print(f"  {parola}: {freq}")

    with open("risultati_analisi_lessicale.json", "w", encoding="utf-8") as f:
        json.dump(risultati, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
