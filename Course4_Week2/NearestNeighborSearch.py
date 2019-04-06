import pandas as pd
import matplotlib.pyplot as plt          # plotting
import numpy as np                       # dense matrices
from scipy.sparse import csr_matrix      # sparse matrices

wiki = pd.read_csv("people_wiki.csv")


def load_sparse_csr(filename):
    loader = np.load(filename)
    data = loader['data']
    indices = loader['indices']
    indptr = loader['indptr']
    shape = loader['shape']

    return csr_matrix((data, indices, indptr), shape)

word_count = load_sparse_csr('people_wiki_word_count.npz')
word_count = np.asarray(word_count)
word_count = pd.DataFrame(word_count, index = )




