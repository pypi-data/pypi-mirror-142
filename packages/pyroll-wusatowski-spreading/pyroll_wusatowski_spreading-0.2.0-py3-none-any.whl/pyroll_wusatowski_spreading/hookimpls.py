import sys

from pyroll import RollPass


@RollPass.hookimpl
def wusatowski_temperature_coefficient(roll_pass):
    return 1


@RollPass.hookimpl
def wusatowski_velocity_coefficient(roll_pass):
    compression = (roll_pass.ideal_out_profile.equivalent_rectangle.height
                   / roll_pass.in_profile.equivalent_rectangle.height)
    return (-0.002958 + 0.00341 * compression) * roll_pass.velocity + 1.07168 - 0.10431 * compression


@RollPass.hookimpl
def wusatowski_material_coefficient(roll_pass):
    return 1


@RollPass.hookimpl
def wusatowski_friction_coefficient(roll_pass):
    return 1


@RollPass.hookimpl
def wusatowski_exponent(roll_pass):
    in_equivalent_height = roll_pass.in_profile.equivalent_rectangle.height
    in_equivalent_width = roll_pass.in_profile.equivalent_rectangle.width
    return 10 ** (
            -1.269 * (in_equivalent_height / (2 * roll_pass.roll_radius)) ** 0.56
            * in_equivalent_width / in_equivalent_height
    )


@RollPass.hookimpl
def width_change(roll_pass: RollPass):
    compression = (roll_pass.ideal_out_profile.equivalent_rectangle.height
                   / roll_pass.in_profile.equivalent_rectangle.height)
    spread = (
            roll_pass.wusatowski_temperature_coefficient
            * roll_pass.wusatowski_velocity_coefficient
            * roll_pass.wusatowski_material_coefficient
            * roll_pass.wusatowski_friction_coefficient
            * compression ** (-roll_pass.wusatowski_exponent)
    )
    out_equivalent_width = spread * roll_pass.in_profile.equivalent_rectangle.width

    out_profile_width = (out_equivalent_width * roll_pass.ideal_out_profile.height
                         / roll_pass.ideal_out_profile.equivalent_rectangle.height)
    width_change = out_profile_width - roll_pass.in_profile.rotated.width

    return width_change


RollPass.plugin_manager.register(sys.modules[__name__])
