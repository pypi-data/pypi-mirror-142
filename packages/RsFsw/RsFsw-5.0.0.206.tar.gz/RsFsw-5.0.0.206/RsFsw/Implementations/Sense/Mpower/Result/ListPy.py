from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:MPOWer:RESult[:LIST] \n
		Snippet: value: float = driver.sense.mpower.result.listPy.get() \n
		This command queries the results of the pulse power measurement. This command may be used to obtain measurement results
		in an asynchronous way, using the service request mechanism for synchronization to the end of the measurement. If there
		are no results, the command returns an error. \n
			:return: pulse_power: List of pulse powers. The number of values depends on the number of pulses you have been measuring. The unit is dBm."""
		response = self._core.io.query_str(f'SENSe:MPOWer:RESult:LIST?')
		return Conversions.str_to_float(response)
