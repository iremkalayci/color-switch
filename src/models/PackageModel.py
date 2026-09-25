"""
ColorSwitch PackageModel.

ColorSwitch executor'unun kullandigi tum get_param anahtarlariyla
(inputData, caseInsensitive, Case1..Case10) uyumlu,
asagidan yukariya (bottom-up) kurulmus Pydantic modelleri.
"""

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


# ---------------------------------------------------------------------------
# 1) INPUT
# ---------------------------------------------------------------------------

class InputData(Input):
    name: Literal["inputData"] = "inputData"
    value: Union[dict, list]
    type: Literal["object"] = "object"

    class Config:
        title = "Input Data"


class PackageInputs(Inputs):
    inputData: InputData


# ---------------------------------------------------------------------------
# 2) OUTPUTS
# ---------------------------------------------------------------------------
# Eslesen case gercek veriyi tasir.
# Eslesmeyen case'ler branch="stop" alir.
# Default da ayni sekilde bir output branch'idir.


class Case1Output(Output):
    name: Literal["case1"] = "case1"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 1"


class Case2Output(Output):
    name: Literal["case2"] = "case2"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 2"


class Case3Output(Output):
    name: Literal["case3"] = "case3"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 3"


class Case4Output(Output):
    name: Literal["case4"] = "case4"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 4"


class Case5Output(Output):
    name: Literal["case5"] = "case5"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 5"


class Case6Output(Output):
    name: Literal["case6"] = "case6"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 6"


class Case7Output(Output):
    name: Literal["case7"] = "case7"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 7"


class Case8Output(Output):
    name: Literal["case8"] = "case8"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 8"


class Case9Output(Output):
    name: Literal["case9"] = "case9"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 9"


class Case10Output(Output):
    name: Literal["case10"] = "case10"
    value: Union[dict, list]
    type: Literal["object"] = "object"
    branch: Optional[Literal["stop"]] = None

    class Config:
        title = "Case 10"


class DefaultOutput(Output):
    name: Literal["default"] = "default"
    value: Union[dict, list]
    type: Literal["object"] = "object"
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


# ---------------------------------------------------------------------------
# 3) CASE CONFIGS
# ---------------------------------------------------------------------------

class ConfigCase1(Config):
    """
    Case 1 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case1"] = "Case1"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 1 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 1 eslesme degeri"
        }


class ConfigCase2(Config):
    """
    Case 2 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case2"] = "Case2"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 2 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 2 eslesme degeri"
        }


class ConfigCase3(Config):
    """
    Case 3 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case3"] = "Case3"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 3 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 3 eslesme degeri"
        }


class ConfigCase4(Config):
    """
    Case 4 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case4"] = "Case4"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 4 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 4 eslesme degeri"
        }


class ConfigCase5(Config):
    """
    Case 5 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case5"] = "Case5"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 5 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 5 eslesme degeri"
        }


class ConfigCase6(Config):
    """
    Case 6 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case6"] = "Case6"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 6 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 6 eslesme degeri"
        }


class ConfigCase7(Config):
    """
    Case 7 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case7"] = "Case7"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 7 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 7 eslesme degeri"
        }


class ConfigCase8(Config):
    """
    Case 8 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case8"] = "Case8"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 8 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 8 eslesme degeri"
        }


class ConfigCase9(Config):
    """
    Case 9 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case9"] = "Case9"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 9 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 9 eslesme degeri"
        }


class ConfigCase10(Config):
    """
    Case 10 icin inputData ile karsilastirilacak deger.
    Bos birakilirsa bu case atlanir.
    """

    name: Literal["Case10"] = "Case10"
    value: Optional[str] = None
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Case 10 Match Value"
        json_schema_extra = {
            "shortDescription": "Case 10 eslesme degeri"
        }


# ---------------------------------------------------------------------------
# 4) CASE INSENSITIVE CONFIG
# ---------------------------------------------------------------------------

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

    class Config:
        title = "Disable"


class CaseInsensitive(Config):
    """
    Case degerleri karsilastirilirken buyuk/kucuk harf duyarliligini
    belirler.
    """

    name: Literal["caseInsensitive"] = "caseInsensitive"
    value: Union[OptionEnable, OptionDisable]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Case Insensitive"
        json_schema_extra = {
            "shortDescription": "Buyuk/kucuk harf duyarliligi"
        }


# ---------------------------------------------------------------------------
# 5) CONFIG AGGREGATION
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# 6) REQUEST / RESPONSE
# ---------------------------------------------------------------------------

class PackageRequest(Request):
    inputs: Optional[PackageInputs]
    configs: ExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class PackageResponse(Response):
    outputs: PackageOutputs


# ---------------------------------------------------------------------------
# 7) EXECUTOR CONFIG
# ---------------------------------------------------------------------------

class ColorSwitch(Config):
    name: Literal["ColorSwitch"] = "ColorSwitch"
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
    value: ColorSwitch
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


# ---------------------------------------------------------------------------
# 8) PACKAGE CONFIGS / MODEL
# ---------------------------------------------------------------------------

class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["ColorSwitch"] = "ColorSwitch"