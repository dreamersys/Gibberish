# Import packages
import os
import numpy as np
import tensorflow as tf
import math
import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

MODEL_NAME = 'inference_graph/saved_model_0207/'
CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH, 'Output Files/labelmap.pbtxt')

NUM_CLASSES = 1
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
num_detections = detection_graph.get_tensor_by_name('num_detections:0')


def arm_detect(frame, prev_time, prev_avg_cood, speed):
    current_avg_cood = None
    frame_expanded = np.expand_dims(frame, axis=0)
    # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    if scores[0][0] > 0.7:
        height, width = frame.shape[:2]
        ymin = int(boxes[0][0][0] * height)
        xmin = int(boxes[0][0][1] * width)
        ymax = int(boxes[0][0][2] * height)
        xmax = int(boxes[0][0][3] * width)
        current_avg_cood = [(xmin + xmax) / 2, (ymin + ymax) / 2]
        delta = math.sqrt(
          (current_avg_cood[0] - prev_avg_cood[0]) ** 2 + (current_avg_cood[1] - prev_avg_cood[1]) ** 2) * 2.54 / 96
        speed = delta / (time.clock() - prev_time)
    else:
        current_avg_cood = prev_avg_cood

    # Draw the results of the detection (aka 'visulaize the results')

    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    return frame, time.clock(), current_avg_cood, speed

