# mediapipe-object-osc
Mediapipe Object Detection Solution to OSC

Based on https://developers.google.com/mediapipe/solutions/vision/object_detector 

Adds basic OSC output for the Mediapipe object detection solution

By default, OSC will be sent to 127.0.0.1 localhost on port 3000 and with address /mediapipe/objects. This can be changed in utils.py

Each OSC message contains: 
Category name, object detection instance within the frame, normalised x position, normalised y position and certainty 

An example Ableton Max for Live device is provided which allows mapping an object calss with x and y position to Ableton parameters
