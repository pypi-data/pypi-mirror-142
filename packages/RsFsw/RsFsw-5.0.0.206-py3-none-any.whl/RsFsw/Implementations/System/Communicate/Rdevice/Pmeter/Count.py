from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: SYSTem:COMMunicate:RDEVice:PMETer<p>:COUNt \n
		Snippet: value: float = driver.system.communicate.rdevice.pmeter.count.get(powerMeter = repcap.PowerMeter.Default) \n
		This command queries the number of power sensors currently connected to the R&S FSW. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: number_sensors: Number of connected power sensors."""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:PMETer{powerMeter_cmd_val}:COUNt?')
		return Conversions.str_to_float(response)
