"""
methods.py
~~~~~~~~~~~

inside of this file, I will store all useful methods that 
I will use in predictions.py file in order to predict the
data to find IoU.
"""

# import libraries 
import os
from ultralytics import YOLO

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

    # following method will help me to get labels 
    def get_labels(self, path):
        labels = []

        for filename in os.listdir(path):
            labels.append(filename)

        return labels

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

    # following method can get a data as a list and will make create new file and store it as txt 
    def write(self, bbox : dict, path : str, filename : str):

        # I better get ful path in order to avoid bugs related to folders
        full_path = os.path.join(path, filename)

        # open the folder 
        with open(full_path, "w", encoding = "utf-8") as file:
            # get variables 
            id = bbox["id"]
            variables = bbox["variables"]
            variables = [str(i) for i in variables]

            # string format of variables 
            string_format_of_variable = " ".join(variables)

            # store the file
            file.write(f"{id} {string_format_of_variable}")

    # predictor method
    def run_the_model(self, model : YOLO):

        # i am going to get list of file names
        image_names = self.get_labels(self.images_path)

        # reach each file and predict it with the model
        for file in image_names:

            # get to full path with os library in order to avoid bugs related to paths
            full_img_path = os.path.join(self.images_path, file)

            # run the model
            results = model.predict(
                source = full_img_path,
                conf = 0.25,
                verbose = False
            )

            if len(results) == 0:
                print(f"Skipping {file} — no results (possibly corrupted image)")
                continue

            # get single output
            result = results[0]

            for box in result.boxes:
                # get the variables 
                id = int(box.cls[0].item())
                xc, yc, w, h = box.xywhn[0].tolist()

                # it is time to make dictionary
                bbox = {
                    "id" : str(id),
                    "variables" : [xc, yc, w, h]
                }

                # get the labels name
                filename = os.path.splitext(file)[0] + ".txt"

                # write the data to predictions folder 
                self.write(bbox, self.predictions_labels_path, filename)

    # calculate intersection over union
    def iou(self, groundtruth : dict, predictions : dict):

        # first get the cordinates of intersection
        xA = max(groundtruth["variables"][0], predictions["variables"][0])
        yA = max(groundtruth["variables"][1], predictions["variables"][1])
        xB = min(groundtruth["variables"][2], predictions["variables"][2])
        yB = min(groundtruth["variables"][3], predictions["variables"][3])

        # get the size
        x_intersection = max(0, xB - xA)
        y_intersection = max(0, yB - yA)
        intersection_area = x_intersection * y_intersection

        # get the area of bboxes 
        area_of_a = (groundtruth["variables"][2] - groundtruth["variables"][0]) * (groundtruth["variables"][3] - groundtruth["variables"][1])      
        area_of_b = (predictions["variables"][2] - predictions["variables"][0]) * (predictions["variables"][3] - predictions["variables"][1]) 

        # calculate intersection over union
        intersection_over_union = intersection_area / (area_of_a + area_of_b - intersection_area)    

        # return the result
        return intersection_over_union 