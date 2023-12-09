import os
import cv2

# Path to the folder containing the images
folder_path = "C:\\Users\\taher\\Downloads\\archive\\data\\train\\notinfected"

# Iterate over all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Get the image dimensions
        print(os.path.splitext(filename)[0])
        height, width, _ = image.shape

        # Get the bounding box information (replace this with your own logic)
        class_name = 0
        # x = width // 2
        # y = height // 2
        # bbox_width = width // 4
        # bbox_height = height // 4
        x = 0.5
        y = 0.5
        bbox_width = 1
        bbox_height = 1

        # Create the annotation string
        annotation = f"{class_name} {x} {y} {bbox_width} {bbox_height}"

        # Create the annotation file with the same name as the image
        annotation_filename = os.path.splitext(filename)[0] + ".txt"
        # annotation_path = os.path.join(folder_path, annotation_filename)
        # annotation_path = os.path.join(os.path.join(folder_path, "labels"), annotation_filename)
        # Create the annotation file path in the "labels" folder
        labels_folder = os.path.join(folder_path, "labels")
        os.makedirs(labels_folder, exist_ok=True)  # Create the "labels" folder if it doesn't exist
        annotation_path = os.path.join(labels_folder, annotation_filename)
        with open(annotation_path, "w") as f:
            f.write(annotation)

        print(f"Generated annotation file: {annotation_filename}")

print("Annotation generation complete.")