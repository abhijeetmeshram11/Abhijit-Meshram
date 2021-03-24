# Abhijit-Meshram
This Project is Basically detect Brain Tumor by reading a MRI scan Image of Brain 
# Brain-Tumor-Detector
Building a detection model using a convolutional neural network in Tensorflow & Keras.<br>
Used a brain MRI images data founded on Kaggle. You can find it [here](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection).<br>

**About the data:**<br>
The dataset contains main Data folder in which it has 2 sub-folders: yes and no which contains 2318 Brain MRI Images. The folder yes contains 1240 Brain MRI Images that are tumorous and the folder no contains 1078 Brain MRI Images that are non-tumorous.

## Getting Started

1240 positive and 1078 negative examples, resulting in 253 example images.


## Data Preprocessing

For every image, the following preprocessing steps were applied:

1. Crop the part of the image that contains only the brain (which is the most important part of the image).
2. Resize the image to have a shape of (240, 240, 3)=(image_width, image_height, number of channels): because images in the dataset come in different sizes. So, all images should have the same shape to feed it as an input to the neural network.
3. Apply normalization: to scale pixel values to the range 0-1.

## Data Split:

The data was split in the following way:
1. 70% of the data for training.
2. 30% of the data for testing.

# Neural Network Architecture

This is the architecture that I've built:

![Neural Network Architecture](convnet_architecture.jpg)

**Understanding the architecture:**<br>
Each input x (image) has a shape of (240, 240, 3) and is fed into the neural network. And, it goes through the following layers:<br>

1. A Zero Padding layer with a pool size of (2, 2).
2. A convolutional layer with 32 filters, with a filter size of (7, 7) and a stride equal to 1.
3. A batch normalization layer to normalize pixel values to speed up computation.
4. A ReLU activation layer.
5. A Max Pooling layer with f=4 and s=4.
6. A Max Pooling layer with f=4 and s=4, same as before.
7. A flatten layer in order to flatten the 3-dimensional matrix into a one-dimensional vector.
8. A Dense (output unit) fully connected layer with one neuron with a sigmoid activation (since this is a binary classification task).

**Why this architecture?**<br>

Firstly, I applied transfer learning using a ResNet50 and vgg-16, but these models were too complex to the data size and were overfitting. Of course, you may get good results applying transfer learning with these models using data augmentation. But, I'm using training on a computer with 6th generation Intel i7 CPU and 8 GB memory. So, I had to take into consideration computational complexity and memory limitations.<br>

So why not try a simpler architecture and train it from scratch. And it worked :)

# Training the model

The model was trained for 10 epochs.


# Results

To Test model I have careated a GUI file ,and here You have to Run GUI and select any MRI scanned Image,
and get your result "Yes" or "No"

# Final Notes

What's in the files?

1. The code in the Python Files.
2. The weights for all the models. The best model is named as 'Brain_tumor_model.h5'.
3. The models are stored as *.model* files. They can be restored as follows:
4. The dataset contains main Data folder in which it has 2 sub-folders: yes and no which contains 2318 Brain MRI Images.


Contributes are welcome!
<br>Thank you!
