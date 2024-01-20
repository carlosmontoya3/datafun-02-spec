''' This module provides functions for creating a series of project folders. '''

import math
import statistics
import pathlib
import os
import time
import Montoya_utils

#Create folders based on range of years. Starting to ending year.
def create_folders_for_range(start_year, end_year):
    for year in range(start_year, end_year + 1):
       pathlib.Path(str(year)).mkdir(exist_ok=True)

#Create folders from list of names
def create_folders_from_list(folder_names, to_lowercase=False, remove_spaces=False):
    for folder in folder_names:
        folder_check = folder
        if to_lowercase and remove_spaces:
            folder_check = folder.replace(' ', '') # Removes spaces from string
            folder_check = folder.lower() # Converts string to lowercase
        pathlib.Path(folder_check).mkdir(exist_ok=True)

#Creat prefixes folders
def create_prefixed_folders(folder_names, prefix):
    for i in folder_names:
        folder_names = str(prefix)+str(i)
        pathlib.Path(folder_names).mkdir(exist_ok=True)
        print(f"Folder {folder_names}")

#Create folders periodically
def create_folders_periodically(duration):
   num_folders = 3 # number of folders to be created 
   next_file = 1   #Int to start while loop
   while next_file <= num_folders:
       pathlib.Path("folder-" + str(next_file)).mkdir(exist_ok=True)
       next_file += 1
       time.sleep(duration)


def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {Montoya_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
    
if __name__ == '__main__':
    main()