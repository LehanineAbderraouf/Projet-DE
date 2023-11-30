import sys
from sklearn.datasets import fetch_20newsgroups
from sentence_transformers import SentenceTransformer

from Dimensionality_Reduction_Functions.dimred_umap import dimred_umap
from Dimensionality_Reduction_Functions.dimred_acp import dimred_acp
from Dimensionality_Reduction_Functions.dimred_afc import dimred_afc
from Clustering_Methods.clust import clust_kmeans, clust_ac, clust_kmedoids, eval_clust

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <function_name>")
        sys.exit(1)

    function_name = sys.argv[1].lower()
    algorithm_name = sys.argv[2].lower()

    # import data
    ng20 = fetch_20newsgroups(subset='test')
    corpus = ng20.data[:2000]
    labels = ng20.target[:2000]
    k = len(set(labels))

    # embedding
    # Load the model from the saved directory
    model = SentenceTransformer('model_directory')
    embeddings = model.encode(corpus)

    #reduce dimension to 20
    if function_name == "umap":
        emb_red = dimred_umap(embeddings, 20)
    elif function_name == "acp":
        emb_red = dimred_acp(embeddings, 20)
    elif function_name == "afc":
        emb_red = dimred_afc(embeddings, 20)
    else:
        print("Invalid function name. Choose 'umap', 'acp', or 'afc'.")

    #apply clustering kmeans algorithm
    if algorithm_name == "kmeans":
        cluster_predictions = clust_kmeans(emb_red, k)
    elif algorithm_name == "ac":
        cluster_predictions = clust_ac(emb_red, k)
    elif algorithm_name == "kmedoids":
        cluster_predictions = clust_kmedoids(emb_red, k)
    else:
        print("Invalid algorithm name. Choose 'kmeans', 'ac', or 'kmedoids'.")

    nmi_score, ari_score = eval_clust(cluster_predictions, labels)


    #evaluate the model
    print("Cluster predictions:", cluster_predictions)
    print(f'NMI: {nmi_score:.2f} \nARI: {ari_score:.2f}')

if __name__ == "__main__":
    main()
