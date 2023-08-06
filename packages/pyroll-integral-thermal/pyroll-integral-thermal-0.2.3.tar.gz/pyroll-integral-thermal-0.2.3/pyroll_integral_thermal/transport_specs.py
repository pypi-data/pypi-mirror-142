import sys

from pyroll import Transport, TransportOutProfile


@Transport.hookspec
def atmosphere_temperature(transport: Transport):
    """Get the temperature of the surrounding atmosphere."""


@Transport.hookspec
def cooling_water_temperature(transport: Transport):
    """Get the temperature of the cooling water."""


@Transport.hookspec
def convection_heat_transfer_coefficient(transport: Transport):
    """Get the heat transfer coefficient for contact of rolls and workpiece."""


@Transport.hookspec
def cooling_heat_transfer_coefficient(transport: Transport):
    """Get the heat transfer coefficient for contact of rolls and workpiece."""


@Transport.hookspec
def relative_radiation_coefficient(transport: Transport):
    """Get the heat transfer coefficient for contact of rolls and workpiece."""


@Transport.hookspec
def temperature_change_by_convection(transport):
    """Get the change in temperature by convection within the transport."""


@Transport.hookspec
def temperature_change_by_cooling(transport):
    """Get the change in temperature by cooling within the transport."""


@Transport.hookspec
def temperature_change_by_radiation(transport):
    """Get the change in temperature by radiation within the transport."""


@Transport.hookspec
def temperature_change(transport):
    """Get the change in temperature within the transport."""


@TransportOutProfile.hookspec
def temperature(transport):
    """Get the temperature of the out profile."""


Transport.plugin_manager.add_hookspecs(sys.modules[__name__])
TransportOutProfile.plugin_manager.add_hookspecs(sys.modules[__name__])
