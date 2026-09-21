"""
methods.py
~~~~~~~~~~~

inside of this file, I will store all useful methods that 
I will use in predictions.py file in order to predict the
data to find IoU.
"""

# import libraries 
from pathlib import Path

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