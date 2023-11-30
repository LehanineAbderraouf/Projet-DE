from sklearn.metrics import normalized_mutual_info_score, adjusted_rand_score
from sklearn.cluster import KMeans
import numpy as np

def clust_kmeans(mat, k):
    '''
    Perform clustering with kmeans

    Input:
    -----
        mat : input list 
        k : number of clusters
    Output:
    ------
        pred : list of predicted labels
    '''
    kmeans = KMeans(n_clusters=k, random_state=42)
    pred = kmeans.fit_predict(mat)
    
    return pred

def eval_clust(pred, labels):
    nmi_score = normalized_mutual_info_score(labels, pred)
    ari_score = adjusted_rand_score(labels, pred)
    return nmi_score, ari_score

if _name_ == "_main_":
    test_matrix_clust = np.random.rand(10, 2)
    test_labels = np.random.randint(3, size=10)

    cluster_predictions = clust_kmeans(test_matrix_clust, 3)
    nmi_score, ari_score = evaluate_clusters(cluster_predictions, test_labels)

    print("Cluster predictions:", cluster_predictions)
    print(f'NMI: {nmi_score:.2f} \nARI: {ari_score:.2f}')
