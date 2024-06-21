import joblib
 

knn_from_joblib = joblib.load('xg_boost_india.pkl')
 



def recondation_fn(temperature, humidity, rainfall):

					features_list=[float(temperature), float(humidity), float(rainfall)]

					print(features_list)

					import numpy as np


					int_features2 = np.array(features_list)

					int_features1 = int_features2.reshape(1, -1)


					tested1=knn_from_joblib.predict(int_features1)



					print(tested1)

					return(tested1)




