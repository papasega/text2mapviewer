## -- Papa Séga WADE 13/04/2023 --
from nomic import atlas
import numpy as np

num_embeddings = 10000
embeddings = np.random.rand(num_embeddings, 256)

project = atlas.map_embeddings(embeddings=embeddings)
