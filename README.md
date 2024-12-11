# Face-Recognition

##  Project Overview
Python-based face recognition program that uses OpenCV to detect faces in an image. It utilizes the Haar Cascade Classifier, a machine learning model trained for face detection. The program loads an image, detects any faces in it, and then highlights the faces by drawing rectangles around them.

## Dataset Used
- <a href="https://github.com/Aajtakk/Face-Recognition---Python">Dataset</a>

## Face-Recognition-Output Screenshot
![Face-Recognition_Output](https://github.com/user-attachments/assets/ca4b3596-0512-4cac-bd66-68dcb151e55f)

## Features
1. Loads an image from a specified path.
2. Converts the image to grayscale for optimal face detection.
3. Detects faces using a pre-trained Haar Cascade model.
4. Draws rectangles around detected faces to highlight them.
5. Displays the processed image with face detections.

## Technologies Used
1. Programming Language: Python 3.x
2. Library: OpenCV

## Usage
1. Make sure you have an image that contains faces, and place it in your working directory or provide the correct path to the image file in the code.
2. Update the image = cv2.imread("D:\\Python\\Programs\\Face.png") line to point to the image file you want to process.
3. Run the Python script:
4. The program will display the image with rectangles drawn around any detected faces.
