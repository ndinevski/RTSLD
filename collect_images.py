import cv2
import os
import sys
import time
import uuid

PATH_IMAGES = 'Tensorflow/workspace/images/collected_images'

labels = ['hello', 'yes', 'no', 'thankyou', 'iloveyou', 'sorry', 'please', 'help']
num_images = 10

# Switch labels[index] where index is in range(labels) to write images
# for different classes. (ex. labels[0] is for capturing 'hello')
cap = cv2.VideoCapture(0)
label = labels[0]
print('Collecting images for ' + label)
time.sleep(5)
for n in range(num_images):
    ret, frame = cap.read()
    image_name = os.path.join(PATH_IMAGES, label, label + ".{}.jpg".format(str(uuid.uuid1())))
    cv2.imwrite(image_name, frame)
    cv2.imshow(label + str(n), frame)
    time.sleep(3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
