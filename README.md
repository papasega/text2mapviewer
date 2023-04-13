This is a vesy simple way to map your text data using [Altas from NOMIC](https://docs.nomic.ai/index.html) using the lib `click`. 

You have to create an account to get API_KEY NOMIC. 

<< Atlas enables you to:

Store, update and organize multi-million point datasets of unstructured text, images and embeddings.

Visually interact with your datasets from a web browser.

Run semantic search and vector operations over your datasets.

Use Atlas to:

    - Visualize, interact, collaborate and share large datasets of text and embeddings.
    
    - Collaboratively clean, tag and label your datasets
    
    - Build high-availability apps powered by semantic search
    
    - Understand and debug the latent space of your AI model trains  
 
 . >>


# How to use
### Installation

To install the necessary dependencies, run the following command:

```bash
python -m venv mymapenv 
source mymapenv/bin/activate
pip install --upgrade pip 
pip install text2mapviewer==0.2.0
```

## Supported Transformer Models from Hugging Face 

This project supports a variety of transformer models, including models from the Hugging Face Model Hub and sentence-transformers. Below are some examples:
    - Hugging Face Model: 'prajjwal1/bert-mini'
    - Hugging Face Model: 'Sahajtomar/french_semantic'  (french version for semantic search embedding) 
    - Sentence-Transformers Model: 'sentence-transformers/all-MiniLM-L6-v2' etc...

Please ensure that the model you choose is compatible with the project requirements and adjust the `--transformer_model_name` option accordingly.

## To map your text/csv  files

```bash
pip install -r requirements.txt
python main.py --transformer-model-name MODEL_NAME --cache_dir CACHE_DIR --batch-size BATCH_SIZE --file-path FILE_PATH
```
NOTE: for the CACHE_DIR : you can setup it like ==> 

```bash
export TRANSFORMERS_CACHE=/path_to_your/transformers_cache
```

Give a fidback. 
