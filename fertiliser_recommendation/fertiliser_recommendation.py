import joblib
 

knn_from_joblib = joblib.load('xg_boost_fertiliser_recomondation.pkl')
 



def recondation_fertiliser_fn(listed):

					features_list=listed

					print(features_list)

					import numpy as np


					int_features2 = np.array(features_list)

					int_features1 = int_features2.reshape(1, -1)


					tested1=knn_from_joblib.predict(int_features1)



					print(tested1)

					return(tested1)




