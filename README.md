# Splitting del Testo con Langchain
### *Facciamo un po' di chiarezza sulla divisione dei testi per i processi di NLP.*

Nel campo dell'elaborazione del linguaggio naturale (NLP), gli strumenti per la trasformazione dei documenti e la suddivisione dei testi sono diventati essenziali grazie all'introduzione dei sistemi di intelligenza artificiale chiamati "Retrieval Augmented Generation" (RAG). 

Questi sistemi hanno rivoluzionato il modo in cui addestriamo i modelli linguistici di grandi dimensioni (LLM), consentendo loro di accedere a informazioni esterne dopo l'addestramento iniziale. Purtroppo però gli LLM hanno una capacità di contestualizzazione (memoria) a tutt'oggi limitata. Di conseguenza, è diventato estremamente importante avere metodi veloci ed efficaci per dividere i testi in parti più gestibili. 
In questo esercizio, spiegheremo come funzionano i diversi tipi di strumenti per la divisione del testo (Text Splitter) presenti nel framework [langchain](https://www.langchain.com/), fornendo a corredo un esempio di codice per una comprensione pratica.

## I Divisori di testo

I Text Splitter, ovvero i divisori di testo, sono strumenti che suddividono il testo in frammenti più piccoli che hanno un significato semantico, di solito corrispondente a una frase. È importante sottolineare che la divisione del testo non riguarda solo la separazione dei frammenti, ma anche la loro combinazione strategica.

Il processo di divisione del testo segue i seguenti passaggi:

1. Inizialmente, il testo viene suddiviso in frammenti più piccoli con un significato semantico, come le frasi.

2. Successivamente, questi frammenti vengono combinati per formare frammenti più grandi fino a raggiungere una determinata dimensione, che di solito viene misurata utilizzando una funzione specifica.

3. Una volta raggiunta tale dimensione, il frammento diventa un'unità di testo completa.

Questo processo viene quindi ripetuto per creare nuovi frammenti di testo, con una certa sovrapposizione rispetto al frammento precedente, al fine di mantenere un contesto coerente tra i frammenti e ridurre al minimo la perdita di informazioni.

Ciò significa che i Text Splitter offrono un alto grado di personalizzazione in due aspetti fondamentali:

- Modalità di divisione del testo: È possibile definire regole specifiche per la suddivisione basate su caratteri, parole o token.

- Misurazione della dimensione del frammento: È possibile regolare le dimensioni dei frammenti in base alle esigenze specifiche del contesto.

### Tipi di separatori di testo in Langchain

***RecursiveCharacterTextSplitter:***
Il RecursiveCharacterTextSplitter è uno strumento che suddivide il testo in frammenti basati sui caratteri, partendo dal primo carattere. Nel caso in cui i frammenti risultino troppo grandi, passa al carattere successivo per ottenere frammenti più piccoli. Questo approccio offre una grande flessibilità, poiché consente di definire i caratteri di divisione e regolare la dimensione dei frammenti in base alle specifiche esigenze.

***CharacterTextSplitter:*** 
Simile a RecursiveCharacterTextSplitter, ma con la possibilità di definire un separatore personalizzato per una divisione più specifica. Per impostazione predefinita, tenta di dividere in base a caratteri come "\n", "\n", " " e "".

***RecursiveTextSplitter:***
A differenza del RecursiveCharacterTextSplitter, il RecursiveTextSplitter suddivide il testo in frammenti basati su parole o token anziché su caratteri. Questo metodo fornisce una prospettiva più semantica ed è particolarmente adatto all'analisi del contenuto piuttosto che alla struttura del testo.

***TokenTextSplitter:***
Il TokenTextSplitter utilizza il modello linguistico OpenAI per dividere il testo in frammenti basati sui token. Questo approccio permette una segmentazione precisa e contestualizzata del testo, rendendolo ideale per applicazioni avanzate di elaborazione del linguaggio naturale.

In aggiunta a questo breve articolo introduttivo, che spero abbia fornito una panoramica chiara sull'argomento, è incluso il file text_splitters.py. Questo file fornisce un esempio pratico di come utilizzare i Text Splitter menzionati sopra. Text_splitter è un'applicazione Python che consente di suddividere e analizzare i file di testo utilizzando i diversi metodi descritti.

Per l'installazione dei pacchetti e l'avvio del progetto fate quanto segue:

create un ambiente virtuale Python:
```bash
python -m text_splitters_venv venv
```

attivate l'ambiente virtuale con: 
```bash
source text_splitters_venv/bin/activate
```

installate i pacchetti necessari nell'ambiente virtuale:
```bash
pip install -r requirements.txt
```

avviate il progetto con:
```bash
streamlit run text_splitters.py
```
