from tkinter.filedialog import askdirectory
from tkinter import Tk
import os, hashlib  #OS Module selects, deletes, or gets the list of a file.
from pathlib import Path   #How to get the absolute path for the file name from a folder. 


Tk().withdraw()  #Hides any additional windows displayed.
path = askdirectory(title="Select a folder.")
#print(path)

#How to get the list of a file inside a folder.
file_list = os.listdir(path)
#print(file_list)  #Displays the files in the list.


#Make a dictionary called unique.
unique = dict()

#To work with the list, we need to look over the list.

for file in file_list:
    #print(file) #If you want to see the file name.
    file_name = Path(os.path.join(path, file))   #Gets the absolute path for the file name from a folder. 
    #print(file_name) #Prints the absolute path.

    #Check whether the file we're getting is really a file or not.
    if file_name.is_file():
        fileHash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()
    
        #In short, from the hashlib library, we're taking the md5 function.
        #md5 is a tool for creating a hash from a string.
        #Inside that function, we're opening a file; i.e the file_name & then reading the file.
        #We're reading the file as rb i.e read binary.
        #read() - read function is for reading the file.
        #hexdigest() - returns the encoded data in hexadecimal format.

        if fileHash not in unique: #Assign the file_name inside the unique dictionary.
            unique[fileHash] = file_name #FileHash is the key, & file_name is the value.
        else:
            os.remove(file_name) #Else: delete the file.
            print(f"Successfully deleted {file_name}")
    else:
        print("Operation not successful.")

#Deletes the original file and leaves the copy.