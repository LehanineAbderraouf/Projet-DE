from sklearn.metrics import normalized_mutual_info_score, adjusted_rand_score
from sklearn.cluster import KMeans, AgglomerativeClustering
import numpy as np
from sklearn_extra.cluster import KMedoids

def clust_kmeans(mat, k):
    '''
    Perform clustering with kmeans

    Input:
    -----
        mat : input matrix 
        k : number of clusters
    Output:
    ------
        pred : list of predicted labels
    '''
    kmeans = KMeans(n_clusters=k, random_state=42)
    pred = kmeans.fit_predict(mat)
    
    return pred

def clust_ac(mat, k):
    '''
    Perform clustering with Agglomerative Clustering

    Input:
    -----
        mat : input matrix 
        k : number of clusters
    Output:
    ------
        pred : list of predicted labels
    '''
    ac = AgglomerativeClustering(n_clusters=k, linkage='ward')
    pred = ac.fit_predict(mat)
    
    return pred

def clust_kmedoids(mat, k):
    '''
    Perform clustering with kmedoids

    Input:
    -----
        mat : input matrix
        k : number of clusters
    Output:
    ------
        pred : list of predicted labels
    '''
    kmedoids = KMedoids(n_clusters=k, random_state=42)
    pred = kmedoids.fit_predict(mat)
    
    return pred

def eval_clust(pred, labels):
    nmi_score = normalized_mutual_info_score(labels, pred)
    ari_score = adjusted_rand_score(labels, pred)
    return nmi_score, ari_score

if __name__== "__main__":
    test_matrix_clust = np.random.rand(10, 2)
    test_labels = np.random.randint(3, size=10)

    cluster_predictions = clust_ac(test_matrix_clust, 3)
    nmi_score, ari_score = eval_clust(cluster_predictions, test_labels)

    print("Cluster predictions:", cluster_predictions)
    print(f'NMI: {nmi_score:.2f} \nARI: {ari_score:.2f}')
