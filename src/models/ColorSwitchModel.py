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

class InputColor(Input):
    name: Literal["color"] = "color"
    value: str
    type: Literal["string"] = "string"

    class Config:
        title = "Color"


class PackageInputs(Inputs):
    color: InputColor


# =========================
# OUTPUTS
# =========================

class OutputRed(Output):
    name: Literal["red"] = "red"
    value: str
    type: Literal["string"] = "string"


class OutputBlue(Output):
    name: Literal["blue"] = "blue"
    value: str
    type: Literal["string"] = "string"


class OutputGreen(Output):
    name: Literal["green"] = "green"
    value: str
    type: Literal["string"] = "string"


class OutputYellow(Output):
    name: Literal["yellow"] = "yellow"
    value: str
    type: Literal["string"] = "string"


class OutputOrange(Output):
    name: Literal["orange"] = "orange"
    value: str
    type: Literal["string"] = "string"


class OutputPurple(Output):
    name: Literal["purple"] = "purple"
    value: str
    type: Literal["string"] = "string"


class OutputPink(Output):
    name: Literal["pink"] = "pink"
    value: str
    type: Literal["string"] = "string"


class OutputBlack(Output):
    name: Literal["black"] = "black"
    value: str
    type: Literal["string"] = "string"


class OutputWhite(Output):
    name: Literal["white"] = "white"
    value: str
    type: Literal["string"] = "string"


class OutputGray(Output):
    name: Literal["gray"] = "gray"
    value: str
    type: Literal["string"] = "string"


class OutputDefault(Output):
    name: Literal["default"] = "default"
    value: str
    type: Literal["string"] = "string"


class PackageOutputs(Outputs):
    red: OutputRed
    blue: OutputBlue
    green: OutputGreen
    yellow: OutputYellow
    orange: OutputOrange
    purple: OutputPurple
    pink: OutputPink
    black: OutputBlack
    white: OutputWhite
    gray: OutputGray
    default: OutputDefault


# =========================
# REQUEST / RESPONSE
# =========================

class PackageRequest(Request):
    inputs: Optional[PackageInputs] = None
    configs: Optional[Configs] = None

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
        title = "Color Switch"
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


# =========================
# PACKAGE CONFIGS
# =========================

class PackageConfigs(Configs):
    executor: ConfigExecutor


# =========================
# PACKAGE MODEL
# =========================

class ColorSwitchModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["ColorSwitch"] = "ColorSwitch"