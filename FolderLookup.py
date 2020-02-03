""" 
FolderLookup  03FEB2020
@author: tyson.kasper

This script will take a search term from the user and scan both possible
directories for folders. Any folder name that includes the search
term will be opened, up to a maximum fo 5 as overload protection.

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNE
"""

import os

os.system("mode con cols=110 lines=45")  

#Set paths to folders to search,
dir_path = os.path.realpath('folder path')

# To add another directory worth of folders, create a new path and copy the below code.
# Then add the directory code for the dcd if-loop in the while loop. 
dirpaths = ['path',
            'path',
            'path',
            'path']

# Put all folders contained within dir_path to a list of folder names.
# Each element of list a tuple (folder name, folder path)



print('''
      Enter the code for the folders you want to search, and then enter a search term. 
      A maximum of *5* folders containing the search term within the folder name will
      be opened. 
      
      If you want to open more folders contained within the given directories
      start your search term with an asterisk (e.g. *05-03). The asterisk search is
      limited to a maximum of 20 folders, to protect against opening an entire directory.
      
      NOTE: Entered text is case-sensitive.
      
      Directory codes:
          1.    'path'
          2.    'path'
          3.    'path'
      
      Enter 'done' or hit enter to close.\n''')

while True:
    dcd = input("Directory code:\t")   
   
    if dcd.lower() == 'done' or dcd == '':
        break
    
    lstpaths = []
    
    # Change list of directories to add to list depending on user given code.
    if dcd == '1':
        lstpaths = dirpaths[:3]
    if dcd == '2':
        lstpaths = dirpaths[3:5]
    if dcd == '3':
        lstpaths = [dirpaths[-1]]
        
    print('\nDirectories being searched:\n')
    
    for L in lstpaths:
        print(L)
        
    lstfolders = []
    # Put all folders contained within dir_path to a list of folder names.
    # Each element of list a tuple (folder name, folder path)
    for path in lstpaths: 
        dir_path = os.path.realpath(path)
        with os.scandir(dir_path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_dir():
                    lstfolders.append((entry.name,entry.path))  
    
    sch = input("\nSearch term:\t\t")
    
    if sch.lower() == 'done' or sch == '':
        break    
    
    mod = 0
    if sch[0] == '*':
        mod = 1
        sch = sch[1:]

    i = 0
    for tup in lstfolders:
        if sch in tup[0]:
            os.startfile(tup[1])
            i +=1
            if mod == 0 and i > 4:
                break
            if mod == 1 and i > 15:
                break
    
    if i == 0:
        print('\n*****************\nFOLDER NOT FOUND\n*****************')
    if i > 0:
        print('\n*****************\nFOLDER(S) OPENED\n*****************')
