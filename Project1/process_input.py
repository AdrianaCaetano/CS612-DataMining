import numpy as np
from numpy import *
import csv
import pandas as pd

class ProcessInput:
# ------------------------------------------------------------------------------------------------
    def rescale_data(self, descriptor_matrix):
        # You have already written code for this.
        mean = descriptor_matrix.flatten().mean()
        std_dev = descriptor_matrix.flatten().std()
        #print("Mean: ", mean, ", Std_deviation: ", std_dev)
        
        return (descriptor_matrix - mean)/ std_dev

# ------------------------------------------------------------------------------------------------
# What do we need to sort the data?

    def sort_descriptor_matrix(self, descriptors, targets):
        # Placing descriptors and targets in ascending order of target (IC50) value.
        alldata = ndarray((descriptors.shape[0], descriptors.shape[1] + 1))
        alldata[:, 0] = targets
        alldata[:, 1:alldata.shape[1]] = descriptors
        alldata = alldata[alldata[:, 0].argsort()]
        descriptors = alldata[:, 1:alldata.shape[1]]
        targets = alldata[:, 0]

        return descriptors, targets

# ------------------------------------------------------------------------------------------------

# Performs a simple split of the data into training, validation, and testing sets.
# So how does it relate to the Data Mining Prediction?

    def simple_split(self, descriptors, targets):

        testX_indices = [i for i in range(descriptors.shape[0]) if i % 4 == 0]
        validX_indices = [i for i in range(descriptors.shape[0]) if i % 4 == 1]
        trainX_indices = [i for i in range(descriptors.shape[0]) if i % 4 >= 2]

        TrainX = descriptors[trainX_indices, :]
        ValidX = descriptors[validX_indices, :]
        TestX = descriptors[testX_indices, :]

        TrainY = targets[trainX_indices]
        ValidY = targets[validX_indices]
        TestY = targets[testX_indices]

        return TrainX, ValidX, TestX, TrainY, ValidY, TestY

# ------------------------------------------------------------------------------------------------

# try to optimize this code if possible
 # OPTIMIZED based on possible forms of text file as csv
    def open_descriptor_matrix (self, fileName):
        with open(fileName, mode='r') as csvfile:
            all_rows = [row.strip().replace(",", " ").replace(";", " ") for row in csvfile if row != '']
            all_entries = list(map(str.split, all_rows))

            dataArray = array(all_entries, order='C')

        if (min(dataArray.shape) == 1):  # flatten arrays of one row or column
            return dataArray.flatten(order='C')
        else:
            return dataArray

    # ************************************************************************************
    # Try to optimize this code if possible

    def open_target_values (self, fileName):
        with open(fileName, mode='r') as csvfile:
            all_rows = [row.strip().replace(",", " ").replace(";", " ") for row in csvfile if row != '']
            datalist = list(map(str.split, all_rows))

        for i in range(len(datalist)):
            try:
                datalist[i] = float(i)
            except:
                datalist[i] = datalist[i]
        return array(datalist)


    def open_file_to_matrix(self, filename):
        if(filename):
            dataArray = np.loadtxt(filename, delimiter=',')
            return dataArray
        else:
            print("Error loading data from file.")
            return np.zeros((2, 1))
       

#**********************************************************************************************
# Removes constant and near-constant descriptors.
# But I think also does that too for real data.
# So for now take this as it is

    def removeNearConstantColumns(self, data_matrix, num_unique=10):
        total_columns = data_matrix.shape[1]
        useful_descriptors = [col for col in range(data_matrix.shape[1])
                                if len(set(data_matrix[:, col])) > num_unique]
        filtered_matrix = data_matrix[:, useful_descriptors]

        remaining_desc = zeros(data_matrix.shape[1])
        remaining_desc[useful_descriptors] = 1
        
        deleted_columns = total_columns - filtered_matrix.shape[1]
        print("Near constant columns deleted: ", deleted_columns)
        
        return filtered_matrix, where(remaining_desc == 1)[0]

# ------------------------------------------------------------------------------------------------
# part 1: Removes all rows with junk (ex: NaN, etc). Note that the corresponding IC50 value should be deleted too
# Part 2: Remove columns with 20 junks or more. Otherwise the junk should be replaced with zero
# Part 3: remove all columns that have zero in every cell

    def removeInvalidData(self, descriptors, targets):
        total_rows = descriptors.shape[0]
        total_columns = descriptors.shape[1]
        
        # Combine all data into one matrix
        alldata = ndarray((descriptors.shape[0], descriptors.shape[1] + 1))
        alldata[:, 0] = list(targets)
        alldata[:, 1:alldata.shape[1]] = descriptors
    
        # Remove all rows with more than 20 junks
        alldata = pd.DataFrame(alldata)
        alldata = (alldata.apply(pd.to_numeric, errors='coerce'))  # Change "junk values" into NaN
        # alldata = alldata.loc[alldata.isna().sum() < 20, :]   # Clean rows
        # alldata = alldata.dropna(axis=0, thresh=20) # Drop rows with 20+ nan/junk
    
        # Separate all data into descriptors and targets
        descriptors = alldata.loc[:, 1:alldata.shape[1]]
        targets = (alldata.loc[:, 0]).to_numpy()
    
        # Remove columns with 20 junks or more. Replace junk with zero.
        columns_junk_replaced = (descriptors.loc[:, descriptors.isna().sum() < 20]).shape[1]
        print("Total columns with junk replaced by zero: ", columns_junk_replaced)
        
        descriptors = descriptors.loc[:, descriptors.isna().sum() < 20]
        descriptors = descriptors.fillna(0)     # Change nan to zero
        descriptors = descriptors.to_numpy()

        removed_columns = total_columns - descriptors.shape[1]
        removed_rows = total_rows - descriptors.shape[0]
        print("Invalid data deleted: ", removed_rows, " rows, and ", removed_columns, " columns")
    
        return descriptors, targets
#------------------------------------------------------------------------------------------------