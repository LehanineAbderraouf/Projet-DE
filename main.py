import sys
from sklearn.datasets import fetch_20newsgroups
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

from dimred_umap import dimred_umap
from dimred_acp import dimred_acp
from dimred_afc import dimred_afc
from clust import clust_kmeans, evaluate_clusters

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <function_name>")
        sys.exit(1)

    function_name = sys.argv[1].lower()

    # import data
    ng20 = fetch_20newsgroups(subset='test')
    corpus = ng20.data[:2000]
    labels = ng20.target[:2000]
    k = len(set(labels))

    # embedding
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(corpus)

    #reduce dimension to 20
    if function_name == "umap":
        emb_red = umap_function(embeddings, 20)
    elif function_name == "acp":
        emb_red = acp_function(embeddings, 20)
    elif function_name == "afc":
        emb_red = afc_function(embeddings, 20)
    else:
        print("Invalid function name. Choose 'umap', 'acp', or 'afc'.")

    #apply clustering kmeans algorithm
    cluster_predictions = clust_kmeans(test_matrix_clust, k)
    nmi_score, ari_score = evaluate_clusters(cluster_predictions, test_labels)


    #evaluate the model
    print("Cluster predictions:", cluster_predictions)
    print(f'NMI: {nmi_score:.2f} \nARI: {ari_score:.2f}')

if __name__ == "__main__":
    main()
