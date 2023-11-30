import pandas as pd
import prince

def dimred_acp(x, n_components):
	 '''
	Perform dimensionality reduction with the ACP function

	Input:
	-----
	    x : NxM list (numpy array)
	    n_components : number of dimensions to keep 
	Output:
	------
	    red_mat : NxP list such that p<<m
	'''
  df = pd.DataFrame(x)
  pca = prince.PCA(n_components=n_components)
  pca = pca.fit(df)
  return pca.transform(df)