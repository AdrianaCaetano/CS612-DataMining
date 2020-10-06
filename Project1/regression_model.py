from sklearn import linear_model
from sklearn import svm
from sklearn import neural_network

class RegressionModel:
   # ----------------------------------------------------------------------------------------------
   def __init__(self, model):
      if (model == 0):
         self.regressor = linear_model.LinearRegression()
         self.instructions = {'dim_limit': 4, 'algorithm': 'None', 'MLM_type': 'MLR'}
      
      elif (model == 1):
         self.regressor = svm.SVR()
         self.instructions = {'dim_limit': 4, 'algorithm': 'None', 'MLM_type': 'SVR'}
      
      elif (model == 2):
         self.regressor = neural_network.MLPRegressor(hidden_layer_sizes=(1000), max_iter=1000)
         self.instructions = {'dim_limit': 4, 'algorithm': 'None', 'MLM_type': 'ANN'}
      
      else:
         print("Invalid model option")

