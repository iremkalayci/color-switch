"""
    Color Switch component.

    Routes the input color to the matching output branch.

    If the color does not match any defined case,
    the default branch is selected.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor

from components.Package.src.utils.response import build_response
from components.Package.src.models.PackageModel import PackageModel


class Package(Component):

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)

        self.request.model = PackageModel(**self.request.data)
        self.color = self.request.get_param("color")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def normalize_color(self):
        if self.color is None:
            return None

        return str(self.color).strip().lower()

    def run(self):
        color = self.normalize_color()

        match color:
            case "red":
                selected_color = "red"

            case "blue":
                selected_color = "blue"

            case "green":
                selected_color = "green"

            case "yellow":
                selected_color = "yellow"

            case "orange":
                selected_color = "orange"

            case "purple":
                selected_color = "purple"

            case "pink":
                selected_color = "pink"

            case "black":
                selected_color = "black"

            case "white":
                selected_color = "white"

            case "gray":
                selected_color = "gray"

            case _:
                selected_color = "default"

        package_model = build_response(
            context=self,
            selected_color=selected_color
        )

        return package_model


if __name__ == "__main__":
    Executor(sys.argv[1]).run()