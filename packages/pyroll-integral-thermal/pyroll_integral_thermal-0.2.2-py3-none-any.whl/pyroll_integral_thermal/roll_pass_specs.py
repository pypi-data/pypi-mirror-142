import sys

from pyroll import RollPass, RollPassOutProfile


@RollPass.hookspec
def roll_temperature(roll_pass: RollPass):
    """Get the mean temperature of the working rolls."""


@RollPass.hookspec
def deformation_heat_efficiency(roll_pass: RollPass):
    """Efficiency of heat generation through deformation. 1 means that all forming energy is dissipated as heat, 0 that all energy is saved in microstructure."""


@RollPass.hookspec
def contact_heat_transfer_coefficient(roll_pass: RollPass):
    """Get the heat transfer coefficient for contact of rolls and workpiece."""


@RollPass.hookspec
def temperature_change_by_contact(roll_pass):
    """Get the change in temperature by contact transfer within the roll pass."""


@RollPass.hookspec
def temperature_change_by_deformation(roll_pass):
    """Get the change in temperature by deformation heat within the roll pass."""


@RollPass.hookspec
def temperature_change(roll_pass):
    """Get the change in temperature within the roll pass."""


@RollPassOutProfile.hookspec
def temperature(roll_pass, profile):
    """Get the temperature of the out profile."""


RollPass.plugin_manager.add_hookspecs(sys.modules[__name__])
RollPassOutProfile.plugin_manager.add_hookspecs(sys.modules[__name__])
