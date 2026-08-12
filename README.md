# Cartaceo vs Ebook: come cambia la copertina quando cambia il supporto
## Dashboard interattive (link diretti) - [Dashboard RQ1/RQ2 — grafici e tabella filtrabile](https://saragnata03-tech.github.io/progetto-esame-tecnologie-dei-dati-e-del-linguaggio/dashboard/01_dashboard_rq1_rq2.html) - [Moodboard e prompt visivi (Traccia 11)](https://saragnata03-tech.github.io/progetto-esame-tecnologie-dei-dati-e-del-linguaggio/dashboard/02_moodboard_prompt.html) - [Confronto AI vs copertina reale — slider interattivo](https://saragnata03-tech.github.io/progetto-esame-tecnologie-dei-dati-e-del-linguaggio/dashboard/03_confronto_ai_vs_editore.html)
Progetto per il corso **Tecnologie dei dati e del linguaggio** — analisi comparativa su 45 titoli dell'editoria italiana contemporanea (narrativa contemporanea e giallo/thriller), tra riuso visivo, linguaggio promozionale e pratiche editoriali del formato digitale.
## Nota sulle tracce di riferimento Questo progetto nasce come **ibrido dichiarato tra due tracce del corso**, unite dal filo conduttore delle copertine come oggetto di studio: la **Traccia 13 "Misurare il gusto"** (dati di mercato editoriale, metadati, linguaggio promozionale) è il riferimento metodologico per RQ1 e RQ2; la **Traccia 11 "Testo e immagine: descrivere, vedere, mostrare"** è il riferimento metodologico per RQ3, che ne applica quasi letteralmente il metodo previsto ("generazione di prompt visivi a partire dalle descrizioni e produzione di immagini con modelli generativi; confronto critico tra testo originale, prompt e immagine ottenuta"). L'ibridazione è una scelta consapevole, non un'imprecisione: le tracce del corso sono esplicitamente presentate come "spunti di partenza, non consegne chiuse".
## Modelli di intelligenza artificiale usati, e in che misura

- **Claude Sonnet 5 (Anthropic)** — usato per: progettazione della metodologia e delle domande di ricerca; scrittura e correzione del codice Python (`codice/analisi_lessicale.py`); costruzione delle tre dashboard HTML interattive; estrazione degli elementi visivi/simbolici dalle sinossi e costruzione dei 6 prompt per la generazione di immagini (Traccia 11); stesura di questo README. Le scelte finali su corpus, interpretazione dei risultati, limiti dichiarati e decisioni metodologiche (es. abbandono della raccolta automatica via API) sono state discusse con il modello ma decise e validate dall'autrice del progetto.
- **Gemini (Google)** — usato esclusivamente per la generazione delle 6 immagini di copertina a partire dai prompt visivi costruiti con Claude, nell'ambito del confronto AI vs copertina reale (Traccia 11, sezione "Testo → Immagine"). **Una sola generazione per titolo**, senza selezione tra più output (vedi nota metodologica nella sezione dedicata più sotto).

## Domande di ricerca e ipotesi

**RQ1 — Cosa cambia visivamente tra copertina cartacea ed ebook per lo stesso titolo, e questa variazione dipende dal genere editoriale o da un adattamento per la resa in miniatura (thumbnail)?**
*Ipotesi iniziale:* ci si aspettava un certo grado di adattamento tra i due formati (semplificazione per la resa in miniatura, differenze cromatiche o di impaginazione), e una divergenza più marcata nel genere con codificazione iconografica più forte (giallo/thriller) rispetto a uno più essenziale (narrativa contemporanea).

**RQ2 — Esistono pattern lessicali nelle sinossi che si associano al genere editoriale?**
*Ipotesi iniziale:* generi diversi (narrativa vs giallo/thriller) mobilitano un lessico promozionale sistematicamente diverso, coerente con le rispettive convenzioni di genere.

**RQ3 — Un generatore di immagini guidato da un prompt costruito a partire dalla sinossi produce una copertina concettualmente e visivamente vicina a quella scelta dall'editore?**
*Ipotesi iniziale:* un prompt fedele agli elementi descrittivi del testo dovrebbe produrre un'immagine ragionevolmente allineata alla copertina reale, in quanto entrambe derivano dallo stesso materiale narrativo di partenza.

## Dati e metodo

### Corpus
45 titoli dell'editoria italiana contemporanea (ultimi anni), suddivisi in 22 di narrativa contemporanea e 23 di giallo/thriller. La selezione ha privilegiato titoli recenti e di ampia diffusione (classifiche di vendita, cataloghi editoriali), integrati con titoli suggeriti dall'autrice del progetto in base alle proprie letture.

