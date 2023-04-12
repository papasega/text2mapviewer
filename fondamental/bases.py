from transformers import AutoTokenizer, AutoModel
import numpy as np
import torch
import csv
from typing import List, Dict,  Any, Optional, Tuple
from nomic import atlas

def load_documents(file_path: str) -> List[Dict[str, str]]:
    documents = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            documents.append({                ## Change with your own variable ## 
                'filename': row['filename'],  
                'text': row['finalText'],
                'label': row['label'],
                'number_word': row['num_words']

            })
    return documents

def encode_documents(documents: List[Dict[str, str]], transformer_model_name: str, cache_dir: str, batch_size: int) -> np.ndarray:
    model = AutoModel.from_pretrained(transformer_model_name, cache_dir=cache_dir)
    tokenizer = AutoTokenizer.from_pretrained(transformer_model_name, cache_dir=cache_dir)
    embeddings = []

    with torch.no_grad():
        for i in range(0, len(documents), batch_size):
            batch = [document['text'] for document in documents[i:i+batch_size]]
            encoded_input = tokenizer(batch, return_tensors='pt', padding=True)
            cls_embeddings = model(**encoded_input)['last_hidden_state'][:, 0]
            embeddings.append(cls_embeddings)

    embeddings = torch.cat(embeddings).numpy()
    return embeddings

def map_embeddings_to_atlas(embeddings: np.ndarray, documents: List[Dict[str, str]]) -> str:
    response = atlas.map_embeddings(embeddings=embeddings, 
                                    data=documents,
                                    id_field='filename',
                                    colorable_fields=['label'],
                                    name="Name_Projet",
                                    description="Name_Project data map with Nomic Atlas.")
    return response
