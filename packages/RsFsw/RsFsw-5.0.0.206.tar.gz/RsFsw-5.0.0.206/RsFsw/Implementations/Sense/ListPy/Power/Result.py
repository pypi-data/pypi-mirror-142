from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:LIST:POWer:RESult \n
		Snippet: value: float = driver.sense.listPy.power.result.get() \n
		This command queries the results of the list evaluation. This command may be used to obtain measurement results in an
		asynchronous way, using the service request mechanism for synchronization to the end of the measurement. If there are no
		results, the command returns an error. \n
			:return: power_level: Power level for each frequency included in the measurement. The command returns up to 3 power levels for each frequency, depending on the number of evaluation modes you have turned on with [SENSe:]LIST:POWer:SET. The result is a list of floating point values separated by commas. The unit depends on method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set."""
		response = self._core.io.query_str(f'SENSe:LIST:POWer:RESult?')
		return Conversions.str_to_float(response)
