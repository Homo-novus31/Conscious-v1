import numpy as np
from sentence_transformers import SentenceTransformer
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
embedding_model = SentenceTransformer(MODEL_NAME)

QUERY="""
AI  safety, alignment risk's, emergent capabilities, scaling behaviours, interoperability, governance, long-term technological impact"""

query_emb= embedding_model. encode (QUERY, normalize_embeddings= True)

def similarity (text:str)->float:
    emb = embedding_model. encode (text, normalize_embeddings=True )
    return  float(np.dot (emb,query_emb))