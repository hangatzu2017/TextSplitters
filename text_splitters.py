import streamlit as st
import re
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter, Language
import tiktoken

# Tokenize (OpenAI)
# Questo codice usa la libreria di encoding tiktoken di OpenAI.
# Crea un oggetto di token encoding usando lo schema di codifica CL100K_BASE.
# Lo schema di codifica CL100K_BASE è usato per codificare i token con il dataset CL100K.
enc = tiktoken.get_encoding("cl100k_base")

# Riferimento: https://python.langchain.com/docs/modules/data_connection/document_transformers
splitters=[
  'Dividi codice',
  'Dividi per carattere',
  'Ricorsivamente dividi per carattere',
  'Dividi per tokens (OpenAI)'
]

# I linguaggi di programmazione supportati
languages=['CPP', 'GO', 'JAVA', 'JS', 'PHP', 'PROTO', 'PYTHON', 'RST', 'RUBY', 'RUST', 'SCALA', 'SWIFT', 'MARKDOWN', 'LATEX', 'HTML', 'SOL']

# I tipi di files supportati
files_types=[
  {
    "extension": "txt",
    "language": "MARKDOWN",
  },
  {
    "extension": "py",
    "language": "PYTHON",
  },
  {
    "extension": "php",
    "language": "PHP",
  },
  {
    "extension": "html",
    "language": "HTML",
  },
  {
    "extension": "js",
    "language": "JS",
  },
  {
    "extension": "css",
    "language": "CSS",
  },
  {
    "extension": "md",
    "language": "MARKDOWN",
  }
]

# Memorizza l'estensione del file nello stato della sessione
if 'file_extension' not in st.session_state:
  st.session_state['file_extension'] = ''

# Memorizza il file di linguaggio nello stato della sessione
if 'file_language' not in st.session_state:
  st.session_state['file_language'] = ''

# Memorizza il contenuto tokenizzato nello stato della sessione
if 'tokenized_content' not in st.session_state:
  st.session_state['tokenized_content'] = 0


def file_upload():
  if uploaded_file is not None:
    # Ottenere l'estensione del file e la salva nello stato di sessione
    st.session_state['file_extension'] = uploaded_file.name.split(".")[-1]
    # Trova il tipo di linguaggio
    for file in files_types:
      if file["extension"] == st.session_state['file_extension']:
        st.session_state['file_language'] = file["language"].lower()
        break

    return uploaded_file.getvalue().decode("utf-8")

# Crea Top KPI's
def metrics(chunks, tokens, characters):
  col1, col2, col3 = st.columns(3)
  col1.metric("Chunks", chunks)
  token_ratio=round(tokens/st.session_state['tokenized_content'], 2)
  col2.metric("Total Tokens", tokens, token_ratio, delta_color="inverse" if token_ratio!=1 else "off")
  col3.metric("Total Characters", characters)

# Crea tabella dataframe
def create_dataframe(text_splitter, file_content):
  chunks=text_splitter.create_documents([file_content])
  st.session_state['tokenized_content']=len(enc.encode(file_content))
  df = pd.DataFrame(
    {
      "Testo": [chunk.page_content for chunk in chunks],
      "Tokens": [len(enc.encode(chunk.page_content)) for chunk in chunks],
      "Caratteri": [len(chunk.page_content) for chunk in chunks],
    }
  )
  metrics(len(df), df['Tokens'].sum(), df['Caratteri'].sum())
  if len(df) < 1:
    st.error('No content found.')
  else:
    st.dataframe(df, use_container_width=True)


#
#
# MAIN
st.set_page_config(
  page_title="Text Splitters",
  page_icon="✂️",
  layout="wide",
  initial_sidebar_state="expanded",
  menu_items={
      'Get help': 'https://github.com/hangatzu2017/text_splitter/pulls',
      'Report a bug': "https://github.com/hangatzu2017/text_splitter/issues",
      'About': "Creato da Hangatzu 2017."
  }
)
st.title("✂️ Text Splitters ✂️")
st.markdown("""#### Utilizzo dei text splitter di [@langchain](https://python.langchain.com/docs/modules/data_connection/document_transformers/) per dividere (chunk) codice e/o file di testo.""")
st.divider()


# SIDEBAR
uploaded_file=st.sidebar.file_uploader(
  "Trascina qui un file o fai click per caricarne uno.",
  type=[file["extension"] for file in files_types],
  accept_multiple_files=False
)

file_content=file_upload()

if uploaded_file is not None:
  splitter=st.sidebar.selectbox(
    'Seleziona uno Splitter',
    splitters,
    # Se l'estensione del file è txt
    index=1 if st.session_state['file_extension']=="txt" else 0
  )
  splitter_index=splitters.index(splitter)
  if splitter_index==0:
    language_selector=st.sidebar.selectbox('Seleziona un Linguaggio', languages, index=languages.index(st.session_state['file_language'].upper()))
  if splitter_index==1:
    text_splitter_separator=st.sidebar.text_input('Separatore', value="\n\n", help="Inserisci il/i carattere/i da cercare per dividere il testo come impostazione predefinita.", placeholder="Inserisci un separatore come ad es. \\n\\n", max_chars=10, key="text_splitter_separator", type="default")
  st.sidebar.divider()
  chunk_size=st.sidebar.slider('Dimensione Chunk', 1, 5000, 1000)
  chunk_overlap=st.sidebar.slider('Sovrapposizione', 0, chunk_size, 0)

  # Codice
  if splitter_index==0:
    code_splitter = RecursiveCharacterTextSplitter.from_language(
      language=Language[language_selector],
      chunk_size=chunk_size,
      chunk_overlap=chunk_overlap
    )
    chunks=code_splitter.create_documents([file_content])
    st.session_state['tokenized_content']=len(enc.encode(file_content))
    df = pd.DataFrame(
      {
        "Testo": [chunk.page_content for chunk in chunks],
        "Tokens": [len(enc.encode(chunk.page_content)) for chunk in chunks],
        "Caratteri": [len(chunk.page_content) for chunk in chunks],
      }
    )
    metrics(len(df), df['Tokens'].sum(), df['Caratteri'].sum())
    st.dataframe(df, use_container_width=True)


  # Se è character splitter
  if splitter_index==1:
    # converti tutti i simili a: \\n\\n oppure \\r \\t in:  \n\n oppure \t
    text_splitter_separator=re.sub(r'\\', '', text_splitter_separator)
    text_splitter=CharacterTextSplitter(
      separator=text_splitter_separator,
      chunk_size=chunk_size,
      chunk_overlap=chunk_overlap,
      length_function=len, 
      is_separator_regex=False
    )
    create_dataframe(text_splitter, file_content)

  # Se è ricorsivo
  if splitter_index==2:
    text_splitter=RecursiveCharacterTextSplitter(
      chunk_size=chunk_size,
      chunk_overlap=chunk_overlap,
      length_function=len,
      is_separator_regex=False
    )
    create_dataframe(text_splitter, file_content)

  # Se usiamo il token splitter
  if splitter_index==3:
    text_splitter=CharacterTextSplitter.from_tiktoken_encoder(
      chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    create_dataframe(text_splitter, file_content)

  with st.expander(f"Guarda il file Originale {uploaded_file.name} – {st.session_state['file_language']}"):
    st.code(file_content, language=f"{st.session_state['file_language']}", line_numbers=True)


st.sidebar.markdown("Hangatzu2017 [https://github.com/hangatzu2017].")