**Rappresentatività e criteri di esclusione (dichiarati esplicitamente):** il corpus non è un campione statistico casuale, ma una selezione per rilevanza/notorietà — non è quindi rappresentativo dell'intera produzione editoriale italiana, né dei generi meno mainstream o dell'editoria indipendente/di nicchia. Sono stati esclusi a priori: saggistica (fuori tema per le domande di ricerca, orientate alla narrativa), edizioni straniere non tradotte in italiano, titoli privi di una pagina prodotto pubblica reperibile per la raccolta manuale. Due titoli inizialmente selezionati sono risultati privi di edizione ebook (dato mantenuto nel corpus perché informativo, non escluso). Il campione è sufficiente per un'analisi esplorativa e per la discussione qualitativa dei pattern osservati, non per generalizzazioni statistiche forti sull'intero mercato editoriale italiano.

Per l'analisi lessicale delle sinossi (RQ2) è stato usato un sottocampione di **24 titoli** (12+12, bilanciato per genere), scelto includendo esplicitamente i casi "speciali" già emersi dal controllo visivo (il titolo con copertina divergente e i due titoli privi di edizione ebook) — riduzione decisa deliberatamente dopo che il controllo visivo su tutti i 45 titoli aveva già mostrato un pattern chiaro, per non appesantire inutilmente la raccolta dati manuale.

### Raccolta dati — nota metodologica importante
Il piano iniziale prevedeva la raccolta automatica di metadati e copertine tramite le API pubbliche di **Google Books** e **Open Library**. Questo approccio è stato **abbandonato dopo verifica empirica**, per due motivi documentati:

1. La quota gratuita e non autenticata di Google Books si è rivelata insufficiente (errori `429 Too Many Requests` persistenti, anche da rete personale non condivisa), e l'ottenimento di una chiave API richiedeva una verifica account non percorribile nei tempi del progetto.
2. Open Library, pur funzionante, ha mostrato una copertura molto scarsa per l'editoria italiana pubblicata negli ultimi 1-2 anni (verificato con test diretti: risposte HTTP 200 ma `numFound: 0` per titoli recenti).

Si è quindi optato per una **raccolta manuale documentata**: consultazione diretta di pagine editoriali pubbliche (IBS.it, siti degli editori) per ciascun titolo, con classificazione del confronto visivo cartaceo/ebook e trascrizione delle sinossi. Gli script Python scritti per il tentativo di raccolta automatica (non funzionanti in modo affidabile) non sono inclusi nella repository, ma restano parte del processo decisionale discusso più sopra. **Il codice Python è comunque parte integrante del progetto**: lo script `codice/analisi_lessicale.py`, incluso nella repository, è quello che ha effettivamente svolto tutta l'elaborazione dati di RQ2 (tokenizzazione, rimozione stopword, esclusione euristica dei nomi propri, conteggio delle frequenze) a partire dal dataset raccolto manualmente.

*Questo è un limite dichiarato del progetto: la raccolta non è riproducibile in automatico da chiunque rilanci uno script, ma il dataset raccolto (cartella `dati/`) è fisso, tracciato e riutilizzabile per rieseguire tutte le analisi successive.*

### Elaborazione
- **RQ1**: confronto visivo diretto (identica / diversa / nessuna edizione ebook) su tutti i 45 titoli, incrociato con la variabile genere.
- **RQ2**: tokenizzazione delle sinossi, rimozione stopword italiane, esclusione euristica dei nomi propri (parole capitalizzate non a inizio frase — vedi `codice/analisi_lessicale.py`), conteggio delle frequenze per genere.
- **RQ3**: per 6 titoli del campione, estrazione manuale degli elementi visivi/simbolici dalla sinossi (moodboard, categorizzati in luogo/oggetti-simboli/atmosfera/personaggio), costruzione di un prompt in lingua inglese per generatore di immagini, generazione con **Gemini** (Google), confronto critico manuale tra immagine generata e copertina reale pubblicata dall'editore.

  **Dettaglio dei passaggi manuali di controllo (dichiarati per trasparenza):** per 4 titoli su 6 è stata mantenuta la prima immagine generata dal prompt originale. Per **"La governante"**, il modello ha inserito autonomamente un nome proprio in copertina come se fosse l'autrice del libro (informazione non presente né corretta nel prompt): l'immagine è stata scartata e il prompt corretto esplicitando titolo e nome dell'autrice, correzione poi applicata anche ai prompt successivi per prevenire lo stesso errore. Per **"Un animale selvaggio"**, la prima generazione non rispettava elementi espliciti del prompt ed è stata richiesta una rigenerazione. Nessuna selezione estetica tra alternative equivalenti è stata effettuata in nessun caso: le rigenerazioni sono avvenute solo per correggere errori oggettivi rispetto al prompt, non per scegliere il risultato esteticamente migliore.

  **Nota sul volume delle generazioni (limite dichiarato):** una sola immagine "valida" per titolo (6 in totale) è un volume che consente un confronto qualitativo, esemplificativo e commentato caso per caso — non è un campione sufficiente per affermazioni statistiche generalizzabili sul comportamento di Gemini nella generazione di copertine. Un'osservazione statisticamente fondata avrebbe richiesto più generazioni per prompt (per controllare la variabilità stocastica del modello) e un campione più ampio di titoli — non svolta in questo progetto per limiti di tempo. Le osservazioni riportate nella sezione "Risultati principali" su questo punto vanno quindi lette come ipotesi interpretative supportate da esempi commentati, non come risultati quantitativi.

