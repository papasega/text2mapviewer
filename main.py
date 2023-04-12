# -- Papa Séga WADE 13/04/2023 --
import click
import torch as th 
from typing import List, Dict
from fondamental.bases import * # or import --> load_documents, encode_documents, map_embeddings_to_atlas

@click.command()
@click.option('--transformer-model-name' , required=True, type=str, help='The name of the transformer model to load.')
@click.option('--cache_dir', envvar = 'TRANSFORMERS_CACHE', type=str, help='The directory to cache the transformer model in.')
@click.option('--batch-size', default=10, type=int, help='The batch size to use when encoding documents.')
@click.option('--file-path', default='dataset.csv', type=str, help='The path to the CSV file containing the documents.')
@click.pass_context
def main(ctx:click.core.Context, transformer_model_name: str, cache_dir: str, batch_size: int, file_path: str) -> None:
    device = th.device('cuda:0' if th.cuda.is_available() else 'cpu')
    ctx.obj = ctx.obj or {}
    ctx.obj['device'] = device
    documents = load_documents(file_path)
    ctx.obj['cache-dir'] = cache_dir
    embeddings = encode_documents(documents, transformer_model_name, cache_dir, batch_size)
    response = map_embeddings_to_atlas(embeddings, documents)
    print(response)

if __name__ == '__main__':
    main()

"""   To run the model :==> 
    python main.py --transformer-model-name MODEL_NAME --cache_dir CACHE_DIR --batch-size BATCH_SIZE --file-path FILE_PATH
    python main.py --transformer-model-name prajjwal1/bert-mini --cache_dir TRANSFORMERS_CACHE --batch-size 5 --file-path /path_to_file/dataset.csv

    models from hugginface
        -  model bert-mini : ==> prajjwal1/bert-mini
        -  model sentence_transformer ==> sentence-transformers/all-MiniLM-L6-v2
        -  model  BERT_Base  ==> distilbert-base-uncased
        - export TRANSFORMERS_CACHE=/home/pswia/miniconda3/envs/pswia/lib/python3.10/site-packages/transformers

"""
