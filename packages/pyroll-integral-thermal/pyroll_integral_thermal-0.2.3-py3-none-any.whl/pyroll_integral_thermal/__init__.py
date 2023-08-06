from . import profile_specs
from . import roll_pass_specs
from . import transport_specs

from . import roll_pass_impls
from . import transport_impls

from pyroll import RollPassOutProfile, TransportOutProfile

RollPassOutProfile.hooks.add("temperature")
TransportOutProfile.hooks.add("temperature")

from . import report_impls