## Risultati principali

**RQ1 — Ipotesi parzialmente respinta.** Su 45 titoli, **42 copertine sono identiche tra cartaceo ed ebook (93%)**, 2 titoli sono privi di edizione ebook, **1 sola copertina è effettivamente diversa** (variazione minore di impaginazione, non un redesign). L'ipotesi di un adattamento sistematico verso soluzioni più semplici per la resa in miniatura non trova sostegno: nel 93% dei casi non c'è alcun processo di adattamento, perché non c'è alcuna modifica. L'unico caso di divergenza osservato va, nella direzione del cambiamento, nel senso ipotizzato (titolo più leggibile) — un indizio che la pratica esiste ma è residuale, non sistemica. Anche l'ipotesi di una divergenza maggiore nel genere più codificato visivamente (giallo/thriller) è respinta: nessuna differenza sostanziale tra generi (91% identiche in narrativa, 96% in giallo/thriller). Il riuso identico dell'asset grafico è la norma quasi assoluta, trasversale ai generi osservati. Evidenza a sostegno: confronto visivo diretto su tutto il corpus, non su un sottocampione.

**RQ2 — Ipotesi confermata.** Le sinossi di narrativa contemporanea sono in media il 28% più lunghe di quelle di giallo/thriller (204 vs 160 parole). Il lessico è nettamente differenziato: narrativa orientata a relazioni ed esistenza (*vita, donna, famiglia, madre, amore*); giallo/thriller orientato a mistero e tensione temporale (*tempo, passato, scomparsa, indagine*). Evidenza a sostegno: conteggio di frequenza su 24 sinossi, con esclusione di stopword e nomi propri.

**RQ3 — Ipotesi parzialmente respinta.** Su 6 casi analizzati in profondità, emerge un pattern ricorrente: gli editori "letterari"/upmarket tendono a scelte di **astrazione o sottrazione simbolica**, mentre Gemini, guidato da un prompt letterale, tende a **illustrare esplicitamente** tutti gli elementi menzionati nel testo. La vicinanza concettuale ipotizzata si verifica solo parzialmente (convergenza su ambientazione e oggetti principali in quasi tutti i casi), ma non sul registro visivo complessivo. Il divario osservato riflette soprattutto l'assenza, nel modello generativo, di conoscenza delle convenzioni di *packaging* editoriale (house style, codici di genere, tropi visivi come la "donna senza volto"), non una cattiva comprensione del testo. Evidenza a sostegno: confronto qualitativo commentato caso per caso (vedi nota sul volume di generazioni più sopra).

## Limiti dichiarati

- Corpus non randomizzato: selezione per rilevanza/notorietà, non campionamento statistico casuale.
- Raccolta dati manuale (vedi sopra): meno riproducibile in automatico, ma dataset fisso e tracciato.
- L'euristica di esclusione dei nomi propri in RQ2 è approssimativa: può generare falsi positivi/negativi (es. parole a inizio di frase interna non riconosciute correttamente).
- Il confronto AI vs copertina reale dipende da una catena con più passaggi soggettivi (sinossi → estrazione moodboard → prompt → immagine), ciascuno dei quali introduce un potenziale bias interpretativo di chi ha costruito il prompt.
- Osservazione preliminare, non sistematica, su titoli fantasy (es. *La corte di rosa e spine*, dove la copertina dell'edizione ebook ha anticipato di alcuni anni quella della successiva edizione tascabile) suggerisce che generi con edizioni fisiche curate esteticamente (tagli decorati, edizioni speciali) potrebbero mostrare tassi di divergenza più alti rispetto a quanto osservato qui — ipotesi da verificare in un campione dedicato, non affrontata in questo progetto per limiti di tempo.

## Struttura della repository

```
├── README.md                          # questo file
├── dati/
│   ├── 01_corpus_45_titoli.csv        # corpus base con metadati editoriali
│   ├── 02_controllo_visivo_45_titoli.csv  # esiti RQ1 (identica/diversa/no ebook)
│   └── 03_sinossi_24_titoli.xlsx      # sinossi raccolte per RQ2
├── codice/
│   └── analisi_lessicale.py           # script Python per RQ2 (tokenizzazione,
│                                       # stopword, esclusione nomi propri, frequenze)
└── dashboard/
    ├── 01_dashboard_rq1_rq2.html      # dashboard interattiva RQ1/RQ2 (Plotly.js)
    ├── 02_moodboard_prompt.html       # moodboard + prompt visivi per 6 titoli
    └── 03_confronto_ai_vs_editore.html # slider di confronto AI vs copertina reale
```

Le tre pagine in `dashboard/` sono file HTML autonomi (aprire con doppio click, nessuna installazione richiesta) oppure visualizzabili online abilitando GitHub Pages su questa repository.
