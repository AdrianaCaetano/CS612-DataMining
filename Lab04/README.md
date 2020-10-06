## Extract data from the Binding Database
-	Go to the virtual machine in the cougarapps (cougarapps.csusm.edu) 
-	Go to the binding database https://www.bindingdb.org/bind/index.jsp
-	Search for  “gamma”
-	Select “gamma seratose”
-	Add all the pages and make a .sdf and .tsv data file as shown in the video
-	Go to .tsv data file and delete all columns except the IC50 column
-	Place the Targets (Ys) and the descriptors (Xs) in the same file (Y should go on the first column)
-	Call the file myGamma.xlxs and email the file to yourself and start working in your own machine

## Write a program in python that does the following:
1. Any molecule with no name should be deleted
2. Any molecule with no IC50 value should be deleted
3. Except the column that is the name, any row that includes non-digit should be deleted.
4. get rid of the columns that are all zeros 
5. Except the IC50 column, rescale the other values in the file and place the results in another file called “RescaledFile.xlxs”

## Your program should print the following:
-	total number of molecules (rows) with no name that are deleted
-	total number of molecules with no IC50 that are deleted
-	total number of molecules with junk data that are deleted
-	Total number of descriptors (columns) that sum to zero 
-	A file that is called “RescaledFile.xlxs” that includes all the data that are re rescaled.

