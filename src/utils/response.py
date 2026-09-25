from sdks.novavision.src.helper.package import PackageHelper

from components.Package.src.models.PackageModel import (
    PackageModel,
    PackageConfigs,
    ConfigExecutor,
    PackageOutputs,
    PackageResponse,
    PackageExecutor,
    Case1,
    Case2,
    Case3,
    Case4,
    Case5,
    Case6,
    Case7,
    Case8,
    Case9,
    Case10,
    Default,
)


def build_response(context, selected_case):

    cases = {
        "case1": Case1,
        "case2": Case2,
        "case3": Case3,
        "case4": Case4,
        "case5": Case5,
        "case6": Case6,
        "case7": Case7,
        "case8": Case8,
        "case9": Case9,
        "case10": Case10,
        "default": Default,
    }

    outputs = {}

    for case_name, output_class in cases.items():

        branch = (
            "forward"
            if case_name == selected_case
            else "stop"
        )

        outputs[case_name] = output_class(
            value=case_name,
            branch=branch
        )

    package_outputs = PackageOutputs(**outputs)

    package_response = PackageResponse(
        outputs=package_outputs
    )

    package_executor = PackageExecutor(
        value=package_response
    )

    executor = ConfigExecutor(
        value=package_executor
    )

    package_configs = PackageConfigs(
        executor=executor
    )

    package = PackageHelper(
        packageModel=PackageModel,
        packageConfigs=package_configs
    )

    return package.build_model(context)