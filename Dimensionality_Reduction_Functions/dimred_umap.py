from umap import UMAP
import numpy as np

def dimred_umap(x, n_components):
    ''' 
    Perform dimensionality reduction using UMAP

    Input:
    -----
        x : NxM list 
        n_components : number of dimensions to keep 
    Output:
    ------
        red_mat : NxP list such that p<<m
    '''
    umap_model = UMAP(n_components=n_components)
    red_mat = umap_model.fit_transform(x)
    
    return red_mat

if __name__== "__main__": #for test
    test_matrix = np.random.rand(10, 10)
    reduced_test_matrix = dimred_umap(test_matrix, 4)
    print("Original matrix shape:", test_matrix.shape)
    print("Reduced matrix shape:", reduced_test_matrix.shape)
