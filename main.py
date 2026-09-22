"""
main.py
~~~~~~~

this file will  help me to run the whole project
using files inside of src folder, using the data
from data folder.
"""
from src.methods import Methods
import src.configs as get

method = Methods(get.weights_path, get.images_path, get.labels_path, get.predictions_images_path, get.predictions_labels_path, get.comparisons_path, get.statistics_path)

def run_main():

    data = {
        "id" : 0,
        "variables" : [1, 2, 3, 4]
    }

    method.write(data, get.predictions_labels_path, "3.txt")


if __name__ == "__main__":
    run_main()