"""
Switch Case component.

The component normalizes an input value, evaluates configured
cases in order, and selects the first matching case.
"""

import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), "../../../../")
)

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor

from components.Package.src.models.PackageModel import PackageModel
from components.Package.src.utils.response import build_response


class ColorSwitch(Component):
    """
    Routes input data to the first matching switch case.
    """

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)

        self.request.model = PackageModel(**(self.request.data))

        self.input_data = self.request.get_param("inputData")

        self.case_insensitive = self.request.get_param(
            "caseInsensitive"
        )

        self.case1 = self.request.get_param("Case1")
        self.case2 = self.request.get_param("Case2")
        self.case3 = self.request.get_param("Case3")
        self.case4 = self.request.get_param("Case4")
        self.case5 = self.request.get_param("Case5")
        self.case6 = self.request.get_param("Case6")
        self.case7 = self.request.get_param("Case7")
        self.case8 = self.request.get_param("Case8")
        self.case9 = self.request.get_param("Case9")
        self.case10 = self.request.get_param("Case10")

        self.matched_case = None

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def _normalize_input(self, value):
        """
        Normalize the input according to Switch Case rules.
        """

        if isinstance(value, bool):
            return "True" if value else "False"

        if isinstance(value, float):
            return str(value)

        if value is None:
            return "None"

        return str(value)

    def evaluate_condition(self):
        """
        Evaluate cases from case1 to case10 and return
        the first matching case. Return default if no
        case matches.
        """

        normalized_input = self._normalize_input(
            self.input_data
        )

        cases = [
            ("case1", self.case1),
            ("case2", self.case2),
            ("case3", self.case3),
            ("case4", self.case4),
            ("case5", self.case5),
            ("case6", self.case6),
            ("case7", self.case7),
            ("case8", self.case8),
            ("case9", self.case9),
            ("case10", self.case10),
        ]

        for case_name, case_value in cases:

            # Empty cases are ignored.
            if case_value is None:
                continue

            case_value = str(case_value)

            if case_value == "":
                continue

            if self.case_insensitive:
                if normalized_input.lower() == case_value.lower():
                    return case_name

            else:
                if normalized_input == case_value:
                    return case_name

        return "default"

    def run(self):
        self.matched_case = self.evaluate_condition()

        return build_response(context=self)


if "__main__" == __name__:
    Executor(sys.argv[1]).run()