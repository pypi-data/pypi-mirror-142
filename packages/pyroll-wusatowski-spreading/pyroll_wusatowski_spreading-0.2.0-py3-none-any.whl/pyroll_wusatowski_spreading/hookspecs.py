import sys

from pyroll import RollPass


@RollPass.hookspec
def wusatowski_temperature_coefficient(roll_pass):
    """Gets the Wusatowski spreading model temperature coefficient a."""


@RollPass.hookspec
def wusatowski_velocity_coefficient(roll_pass):
    """Gets the Wusatowski spreading model velocity coefficient c."""


@RollPass.hookspec
def wusatowski_material_coefficient(roll_pass):
    """Gets the Wusatowski spreading model material coefficient d."""


@RollPass.hookspec
def wusatowski_friction_coefficient(roll_pass):
    """Gets the Wusatowski spreading model friction coefficient f."""


@RollPass.hookspec
def wusatowski_exponent(roll_pass):
    """Gets the Wusatowski spreading model exponent w."""


RollPass.plugin_manager.add_hookspecs(sys.modules[__name__])
