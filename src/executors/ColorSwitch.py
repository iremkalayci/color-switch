import os
import sys

import cv2
import numpy as np

sys.path.append(
    os.path.join(os.path.dirname(__file__), "../../../../")
)

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor

from components.Package.src.utils.response import build_response
from components.Package.src.models.PackageModel import PackageModel


class ColorSwitch(Component):

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)

        self.request.model = PackageModel(**self.request.data)
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def detect_color(self, img):

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h = hsv[:, :, 0]
        s = hsv[:, :, 1]
        v = hsv[:, :, 2]

        total_pixels = h.size

        # Black
        black_mask = v < 50

        # White
        white_mask = (s < 40) & (v > 200)

        # Gray
        gray_mask = (
            (s < 50)
            & (v >= 50)
            & (v <= 200)
        )

        # Colors
        red_mask = (
            ((h <= 10) | (h >= 170))
            & (s >= 50)
            & (v >= 50)
        )

        orange_mask = (
            (h >= 11)
            & (h <= 20)
            & (s >= 50)
            & (v >= 50)
        )

        yellow_mask = (
            (h >= 21)
            & (h <= 35)
            & (s >= 50)
            & (v >= 50)
        )

        green_mask = (
            (h >= 36)
            & (h <= 85)
            & (s >= 50)
            & (v >= 50)
        )

        blue_mask = (
            (h >= 86)
            & (h <= 125)
            & (s >= 50)
            & (v >= 50)
        )

        purple_mask = (
            (h >= 126)
            & (h <= 155)
            & (s >= 50)
            & (v >= 50)
        )

        pink_mask = (
            (h >= 156)
            & (h <= 169)
            & (s >= 50)
            & (v >= 50)
        )

        color_masks = {
            "red": red_mask,
            "blue": blue_mask,
            "green": green_mask,
            "yellow": yellow_mask,
            "orange": orange_mask,
            "purple": purple_mask,
            "pink": pink_mask,
            "black": black_mask,
            "white": white_mask,
            "gray": gray_mask,
        }

        scores = {
            color: int(np.count_nonzero(mask))
            for color, mask in color_masks.items()
        }

        detected_color = max(scores, key=scores.get)

        # If no color covers enough of the image
        if scores[detected_color] / total_pixels < 0.05:
            return "default"

        return detected_color

    def run(self):

        img = Image.get_frame(
            img=self.image,
            redis_db=self.redis_db
        )

        detected_color = self.detect_color(img.value)

        package_model = build_response(
            context=self,
            selected_color=detected_color
        )

        return package_model


if __name__ == "__main__":
    Executor(sys.argv[1]).run()