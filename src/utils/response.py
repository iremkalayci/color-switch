from sdks.novavision.src.helper.package import PackageHelper

from components.Package.src.models.ColorSwitchModel import (
    ColorSwitchModel,
    PackageConfigs,
    ConfigExecutor,
    PackageOutputs,
    PackageResponse,
    PackageExecutor,
    OutputRed,
    OutputBlue,
    OutputGreen,
    OutputYellow,
    OutputOrange,
    OutputPurple,
    OutputPink,
    OutputBlack,
    OutputWhite,
    OutputGray,
    OutputDefault,
)


def build_response(context, selected_color):

    def get_branch(color):
        if color == selected_color:
            return "forward"

        return "stop"

    outputs = PackageOutputs(
        red=OutputRed(
            value="red",
            branch=get_branch("red")
        ),

        blue=OutputBlue(
            value="blue",
            branch=get_branch("blue")
        ),

        green=OutputGreen(
            value="green",
            branch=get_branch("green")
        ),

        yellow=OutputYellow(
            value="yellow",
            branch=get_branch("yellow")
        ),

        orange=OutputOrange(
            value="orange",
            branch=get_branch("orange")
        ),

        purple=OutputPurple(
            value="purple",
            branch=get_branch("purple")
        ),

        pink=OutputPink(
            value="pink",
            branch=get_branch("pink")
        ),

        black=OutputBlack(
            value="black",
            branch=get_branch("black")
        ),

        white=OutputWhite(
            value="white",
            branch=get_branch("white")
        ),

        gray=OutputGray(
            value="gray",
            branch=get_branch("gray")
        ),

        default=OutputDefault(
            value="default",
            branch=get_branch("default")
        ),
    )

    package_response = PackageResponse(
        outputs=outputs
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
        packageModel=ColorSwitchModel,
        packageConfigs=package_configs
    )

    package_model = package.build_model(context)

    return package_model