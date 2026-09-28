import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), "../../../../")
)

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor

from components.SwitchCase.src.models.PackageModel import PackageModel
from components.SwitchCase.src.utils.response import build_response


class SwitchCase(Component):

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)

        self.request.model = PackageModel(**self.request.data)

        self.value = self.request.get_param("value")
        self.cases = self.request.get_param("cases") or {}
        self.default_next_steps = (
            self.request.get_param("default_next_steps") or []
        )
        self.case_insensitive = bool(
            self.request.get_param("case_insensitive")
        )

        self.selected_route = None
        self.routes = {}

        self._validate_inputs()

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def _validate_inputs(self):
        if not isinstance(self.cases, dict):
            raise ValueError("'cases' must be a dictionary")

        if not isinstance(self.default_next_steps, list):
            raise ValueError("'default_next_steps' must be a list")

        targets = list(self.cases.values()) + self.default_next_steps

        if any(not isinstance(target, str) or not target for target in targets):
            raise ValueError("Every step target must be a non-empty string")

        if len(targets) != len(set(targets)):
            raise ValueError(
                "A target step may appear only once across cases "
                "and default_next_steps"
            )

    def _normalize(self, value):
        result = str(value)
        return result.casefold() if self.case_insensitive else result

    def select_route(self):
        value = self._normalize(self.value)

        for case_value, target in self.cases.items():
            if self._normalize(case_value) == value:
                return case_value

        return None

    def run(self):
        matched_case = self.select_route()

        if matched_case is not None:
            self.selected_route = matched_case
            self.routes = dict(self.cases)
        elif self.default_next_steps:
            self.selected_route = "__default__"
            self.routes = {
                "__default__": self.default_next_steps[0]
            }
        else:
            self.selected_route = None
            self.routes = {}

        return build_response(context=self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()