# from ultralytics import YOLO

# def main():
#     # Load a model
#     model = YOLO('yolov8n.pt')  # load an official model
#     model = YOLO('E:\\Documents\\yolo\\pcos\\runs\\detect\\train14\\weights\\best.pt')  # load a custom model

#     # Validate the model
#     metrics = model.val()  # no arguments needed, dataset and settings remembered
#     metrics.box.map    # map50-95
#     metrics.box.map50  # map50
#     metrics.box.map75  # map75
#     metrics.box.maps   # a list contains map50-95 of each category

# if __name__ == '__main__':
#     main()

from ultralytics import YOLO
import matplotlib.pyplot as plt

def main():
    # Load a model
    model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO('E:\\Documents\\yolo\\pcos\\runs\\detect\\train14\\weights\\best.pt')  # load a custom model

    # Validate the model
    metrics = model.val()  # no arguments needed, dataset and settings remembered

    # Plot the mAP values
    categories = metrics.names
    map_values = metrics.box.maps

    plt.figure()
    # plt.bar(categories, map_values)
    # plt.bar(categories, map_values.astype(float))
    plt.bar(categories, list(map_values))
    plt.xlabel('Categories')
    plt.ylabel('mAP')
    plt.title('mAP per Category')
    plt.xticks(rotation=90)
    plt.show()

if __name__ == '__main__':
    main()