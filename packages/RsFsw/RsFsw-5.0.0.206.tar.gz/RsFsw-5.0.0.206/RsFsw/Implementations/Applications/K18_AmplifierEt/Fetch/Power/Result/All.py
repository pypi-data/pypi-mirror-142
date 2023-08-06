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
		"""SCPI: FETCh:POWer[:RESult]:ALL \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.power.result.all.get() \n
		This command queries all power related numerical results as shown in the result summary. \n
			:return: results: numerical value: Results as a comma separated list. The order of results is the same as in the result summary: The unit depends on the result. If a result hasn't been calculated, the command returns NAN."""
		response = self._core.io.query_str(f'FETCh:POWer:RESult:ALL?')
		return Conversions.str_to_float(response)
