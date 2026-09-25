"""
response.py

build_response, outputs -> response -> executor -> config_executor ->
package_configs -> package zincirini kurar.

context.matched_case ("case1".."case10" ya da "default") degerine gore,
eslesen case veriyi tasir (branch=None); eslesmeyen tum case'ler
branch="stop" ile isaretlenip o dallarda akis durdurulur.
"""

from sdks.novavision.src.helper.package import PackageHelper

from components.Package.src.models.PackageModel import (
    PackageModel,
    PackageConfigs,
    ConfigExecutor,
    PackageOutputs,
    PackageResponse,
    ColorSwitch,
    Case1Output,
    Case2Output,
    Case3Output,
    Case4Output,
    Case5Output,
    Case6Output,
    Case7Output,
    Case8Output,
    Case9Output,
    Case10Output,
    DefaultOutput,
)


CASE_CLASSES = {
    "case1": Case1Output,
    "case2": Case2Output,
    "case3": Case3Output,
    "case4": Case4Output,
    "case5": Case5Output,
    "case6": Case6Output,
    "case7": Case7Output,
    "case8": Case8Output,
    "case9": Case9Output,
    "case10": Case10Output,
    "default": DefaultOutput,
}


def build_response(context):
    """
    context.matched_case: ColorSwitch.evaluate_condition() tarafindan
    belirlenen, inputData'nin hangi case ile eslestigini gosteren
    string ("case1".."case10" ya da eslesme yoksa "default").
    """

    matched_case = getattr(context, "matched_case", None) or "default"

    case_outputs = {}

    for case_name, OutputClass in CASE_CLASSES.items():

        if case_name == matched_case:
            # Eslesen case: veriyi tasir, dal acik kalir.
            case_outputs[case_name] = OutputClass(
                value=context.input_data,
            )

        else:
            # Eslesmeyen case: dal durdurulur.
            case_outputs[case_name] = OutputClass(
                value={},
                branch="stop",
            )

    outputs = PackageOutputs(
        **case_outputs
    )

    response = PackageResponse(
        outputs=outputs
    )

    executor = ColorSwitch(
        value=response
    )

    config_executor = ConfigExecutor(
        value=executor
    )

    package_configs = PackageConfigs(
        executor=config_executor
    )

    package = PackageHelper(
        packageModel=PackageModel,
        packageConfigs=package_configs
    )

    return package.build_model(context)