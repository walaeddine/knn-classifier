### Image Classification with K-Nearest Neighbors
This project demonstrates a simple image classification pipeline using the K-Nearest Neighbors (k-NN) algorithm. The script trains a k-NN classifier on raw pixel intensities from a dataset of images and then evaluates its performance.

Features
Simple Image Preprocessing: Resizes images to a standard size for consistent input.

Raw Pixel Intensities: Uses the flattened pixel values of images as features.

K-NN Classification: Trains and evaluates a k-NN model.

Performance Metrics: Outputs a detailed classification report, including precision, recall, and F1-score.

Getting Started
Prerequisites
You'll need Python 3 and the following libraries to run the script. You can install them using pip:

pip install scikit-learn numpy opencv-python

Project Structure
Make sure your project is structured like this:

.
├── knn.py
└── pipeline/
    ├── datasets/
    │   └── simpledatasetloader.py
    └── preprocessing/
        └── simplepreprocessor.py
    └── utils/
        └── simpleimageutils.py

Dataset
The script expects your images to be organized into a folder structure where each subdirectory represents a class. For example:
```
dataset/
├── cats/
│   ├── cat_01.jpg
│   └── cat_02.jpg
└── dogs/
    ├── dog_01.jpg
    └── dog_02.jpg

```

How to Run the Script
To run the k-NN classifier, use the following command in your terminal. You must specify the path to your dataset using the --dataset argument.

python knn.py --dataset path/to/your/dataset

Command-line Arguments
--dataset (required): The path to the root directory of your image dataset.

--neighbors (optional): The number of nearest neighbors for the k-NN classifier. The default is 1.

--jobs (optional): The number of CPU cores to use for calculating distances. Use -1 to utilize all available cores. The default is -1.

Example Output
When you run the script, you'll see information about the data loading process, memory usage, and finally, a detailed classification report like the one below.

[INFO] loading images...
[INFO] processed 500/3000
[INFO] processed 1000/3000
[INFO] processed 1500/3000
[INFO] processed 2000/3000
[INFO] processed 2500/3000
[INFO] processed 3000/3000
[INFO] features matrix: 9.0MB
[INFO] evaluating k-NN classifier...
              precision    recall  f1-score   support

        cats       0.40      0.56      0.46       249
        dogs       0.41      0.47      0.43       262
       panda       0.80      0.32      0.46       239

    accuracy                           0.45       750
   macro avg       0.53      0.45      0.45       750
weighted avg       0.53      0.45      0.45       750

License
This project is open-source and available under the MIT License.