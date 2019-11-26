# Pickling and Structured Error Handling in Python #

This website will describe Pickling in Python, and include an example of Structured Error Handling.  Pickling is the technique of saving data in a binary format, which can obscure the file content and may reduce the file size.  Also known as flattening, serialization, or marshalling, using Pickle to read and write large amounts of data can be more efficient than reading and writing from or to plain text files.  Structured Error Handling guards against potential (user-induced) errors and allows the programmer to customize how the program handles errors, instead of letting Python display default error messages that might be confusing to the user. 

## Work Instructions ##

We will write a simple script to read and write data to binary format, and include some simple structured error handling.

First, import pickle and create a file called ‘AppData.dat’ and a list called lstCustomer.  Note that the file extension is .dat (binary).

import pickle

strFileName = 'AppData.dat'

lstCustomer = [ ]

Now we will create two new functions to save and read data to/from the binary file and utilize the .dump and .load functions within pickle.  The first function will save the string data and write to the file.  Note that .dump method is appended after pickle, and that “wb” (write binary) is used instead of “w”, as you would for a plain text file.

def save_data_to_file(file_name, list_of_data):

    file = open(file_name, "wb")
    pickle.dump(list_of_data, file)
    file.close()

The second function will read the data from the binary file.  Note that .load method is appended after pickle, and that “rb” (read binary) is used instead of “r”, as you would for a plain text file.

def read_data_from_file(file_name):

    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

Now that the functions are written, this is a good opportunity to add some Structured Error Handling.  A user ID should be only numbers, so anticipating that the user may attempt to add a string character instead of an integer as their user ID, construct a while loop with try/except to handle the error:

while True: 

    try:  
        intID = int(input("Enter an ID: "))
        intID = int(intID)
        break 
    except ValueError:
        print("Not an integer!  Please try again...")

If the user enters a string value, such as the letter 'd', a custom error will be produced as shown below:

Enter and ID: d

Not an integer! Please try again....

Enter an ID:

This is a more user-friendly error that simply prompts the user to enter an integer versus a string for the User ID.  It is a good alternative to the Python generated ValueError message which reads similar to as shown below:

Traceback (most recent call last):

File "C:/Users/................, line 27, in <module>
  
  intID = int(input("Enter an ID: "))
  
ValueError: invalid literal for int() with base 10: 'd'

Add more code to prompt the user to enter their name, store the entries into a list object, and print the entry back to the user:

strName = str(input("Enter a Name: ")) 

lstCustomer = [intID, strName]

print(lstCustomer) 

Lastly, add code to call the functions declared previously to save and read the data to/from the file as shown below:

save_data_to_file(strFileName, lstCustomer) 

print(read_data_from_file(strFileName))  

The code output when the script is ran should be similar to what is shown below depending on what the user enters:

Enter an ID: 362

Enter a Name: John Smith

[362, 'John Smith']

Note that data should also be present in the ‘AppData.dat’ file, although parts of it will be obscured and unreadable (to a human).

The following is the completed code:

 --------------------------------------------------
 Title: Demonstration of Pickling and Error Handling
 Description:  Storing data in a binary format and example of simple error handling
 ChangeLog: (Who, When, What)
 muell-blip, 11/23/2019, Created Script
 --------------------------------------------------

import pickle  #imports code from another code file

 Data --------------------------------
 
strFileName = 'AppData.dat'  # .dat extension is binary format

lstCustomer = []

 Processing -------------------------------------
 
def save_data_to_file(file_name, list_of_data):

    file = open(file_name, "ab")
    pickle.dump(list_of_data, file) #store the data using the pickle.dump method
    file.close()

def read_data_from_file(file_name):

    file = open(file_name, "rb")
    list_of_data = pickle.load(file) #read the data using the pickle.load method
    file.close()
    return list_of_data

 Presentation -----------------------------------------
 
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


The following links are helpful in completing this script:

https://www.python-course.eu/python3_exception_handling.php

The page is well organized and provides multiple examples of Exception Handling in Python.  It was especially helpful for me because it embedded the try/except block within a while loop, and the example therefore fit nicely into my already-existing code.

https://www.tutorialspoint.com/python/python_exceptions.htm

Provides a list of standard Exceptions in Python and a short description of in which cases each is raised, i.e., a “Value Error” is raised when “the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.”

https://docs.python.org/3.7/library/pickle.html

Comprehensive description of how pickle works and provides a list of functions (.dump, .load, etc.) to make the pickling process more convenient.

https://www.pitt.edu/~naraehan/python3/pickling.html

Short, well written example with a simple code example as well.


