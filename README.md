# Divisione del Testo con Langchain
## <i> Facciamo un po' di chiarezza sulla divisione dei testi per i processi di NLP con Langchain. </i>

Nel mondo dell'elaborazione del linguaggio naturale (NLP), gli strumenti per la trasformazione dei documenti e la suddivisione dei testi sono diventati essenziali, 
grazie soprattutto alla nascita di sistemi per l'elaborazione di documenti basati su IA conosciuti come "Retrieval Augmented Generation" o RAG.

I sistemi basati su RAG hanno in qualche modo rivoluzionato il modo in cui addestriamo i modelli linguistici di grandi dimensioni (LLM), consentendo loro di accedere a dati esterni dopo l'addestramento iniziale. 
Per questo motivo è diventata indispensabile una veloce ed efficace divisione delle informazioni.

In questo articolo, cercheremo di approfondire i trasformatori di documenti (Document transformers) e i divisori di testo (Text Splitter) inclusi nel framework #langchain.

## Divisori di testo
I text splitter (divisori di testo) sono strumenti che dividono il testo in frammenti più piccoli con un significato semantico, spesso corrispondente ad una frase. 
Facciamo bene attenzione però, perchè non si tratta solo di dividere il testo, ma anche di combinare questi frammenti in modo strategico. 
La divisione del testo segue questi passaggi:

1. Divisione il testo in piccoli frammenti con significato semantico, come ad esempio le frasi.
2. Combinare questi piccoli frammenti in un frammento più grande fino a raggiungere una certa dimensione (solitamente misurata da una funzione).
3. Una volta raggiunta tale dimensione, il frammento diventa una vera e propria unità di testo.

Quindi il processo viene ripetuto e inizia la creazione di un nuovo frammento di testo, con una certa sovrapposizione rispetto al precedente per cercare di mantenere un contesto coerente tra i frammenti e ridurre al minimo la perdita di informazioni.
