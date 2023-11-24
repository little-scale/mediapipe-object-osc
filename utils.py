import cv2
import numpy as np

from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

ip = "127.0.0.1"
port = 3000
address = "/mediapipe/objects"

MARGIN = 10  # pixels
ROW_SIZE = 1  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red

client = udp_client.SimpleUDPClient(ip, port, True)



def visualize(width, height,
    image,
    detection_result
) -> np.ndarray:

  det = 0
  
  for detection in detection_result.detections:
    # print(detection)
    # Draw bounding_box

    det = det + 1
    
    bbox = detection.bounding_box
    x_pos = (bbox.origin_x + (bbox.width / 2)) / width
    y_pos = (bbox.origin_y + (bbox.height / 2)) / height

    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name
    probability = round(category.score, 2)
    
    print(category_name, x_pos, y_pos, probability)
    # send normalised 
    client.send_message(address, [category_name, det, x_pos, 1 - y_pos, probability])
    
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x,
                     MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

  return image
