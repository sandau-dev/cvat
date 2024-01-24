import io
import base64
import json

import cv2
import numpy as np
from ultralytics import YOLO

# Initialize your model
def init_context(context):
    context.logger.info('Init context...  0%')

    model = YOLO('vaw-road-defect-classifier.pt')
    context.user_data.model_handler = model
    context.logger.info('Init context...100%')

# Inference endpoint
def handler(context, event):
    context.logger.info('Run YOLOv8 VAW v1 model')
    data = event.body
    image_buffer = io.BytesIO(base64.b64decode(data['image']))
    image = cv2.imdecode(np.frombuffer(image_buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR)

    results = context.user_data.model_handler(image)
    result = results[0]

    if result.masks:
        masks = result.masks.xy
    else:
        masks = np.array([])

    boxes = result.boxes.data[:,:4]
    confs = result.boxes.conf
    clss = result.boxes.cls
    class_name = result.names

    detections = []
    threshold = 0.1
    for mask, conf, cls in zip(masks, confs, clss): # Switch masks to boxes if you want to annotate with bounding boxes
        if mask.any():
            mask_xy_flattened = mask.flatten().tolist()
        else:
            mask_xy_flattened = []
        label = class_name[int(cls)]
        if conf >= threshold:
            # must be in this format
            detections.append({
                'confidence': str(float(conf)),
                'label': label,
                'points': mask_xy_flattened, # boxes.tolist() if you want to annotate with bounding boxes
                'type': 'mask', # Switch this to rectangle if you want to annotate with bounding boxes
            })

    return context.Response(body=json.dumps(detections), headers={},
        content_type='application/json', status_code=200)