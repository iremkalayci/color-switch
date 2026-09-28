from sdks.novavision.src.helper.package import PackageHelper

from components.SwitchCase.src.models.PackageModel import (
    PackageModel,
    PackageConfigs,
    ConfigExecutor,
    ExecutorSwitchCase,
    ExecutorResponse,
    ExecutorOutputs,
)


def build_response(context):
    outputs = {}

    for route_name, target in context.routes.items():
        outputs[route_name] = {
            "name": route_name,
            "value": target,
            "type": "string",
            "branch": (
                "forward"
                if route_name == context.selected_route
                else "stop"
            ),
            "listen": "continuous",
        }

    executor_response = ExecutorResponse(
        outputs=ExecutorOutputs(**outputs)
    )

    executor = ExecutorSwitchCase(value=executor_response)

    package_configs = PackageConfigs(
        executor=ConfigExecutor(value=executor)
    )

    package = PackageHelper(
        packageModel=PackageModel,
        packageConfigs=package_configs,
    )

    return package.build_model(context)