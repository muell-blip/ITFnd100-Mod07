# --------------------------------------------------#
# Title: Demonstration of Pickling and Error Handling
# Description:  Storing data in a binary format and example of simple error handling
# ChangeLog: (Who, When, What)
# KMueller, 11/23/2019, Created Script
# --------------------------------------------------#

import pickle  #imports code from another code file

# Data --------------------------------
strFileName = 'AppData.dat'  # .dat extension is binary format
lstCustomer = []

# Processing -------------------------------------
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "ab")
    pickle.dump(list_of_data, file) #store the data using the pickle.dump method
    file.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file) #read the data using the pickle.load method
    file.close()
    return list_of_data

# Presentation -----------------------------------------
while True:  # anticipate that the user may try to enter a string value versus an integer
    try:  # exception handling
        intID = int(input("Enter an ID: "))
        intID = int(intID)
        break  # Loop breaks only if a valid integer is given
    except TypeError:
        print("Not an integer!  Please try again...") # otherwise stay in the loop until an integer value is entered

strName = str(input("Enter a Name: ")) # get Name from user
lstCustomer = [intID, strName] # store the entries into a list object
print(lstCustomer) #print entry back to the user

save_data_to_file(strFileName, lstCustomer)  #call the save file function declared previously
print(read_data_from_file(strFileName))  # call the read file function declared previously