"""
main.py
~~~~~~~

this file will  help me to run the whole project
using files inside of src folder, using the data
from data folder.
"""
from src.methods import Methods
import src.configs as get
from ultralytics import YOLO

method = Methods(get.weights_path, get.images_path, get.labels_path, get.predictions_images_path, get.predictions_labels_path, get.comparisons_path, get.statistics_path)

def run_main():

    data = {
        "id" : 0,
        "variables" : [1, 2, 3, 4]
    }

    model = YOLO(get.weights_path)

    method.run_the_model(model)


if __name__ == "__main__":
    run_main()