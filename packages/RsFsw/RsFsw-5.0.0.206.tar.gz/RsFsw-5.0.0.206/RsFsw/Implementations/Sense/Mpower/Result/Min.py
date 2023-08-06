from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Min:
	"""Min commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("min", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:MPOWer:RESult:MIN \n
		Snippet: value: float = driver.sense.mpower.result.min.get() \n
		This command queries the lowest pulse power that has been measured during a pulse power measurement. If there are no
		results, the command returns an error. \n
			:return: pulse_power: Lowest power level of the pulse power measurement. The unit is dBm."""
		response = self._core.io.query_str(f'SENSe:MPOWer:RESult:MIN?')
		return Conversions.str_to_float(response)
