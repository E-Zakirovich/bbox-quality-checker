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

    ground_truth = {
        "variables" : [50, 50, 150, 150]
    }

    prediction = {
        "variables" : [70, 80, 170, 180]
    }

    a = method.iou(ground_truth, prediction)

    print(a)


if __name__ == "__main__":
    run_main()