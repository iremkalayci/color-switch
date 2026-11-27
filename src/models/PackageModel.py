from typing import Dict, List, Literal, Optional, Union

from pydantic import Field

from sdks.novavision.src.base.model import (
    Package,
    Inputs,
    Input,
    Outputs,
    Output,
    Request,
    Response,
    Config,
    Configs,
)


class InputValue(Input):
    name: Literal["value"] = "value"
    value: Union[bool, float, int, str]
    type: str = "string"


class InputCases(Input):
    name: Literal["cases"] = "cases"
    value: Dict[str, str]
    type: Literal["object"] = "object"


class InputDefaultNextSteps(Input):
    name: Literal["default_next_steps"] = "default_next_steps"
    value: List[str] = Field(default_factory=list)
    type: Literal["list"] = "list"


class InputCaseInsensitive(Input):
    name: Literal["case_insensitive"] = "case_insensitive"
    value: bool = False
    type: Literal["bool"] = "bool"


class ExecutorInputs(Inputs):
    value: InputValue
    cases: InputCases
    default_next_steps: Optional[InputDefaultNextSteps] = None
    case_insensitive: InputCaseInsensitive = Field(
        default_factory=InputCaseInsensitive
    )


class ExecutorOutputs(Outputs):
    pass


class ExecutorRequest(Request):
    inputs: ExecutorInputs


class ExecutorResponse(Response):
    outputs: ExecutorOutputs


class ExecutorSwitchCase(Config):
    name: Literal["SwitchCase"] = "SwitchCase"
    value: Union[ExecutorRequest, ExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: ExecutorSwitchCase
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["SwitchCase"] = "SwitchCase"