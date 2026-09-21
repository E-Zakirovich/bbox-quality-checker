"""
methods.py
~~~~~~~~~~~

inside of this file, I will store all useful methods that 
I will use in predictions.py file in order to predict the
data to find IoU.
"""

# import libraries 
from pathlib import Path
import os

class Methods:

    def __init__(self, 
                 weights_path: str, 
                 images_path : str, 
                 labels_path : str, 
                 predictions_images_path : str, 
                 predictions_labels_path : str,
                 comparisons_path : str,
                 statistics_path : str

                 ):
        # path settings
        self.weights_path = weights_path
        self.images_path = images_path
        self.labels_path = labels_path
        self.predictions_images_path = predictions_images_path
        self.predictions_labels_path = predictions_labels_path
        self.comparisons_path = comparisons_path
        self.statistics_path = statistics_path

    # this method will help me to get the information from inside of txt files
    def read_txt(self, file_names):
        # store the data to somewhere
        data = []

        # following loop will get the name of each file from file names
        for filename in file_names:

            # I need a dictionary in order to store the data of each file
            file_data = {}

            full_file_path = os.path.join(self.labels_path, filename)

            # it is time to read files inside of file path
            with open(full_file_path, "r", encoding = "utf-8") as file:

                # I need to read only one line of data (there is only one line of data tbh)
                information = file.read()

                # i made a list according to space from information string
                array_version_of_information = information.split()

                # it is time to separate variables from array_version_of_information list
                id = array_version_of_information[0]

                # i am storing variables as dictionary
                file_data["id"] = id
                file_data["filename"] = filename
                file_data["variables"] = array_version_of_information[1:]
                
            # append the dictionary to data
            data.append(file_data)

        # return the result
        return data

    # following method will help me to get labels 
    def get_labels(self, path):
        labels = []

        for filename in os.listdir(path):
            labels.append(filename)

        return labels