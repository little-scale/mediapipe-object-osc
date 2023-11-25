# mediapipe-object-osc
Mediapipe Object Detection Solution to OSC

Based on https://developers.google.com/mediapipe/solutions/vision/object_detector 

Adds basic OSC output for the Mediapipe object detection solution

By default, OSC will be sent to 127.0.0.1 localhost on port 3000 and with address /mediapipe/objects. This can be changed in utils.py

Each OSC message contains: 
Category name, object detection instance within the frame, normalised x position, normalised y position and certainty 

An example Ableton Max for Live device is provided which allows mapping an object calss with x and y position to Ableton parameters

To run: 
- Download and unzip repo
- You will need a model to use in the same directory. This could be an existing model like https://github.com/schu-lab/Tensorflow-Object-Detection/blob/main/efficientdet_lite0.tflite or you could train your own model https://developers.google.com/mediapipe/solutions/customization/object_detector 
- Change line 114 of detect.py to point to the model you would like to use
- Change line 7 - 9 of utils.py to change OSC IP, port and address
- In terminal, run pip install mediapipe and pip install python-osc
- Then change directory to repo and run python detect.py

