# Traffic Sign Classifier

This project is a Convolutional Neural Network (CNN) implemented in TensorFlow/Keras to classify traffic sign images into 43 categories, based on the German Traffic Sign Recognition Benchmark (GTSRB) dataset.

## Features

- Loads and preprocesses traffic sign images.
- Trains a CNN to recognize 43 different traffic sign categories.
- Evaluates model accuracy on a test set.
- Optionally saves the trained model.

## Requirements

- Python 3.x
- TensorFlow
- NumPy
- OpenCV (`cv2`)
- scikit-learn

Install dependencies with:
```
pip install tensorflow numpy opencv-python scikit-learn
```

## Usage

1. **Prepare the dataset:**  
   Place the GTSRB dataset in a directory, structured as:
   ```
   data_directory/
     0/
       image1.ppm
       image2.ppm
       ...
     1/
       ...
     ...
     42/
   ```

2. **Train the model:**
   ```
   python traffic.py data_directory
   ```

3. **Train and save the model:**
   ```
   python traffic.py data_directory model.h5
   ```

## Files

- `traffic.py` — Main script for training and evaluating the model.

## Notes

- The model expects images to be 30x30 pixels.
- The script splits the data into training and testing sets (60%/40%).
- The output model (if saved) can be loaded later for predictions.

---