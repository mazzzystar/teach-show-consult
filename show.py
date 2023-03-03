import os
import glob
import pickle
import API_KEY
from langchain.vectorstores.faiss import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ["OPENAI_API_KEY"] = API_KEY.OPENAI_API_KEY

source_file_lst = glob.glob("source_data/alda/examples/*")

all_codes = ""
f_alda = open("source_data/alda_all_in_one.txt", 'w')
for alda_file in source_file_lst:
    lines = open(alda_file, 'r').readlines()
    clean_lines = []
    for line in lines:
        if line.strip().startswith('#'): continue
        clean_lines.append(line.strip()+"\n")
    f_alda.write(str(clean_lines)+"\n\n")
f_alda.close()

# Load
loader = UnstructuredFileLoader("source_data/alda_all_in_one.txt")
raw_documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)

# Load Data to vectorstore
embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(documents, embeddings)

# Save vectorstore
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)