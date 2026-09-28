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

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)

        self.request.model = PackageModel(**self.request.data)

        self.input_data = self.request.get_param("inputData")
        self.case_insensitive = self.request.get_param(
            "caseInsensitive"
        )

        self.cases = [
            ("case1", self.request.get_param("Case1")),
            ("case2", self.request.get_param("Case2")),
            ("case3", self.request.get_param("Case3")),
            ("case4", self.request.get_param("Case4")),
            ("case5", self.request.get_param("Case5")),
            ("case6", self.request.get_param("Case6")),
            ("case7", self.request.get_param("Case7")),
            ("case8", self.request.get_param("Case8")),
            ("case9", self.request.get_param("Case9")),
            ("case10", self.request.get_param("Case10")),
        ]

        self.matched_case = None

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    @staticmethod
    def normalize(value):
        if value is None:
            return "None"
        if isinstance(value, bool):
            return str(value)
        return str(value)

    @staticmethod
    def is_case_insensitive(value):
        if isinstance(value, bool):
            return value

        if isinstance(value, dict):
            return value.get("value") is True

        option = getattr(value, "value", None)

        if isinstance(option, bool):
            return option

        return False

    def evaluate_condition(self):
        input_value = self.normalize(self.input_data)
        insensitive = self.is_case_insensitive(
            self.case_insensitive
        )

        for case_name, case_value in self.cases:
            if case_value is None:
                continue

            case_value = self.normalize(case_value)

            if case_value == "":
                continue

            if insensitive:
                if input_value.casefold() == case_value.casefold():
                    return case_name
            else:
                if input_value == case_value:
                    return case_name

        return "default"

    def run(self):
        self.matched_case = self.evaluate_condition()
        print("MATCHED CASE:", self.matched_case, flush=True)
        return build_response(context=self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()