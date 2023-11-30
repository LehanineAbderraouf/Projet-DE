import pandas as pd
import prince
import numpy as np

def dimred_afc(x, n_components):
  '''
	Perform dimensionality reduction with the AFC function

	Input:
	-----
	    x : NxM list (numpy array)
	    n_components : number of dimensions to keep 
	Output:
	------
	    red_mat : NxP list such that p<<m
  '''
  # check if there exists negative values in the data
  has_negative_values = np.any(x < 0)

  if has_negative_values:
    print("The rix contains negative values, applying shift")
    # Shift data to make it non-negative
    min_value = np.min(x)
    shifted_data = x - min_value + 1e-10
    df = pd.DataFrame(shifted_data)
  else:
    df = pd.DataFrame(x)

  ca = prince.CA(n_components=n_components)
  ca = ca.fit(df)
  return ca.row_coordinates(df)