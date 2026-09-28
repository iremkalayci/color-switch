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
    matched_case = context.matched_case or "default"

    case_outputs = {}

    for case_name, output_class in CASE_CLASSES.items():
        if case_name == matched_case:
            case_outputs[case_name] = output_class(
                value=context.normalize(context.input_data)
            )
        else:
            case_outputs[case_name] = output_class(
                value="",
                branch="stop"
            )

    outputs = PackageOutputs(**case_outputs)

    response = PackageResponse(outputs=outputs)

    executor = ColorSwitch(value=response)

    config_executor = ConfigExecutor(value=executor)

    package_configs = PackageConfigs(
        executor=config_executor
    )

    package = PackageHelper(
        packageModel=PackageModel,
        packageConfigs=package_configs
    )

    return package.build_model(context)