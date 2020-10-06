from numpy import zeros

import fitting_scoring
import process_input
import regression_model

class DrugDiscovery:
    input_processor = process_input.ProcessInput()  # Instantiate an object of the new InputProcessor class
   
   # Path to data
    descriptors_file = "Practice_Descriptors.csv"
    targets_file = "Practice_Targets.csv"
   
   # ------------------------------------------------------------------------------------------------
    def discover(self):
       self.import_data()
       self.clean_data()
       self.sort_data()
       self.split_data()
       self.demonstration_model()
       self.test_model()
       
   
   # ------------------------------------------------------------------------------------------------
    # Step 1
    def import_data(self):
       self.descriptors = self.input_processor.open_file_to_matrix(self.descriptors_file)
       self.targets = self.input_processor.open_file_to_matrix(self.targets_file)
       #print("Data imported. Descriptors: ", self.descriptors.shape, ", Targets: ", self.targets.shape)
   
   # ------------------------------------------------------------------------------------------------
    # Step 2
    def clean_data(self):
      # Filter out molecules with NaN-value descriptors and descriptors with little or no variance
       self.descriptors, self.targets = self.input_processor.removeInvalidData(self.descriptors, self.targets)
       self.descriptors, self.active_descriptors = self.input_processor.removeNearConstantColumns(self.descriptors)
      
       # Rescale the descriptor data
       self.descriptors = self.input_processor.rescale_data(self.descriptors)
      
       print("Clean Data. Descriptors: ", self.descriptors.shape, ", Targets: ", self.targets.shape)
       print("Rescaled data:\n", self.descriptors)

     # ------------------------------------------------------------------------------------------------
    # Step 3
    def sort_data(self):
       self.descriptors, self.targets = self.input_processor.sort_descriptor_matrix(self.descriptors, self.targets)
       #print("Sort Data")

    # -----------------------------------------------------------------------------------------------
    # Step 4
    def split_data(self):
       self.X_Train, self.X_Valid, self.X_Test, self.Y_Train, self.Y_Valid, self.Y_Test = \
          self.input_processor.simple_split(self.descriptors, self.targets)
       self.data = {'TrainX': self.X_Train, 'TrainY': self.Y_Train,
                    'ValidateX': self.X_Valid, 'ValidateY': self.Y_Valid,
                    'TestX': self.X_Test, 'TestY': self.Y_Test,
                    'UsedDesc': self.active_descriptors}
      
       print(str(self.descriptors.shape[1]) + " valid descriptors and " + str(
              self.targets.__len__()) + " molecules available.")
      
       # print(X_Train[0:5, 0:20])

    # ------------------------------------------------------------------------------------------------
    # Step 5
    def demonstration_model(self):
       # Set up the demonstration model
       self.featured_descriptors = [4, 8, 12,16]  # These indices are "false", applying only to the truncated post-filter descriptor matrix.
       self.binary_model = zeros((1, self.X_Train.shape[1]))
       self.binary_model[0][self.featured_descriptors] = 1
       #print("Demonstration model created")
    
   # ------------------------------------------------------------------------------------------------
    # Step 6
    def test_model(self):
       #print("Create a regression object to fit our demonstration model to the data")
       for i in range(3):
          model_obj = regression_model.RegressionModel(i)
      
          self.trackDesc, self.trackFitness, self.trackModel, \
          self.trackDimen, self.trackR2train, self.trackR2valid, \
          self.trackR2test, self.testRMSE, self.testMAE, \
          self.testAccPred = fitting_scoring.ScoreFitting().evaluate_population(
             model=model_obj.regressor, instructions=model_obj.instructions, data=self.data,
             population=self.binary_model, exportfile=None)
      
          self.print_results()  # print results for each iteration
   # ------------------------------------------------------------------------------------------------
    # Step 7
    def print_results(self):
       print("****************************************")
       for key in self.trackDesc.keys():
          print("Descriptors:")
          print("\t" + str(self.trackDesc[key]))  # Show the "true" indices of the featured descriptors in the full matrix
          print("Fitness:")
          print("\t" + str(self.trackFitness[key]))
          print("Model:")
          print("\t" + str(self.trackModel[key]))
          print("Dimensionality:")
          print("\t" + str(self.trackDimen[key]))
          print("R2_Train:")
          print("\t" + str(self.trackR2train[key]))
          print("R2_Valid:")
          print("\t" + str(self.trackR2valid[key]))
          print("R2_Test:")
          print("\t" + str(self.trackR2test[key]))
          print("Testing RMSE:")
          print("\t" + str(self.testRMSE[key]))
          print("Testing MAE:")
          print("\t" + str(self.testMAE[key]))
          print("Acceptable Predictions From Testing Set:")
          print("\t" + str(100 * self.testAccPred[key]) + "% of predictions")
    
   # ------------------------------------------------------------------------------------------------
    def step8(self):
       pass
