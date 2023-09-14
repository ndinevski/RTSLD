# RealTimeSignLanguageDetection
Real Time Sign Language Detection with Tensorflow Object Detection and Python and Deep Learning

Using Tensorflow Object Detection API, Python, pre-trained model SSD MobNet V2, created datasets (labeled with LabelImg).
Includes detection of 8 gestures : Yes, No, Hello, Help, Please, Sorry, I Love You, Thank you

Scripts and Description:

- path_names.py - Includes paths of whole directory for easier usage in code
- collect_images.py - Collects images from web-cam and creates data set, then you label images with labelImg, and divide them in
                      train and test set (83:17 ratio)
- label_map.py - Creates label map
- generate_tfrecord.py - Generates TF records (train.record and test.record)
- update_config_for_learning.py - Updates pre-trained pipeline config to our parameters
- load_model.py - Loads specified model (Includes checkpoints from 1k to 10k epochs of trained model)
- test_picture.py - Predicts image from test set
- test_video.py - Main script that predicts Sign Language in real time
- text files - include all instructions and commands to train model, evaluate model, and create the TF Records

Results:
![image](https://github.com/ndinevski/Real_Time_Sign_Language_Detection/assets/61565298/7e295ccb-136d-472d-96f7-0e1a411b61e1)

Labelling images:
![image](https://github.com/ndinevski/Real_Time_Sign_Language_Detection/assets/61565298/65473076-4d65-45a4-b52d-6e0f04b0adb3)
![image](https://github.com/ndinevski/Real_Time_Sign_Language_Detection/assets/61565298/58f42aa2-f94a-4f53-8487-346f9e90e618)

Developed by:

-Petar Atanasovski
-Nikola Dinevski
