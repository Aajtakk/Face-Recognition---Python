# Face Recognition

import cv2

# Load the image
image =cv2.imread("D:\\Pammi\\Python\\Programs\\Face.png")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Verify if the image was loaded
if image is None:
    print("Error: Could not load image. Check the file path and integrity.")
else:
# Convert the image to greyscale
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect the faces in image
faces = face_cascade.detectMultiScale(gray,1.3, 5)

# Draw a rectangle around faces
for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    
# Display the image with detected faces
cv2.imshow("Faces Found", image)
cv2.waitKey(0)
cv2.destroyAllWindows