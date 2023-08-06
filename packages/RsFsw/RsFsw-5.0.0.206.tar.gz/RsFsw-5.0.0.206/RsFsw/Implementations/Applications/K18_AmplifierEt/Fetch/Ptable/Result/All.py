from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:PTABle[:RESult]:ALL \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.ptable.result.all.get() \n
		This command queries all numerical results shown in the Parameter Sweep Table. \n
			:return: results: numeric value: Results as a comma separated list. EVMMinValue, EVMMinX, EVMMinY, ACPMinCalue, ACPMinX, ACPMinY,... The unit depends on the result and parameters assigned to the x- and y-axis. If a result hasn't been calculated, the command returns NAN."""
		response = self._core.io.query_str(f'FETCh:PTABle:RESult:ALL?')
		return Conversions.str_to_float(response)
