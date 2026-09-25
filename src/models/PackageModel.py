from typing import Optional, Union, Literal

from sdks.novavision.src.base.model import (
    Package,
    Inputs,
    Configs,
    Outputs,
    Response,
    Request,
    Output,
    Input,
    Config,
)


# =========================
# INPUT
# =========================

class InputData(Input):
    name: Literal["inputData"] = "inputData"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Input"


class PackageInputs(Inputs):
    inputData: InputData


# =========================
# OUTPUTS
# =========================

class Case1(Output):
    name: Literal["case1"] = "case1"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 1"


class Case2(Output):
    name: Literal["case2"] = "case2"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 2"


class Case3(Output):
    name: Literal["case3"] = "case3"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 3"


class Case4(Output):
    name: Literal["case4"] = "case4"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 4"


class Case5(Output):
    name: Literal["case5"] = "case5"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 5"


class Case6(Output):
    name: Literal["case6"] = "case6"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 6"


class Case7(Output):
    name: Literal["case7"] = "case7"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 7"


class Case8(Output):
    name: Literal["case8"] = "case8"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 8"


class Case9(Output):
    name: Literal["case9"] = "case9"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 9"


class Case10(Output):
    name: Literal["case10"] = "case10"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Case 10"


class Default(Output):
    name: Literal["default"] = "default"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Default"


class PackageOutputs(Outputs):
    case1: Case1
    case2: Case2
    case3: Case3
    case4: Case4
    case5: Case5
    case6: Case6
    case7: Case7
    case8: Case8
    case9: Case9
    case10: Case10
    default: Default


# =========================
# REQUEST / RESPONSE
# =========================

class PackageRequest(Request):
    inputs: Optional[PackageInputs]
    configs: Optional[Configs]

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class PackageResponse(Response):
    outputs: PackageOutputs


# =========================
# EXECUTOR
# =========================

class PackageExecutor(Config):
    name: Literal["Package"] = "Package"
    value: Union[PackageRequest, PackageResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Switch Case"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: PackageExecutor
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor


# =========================
# PACKAGE MODEL
# =========================

class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["ColorSwitch"] = "ColorSwitch"