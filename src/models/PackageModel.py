"""
ColorSwitch PackageModel.
String-based models for testing Switch Case before HSV integration.
"""
from typing import Optional, Union, Literal

from sdks.novavision.src.base.model import (
    Package, Inputs, Configs, Outputs, Response, Request, Output, Input, Config,
)


class InputData(Input):
    name: Literal["inputData"] = "inputData"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Input Data"


class PackageInputs(Inputs):
    inputData: InputData


class Case1Output(Output):
    name: Literal["case1"] = "case1"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 1"


class Case2Output(Output):
    name: Literal["case2"] = "case2"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 2"


class Case3Output(Output):
    name: Literal["case3"] = "case3"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 3"


class Case4Output(Output):
    name: Literal["case4"] = "case4"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 4"


class Case5Output(Output):
    name: Literal["case5"] = "case5"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 5"


class Case6Output(Output):
    name: Literal["case6"] = "case6"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 6"


class Case7Output(Output):
    name: Literal["case7"] = "case7"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 7"


class Case8Output(Output):
    name: Literal["case8"] = "case8"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 8"


class Case9Output(Output):
    name: Literal["case9"] = "case9"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 9"


class Case10Output(Output):
    name: Literal["case10"] = "case10"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 10"


class DefaultOutput(Output):
    name: Literal["default"] = "default"
    value: str
    type: Literal["string"] = "string"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Default"


class PackageOutputs(Outputs):
    case1: Case1Output
    case2: Case2Output
    case3: Case3Output
    case4: Case4Output
    case5: Case5Output
    case6: Case6Output
    case7: Case7Output
    case8: Case8Output
    case9: Case9Output
    case10: Case10Output
    default: DefaultOutput


class ConfigCase1(Config):
    """Value to compare with inputData for Case 1."""

    name: Literal["Case1"] = "Case1"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 1 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 1 match value"
        }


class ConfigCase2(Config):
    """Value to compare with inputData for Case 2."""

    name: Literal["Case2"] = "Case2"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 2 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 2 match value"
        }


class ConfigCase3(Config):
    """Value to compare with inputData for Case 3."""

    name: Literal["Case3"] = "Case3"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 3 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 3 match value"
        }


class ConfigCase4(Config):
    """Value to compare with inputData for Case 4."""

    name: Literal["Case4"] = "Case4"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 4 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 4 match value"
        }


class ConfigCase5(Config):
    """Value to compare with inputData for Case 5."""

    name: Literal["Case5"] = "Case5"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 5 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 5 match value"
        }


class ConfigCase6(Config):
    """Value to compare with inputData for Case 6."""

    name: Literal["Case6"] = "Case6"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 6 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 6 match value"
        }


class ConfigCase7(Config):
    """Value to compare with inputData for Case 7."""

    name: Literal["Case7"] = "Case7"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 7 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 7 match value"
        }


class ConfigCase8(Config):
    """Value to compare with inputData for Case 8."""

    name: Literal["Case8"] = "Case8"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 8 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 8 match value"
        }


class ConfigCase9(Config):
    """Value to compare with inputData for Case 9."""

    name: Literal["Case9"] = "Case9"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 9 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 9 match value"
        }


class ConfigCase10(Config):
    """Value to compare with inputData for Case 10."""

    name: Literal["Case10"] = "Case10"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 10 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 10 match value"
        }


class OptionEnable(Config):
    name: Literal["enable"] = "enable"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class OptionDisable(Config):
    name: Literal["disable"] = "disable"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"


class CaseInsensitive(Config):
    """Controls case-sensitive or case-insensitive matching."""

    name: Literal["caseInsensitive"] = "caseInsensitive"
    value: Union[OptionEnable, OptionDisable]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Case Insensitive"
        json_schema_extra = {
            "shortDescription": "Case-insensitive matching"
        }


class ExecutorConfigs(Configs):
    case1: ConfigCase1
    case2: ConfigCase2
    case3: ConfigCase3
    case4: ConfigCase4
    case5: ConfigCase5
    case6: ConfigCase6
    case7: ConfigCase7
    case8: ConfigCase8
    case9: ConfigCase9
    case10: ConfigCase10
    caseInsensitive: CaseInsensitive


class PackageRequest(Request):
    inputs: Optional[PackageInputs]
    configs: ExecutorConfigs

    class Config:
        json_schema_extra = {"target": "configs"}


class PackageResponse(Response):
    outputs: PackageOutputs


class ColorSwitch(Config):
    name: Literal["ColorSwitch"] = "ColorSwitch"
    value: Union[PackageRequest, PackageResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Color Switch"
        json_schema_extra = {"target": {"value": 0}}


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: ColorSwitch
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {"target": "value"}


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["ColorSwitch"] = "ColorSwitch"
