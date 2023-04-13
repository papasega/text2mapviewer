import click
import numpy as np
from nomic import atlas

@click.command()
@click.option('--num_embeddings', default=10000, help='Number of embeddings')
@click.option('--embedding_dim', default=256, help='Dimension of embeddings')
def map_embeddings(num_embeddings, embedding_dim):
    """Maps randomly generated embeddings onto a 2D map using Atlas"""
    embeddings = np.random.rand(num_embeddings, embedding_dim)
    project = atlas.map_embeddings(embeddings=embeddings)
    print(project)


if __name__ == '__main__':
    map_embeddings()
