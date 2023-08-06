import sys

from pyroll import RollPass, RollPassOutProfile


@RollPass.hookimpl
def roll_temperature(roll_pass: RollPass):
    """Default roll temperature at 293.15 K."""
    return 293.15


@RollPass.hookimpl
def deformation_heat_efficiency(roll_pass: RollPass):
    """Default implementation"""
    return 0.95


@RollPass.hookimpl
def contact_heat_transfer_coefficient(roll_pass: RollPass):
    """Default implementation"""
    return 6e3


@RollPass.hookimpl
def temperature_change_by_contact(roll_pass: RollPass):
    if roll_pass.roll_temperature is None:
        return 0

    volume = (roll_pass.in_profile.cross_section + roll_pass.out_profile.cross_section) / 2 * roll_pass.contact_length
    area_volume_ratio = roll_pass.contact_area * 2 / volume
    time = roll_pass.contact_length / roll_pass.velocity
    denominator = (
                          (roll_pass.in_profile.density + roll_pass.out_profile.density)
                          * (roll_pass.in_profile.thermal_capacity + roll_pass.out_profile.thermal_capacity)
                  ) / 2
    by_contact = -(
            roll_pass.contact_heat_transfer_coefficient * (roll_pass.mean_temperature - roll_pass.roll_temperature)
            * time * area_volume_ratio
    ) / denominator

    return by_contact


@RollPass.hookimpl
def temperature_change_by_deformation(roll_pass: RollPass):
    deformation_resistance = (
        roll_pass.deformation_resistance
        if hasattr(roll_pass, "deformation_resistance")
        else roll_pass.mean_flow_stress
    )
    denominator = (
                          (roll_pass.in_profile.density + roll_pass.out_profile.density)
                          * (roll_pass.in_profile.thermal_capacity + roll_pass.out_profile.thermal_capacity)
                  ) / 2
    by_deformation = roll_pass.deformation_heat_efficiency * deformation_resistance * roll_pass.strain_change / denominator

    return by_deformation


@RollPass.hookimpl
def temperature_change(roll_pass: RollPass):
    return roll_pass.temperature_change_by_contact + roll_pass.temperature_change_by_deformation


@RollPassOutProfile.hookimpl
def temperature(roll_pass: RollPass):
    return roll_pass.in_profile.temperature + roll_pass.temperature_change


RollPass.plugin_manager.register(sys.modules[__name__])
RollPassOutProfile.plugin_manager.register(sys.modules[__name__])
