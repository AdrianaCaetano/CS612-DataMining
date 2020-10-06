"""
    CS 612 Data Mining
    Lab 04
    @author: Adriana Caetano and Farnaz Tajadod
    Created on 09/27/2020
    Program Description: Read dataset from excel file, clean it, and rescale it.
"""

import numpy as np
import pandas as pd

class CleanData:
 
    #	Any molecule with no value in NAME or IC50 should be deleted. Count # deleted rows.
    def delete_missing_on_column(self, data_frame: pd.DataFrame):
        column = input("Which column do you want to clean? ")
        data_frame[column].str.strip() # Delete whitespaces on this column
        
        # Count missing values on column
        count_missing = str(sum(pd.isnull(data_frame[column])))
        print("Total number of molecules (rows) with missing values on ", column, " deleted: ", count_missing)
        
        # Drop missing values from column
        data_frame.dropna(how='any', subset= [column], inplace= True)
        
        print("Dataset new shape: ", data_frame.shape)
        return data_frame

    # Except the column that is the name, any row that includes non-digit should be deleted. Count # deleted rows.
    def delete_nan_except(self, data_frame: pd.DataFrame):
        column = input("Which column could have non-digit values as an exception? ")
        acceptable = int(input("How many junks are acceptable per column?"))
        
        # Drop chosen column
        df = data_frame.drop(columns=column)
        
        columns_count = df.shape[1]
        
        df = (df.apply(pd.to_numeric, errors='coerce')) # Change "junk values" into NaN
        df = df.loc[:, df.isna().sum() < acceptable] # Keep columns with less than 200 junks
        df = df.fillna(0) #Change all NaN to zero
        
        total_columns = columns_count - df.shape[1]
        print("Total number of molecules (rows) with junk data deleted: " , str(total_columns))
        print("Dataset new shape: ", df.shape)
        return df

    # Get rid of the columns that are all zeros. Count # deleted columns
    def delete_all_zero_columns(self, data_frame: pd.DataFrame):
        df = data_frame.loc[:, (data_frame != 0).any(axis=0)]
        
        # Count total number of descriptor (columns) that has sum zero
        total_columns = data_frame.shape[1]
        zero_col_count = total_columns - df.shape[1]
        print("Total number of descriptors (columns) that sum to zero: ", str(zero_col_count))
        
        print("Dataset new shape: ", df.shape)
        return df

    # Using helper functions above, clean data
    def clean(self, data_frame: pd.DataFrame):
        print("Any row with missing data should be deleted.")
        df = data_frame
        num_columns = int(input("How many columns do you want to clean? "))
        print("Original dataset shape: ", df.shape)
        
        for x in range(num_columns):
            df = CleanData().delete_missing_on_column(df)
        
        df = CleanData().delete_nan_except(df)
        df = CleanData().delete_all_zero_columns(df)
        return df
    
    # Except the IC50 column, rescale the other values in the file
    def rescale(self, data_frame: pd.DataFrame):
        # Separate target to perform calculations
        Ys = data_frame.iloc[:, 0]
        Ys = Ys.to_frame()
        Xs = data_frame.drop(data_frame.columns[0], axis=1)
        
        print("Target Ys shape: ", Ys.shape)
        print("Xs shape: ", Xs.shape)
        
        # Find mean, and stdDev of the population. Do not include column Y
        mean = Xs.stack().mean()
        std_dev = Xs.stack().std()
       
        # Rescale
        rescaled_data = Ys.join((Xs - mean) / std_dev)
        print("Rescaled data shape: ", rescaled_data.shape)
       
        return rescaled_data
       
    def normalize(self, data_frame: pd.DataFrame):
        # Separate target to perform calculations
        Ys = data_frame.iloc[:, 0]
        Ys = Ys.to_frame()
        Xs = data_frame.drop(data_frame.columns[0], axis=1)
        
        # Find min, and max of the population. Do not include column Y
        min = Xs.stack().min()
        max = Xs.stack().max()
       
        # Normalize
        normalized_data = Ys.join((Xs - min) / max - min)
        print("Normalized data shape: ", normalized_data.shape)
       
        return normalized_data

# ----------------------------------------------------------------------

def main():
    print("To run this program use the following values: ")
    print("- File name: myGammaS.xlsx")
    print("- Number of columns to clean: 2")
    print("- First column to clean: NAME")
    print("- Second column to clean: IC50")
    print("- Column with non-digit values: NAME")
    print("- Acceptable number of junks: 200")
    print()
    
    # Define file
    file = input("Excel file with the original dataset: ")

    # Read dataset from excel to dataframe
    print("Reading data from file...")
    rawData = pd.read_excel(file)
    print("Data imported from file.")
    print()
    
    # Clean junks
    print("Cleaning data...")
    data = rawData.copy()  #copy to preserve original
    data = CleanData().clean(data)
    print("Data is clean.")
    print()
    
    #Rescale Clean Data
    rescaled_data = CleanData().rescale(data)
    print("Data is rescaled.")
    
    # Normalize Clean Data
    normalized_data = CleanData().normalize(data)
    print("Data is normalized.")
    
    print()

    # Place the results in a file called “RescaledFile.xlxs”
    # Save output to excel file, each matrix in a different tab
    print("Saving to file...")
    with pd.ExcelWriter("Lab04-RescaledFile.xlsx") as writer:
        #data.to_excel(writer, sheet_name="Clean_Data", index=False)
        rescaled_data.to_excel(writer, sheet_name="Rescaled_Data", index=False)
        #normalized_data.to_excel(writer, sheet_name="Normalized_Data", index=False)
    print("Done!")
    
    return

if __name__ == "__main__":
    main()