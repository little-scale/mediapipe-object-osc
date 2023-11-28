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
- To use with Ableton Live, load the Object Detection Receiver (little-scale.object-detection-receiver.amxd) M4L device on an Audio track
- Choose the right OSC port (default is 3000 or 3001) and run the object detection Python script above
- As object classes are detected, the drop down menu in the M4L device will populate
- Choose the right object class from the drop down menu
- Now map X and Y location of that particular class to Ableton parameters
- Smooth smooths out values over time
- Note - multiple little-scale.object-detection-receiver.amxd devices can be loaded in the same set without issue

