import sys

from pyroll import Profile


@Profile.hookimpl
def density(profile: Profile):
    raise ValueError("You must provide a density to use the pyroll-intergal-thermal plugin.")


@Profile.hookimpl
def thermal_capacity(profile: Profile):
    raise ValueError("You must provide a thermal capacity to use the pyroll-intergal-thermal plugin.")


Profile.plugin_manager.register(sys.modules[__name__])
