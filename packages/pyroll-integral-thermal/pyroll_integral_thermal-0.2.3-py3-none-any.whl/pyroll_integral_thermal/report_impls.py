import sys
from typing import Sequence

import numpy as np
from pyroll import RollPass, Transport, Unit
from pyroll.ui.report import Report, utils
from pyroll.utils.hookutils import applies_to_unit_types


@Report.hookimpl(specname="unit_properties")
@applies_to_unit_types(RollPass)
def pass_properties(unit: RollPass):
    return {
        "temperature change": "{:.2g}".format(unit.temperature_change),
        "temperature change by deformation": "{:.2g}".format(unit.temperature_change_by_deformation),
        "temperature change by contact": "{:.2g}".format(unit.temperature_change_by_contact),
    }


@Report.hookimpl(specname="unit_properties")
@applies_to_unit_types(Transport)
def transport_properties(unit: Transport):
    return {
        "temperature change": "{:.2g}".format(unit.temperature_change),
        "temperature change by convection": "{:.2g}".format(unit.temperature_change_by_convection),
        "temperature change by cooling": "{:.2g}".format(unit.temperature_change_by_cooling),
        "temperature change by radiation": "{:.2g}".format(unit.temperature_change_by_radiation),
    }


@Report.hookimpl
def sequence_plot(units: Sequence[Unit]):
    """Plot the temperatures of all profiles"""
    fig, ax = utils.create_sequence_plot(units)
    ax.set_ylabel(r"temperature $T$")
    ax.set_title("Mean Profile Temperatures")

    units = list(units)
    if len(units) > 0:
        def gen_seq():
            yield -0.5, units[0].in_profile.temperature
            for i, u in enumerate(units):
                yield i + 0.5, u.out_profile.temperature

        x, y = np.transpose(
            list(gen_seq())
        )

        ax.plot(x, y, marker="x")

        return fig


Report.plugin_manager.register(sys.modules[__name__])
