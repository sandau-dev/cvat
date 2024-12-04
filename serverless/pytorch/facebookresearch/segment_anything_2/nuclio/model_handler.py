# Copyright (C) 2023-2024 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

import numpy as np
import torch
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor

class ModelHandler:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.sam_checkpoint = "/opt/nuclio/sam2/sam2.1_hiera_base_plus.pt"
        self.model_cfg = "configs/sam2.1/sam2.1_hiera_b+.yaml"
        self.predictor = SAM2ImagePredictor(build_sam2(self.model_cfg, self.sam_checkpoint, self.device))

    def handle(self, image, pos_points, neg_points):
        pos_points, neg_points = list(pos_points), list(neg_points)
        with torch.inference_mode():
            self.predictor.set_image(np.array(image))
            masks, scores, _ = self.predictor.predict(
                point_coords=np.array(pos_points + neg_points),
                point_labels=np.array([1]*len(pos_points) + [0]*len(neg_points)),
                multimask_output=True,
            )
            sorted_ind = np.argsort(scores)[::-1]
            best_mask = masks[sorted_ind][0]
            return best_mask
