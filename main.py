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

    # run the model
    print("I am model")
    my_model = YOLO(get.weights_path)

    print("I am running it")

    method.run_the_model(my_model)

    print("get labels and its data from dataset")
    # get labels and its data from dataset
    actual_images_labels = method.get_labels(get.images_path)
    actual_labels = method.get_labels(get.labels_path)
    actual_labels_data = method.read_txt(actual_labels, get.labels_path)

    print("get predicted data and its labels")
    # get predicted data and its labels
    predicted_labels = method.get_labels(get.predictions_labels_path)
    predicted_labels_data = method.read_txt(predicted_labels, get.predictions_labels_path)

    l = len(actual_labels)



    IOU = []
    ids = []
    print("IOU")

    for i in range(l):
        iou_value = method.iou(actual_labels_data[i], predicted_labels_data[i])
        IOU.append(iou_value)
        ids.append(actual_labels_data[i]["id"])

        # it is time to predict bbox
        method.draw_rectangle(
            actual_labels_data[i],
            predicted_labels_data[i],
            actual_images_labels[i],
            get.comparisons_path,
            get.images_path,
            iou_value
        )

    print("make csv")
    method.make_csv(IOU, ids, actual_labels, get.statistics_path)

    print("done ")

    


if __name__ == "__main__":
    run_main()