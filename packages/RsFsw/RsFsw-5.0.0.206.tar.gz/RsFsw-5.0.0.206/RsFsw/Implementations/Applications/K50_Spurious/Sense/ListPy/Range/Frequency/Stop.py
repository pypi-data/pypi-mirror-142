from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, stop: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>[:FREQuency]:STOP \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.frequency.stop.set(stop = 1.0, rangePy = repcap.RangePy.Default) \n
		This command defines the stop frequency of a wide search measurement range. The stop frequency must be higher than the
		start frequency for the same range. \n
			:param stop: Range: 0 to max. frequency , Unit: HZ
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(stop)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:FREQuency:STOP {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>[:FREQuency]:STOP \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.frequency.stop.get(rangePy = repcap.RangePy.Default) \n
		This command defines the stop frequency of a wide search measurement range. The stop frequency must be higher than the
		start frequency for the same range. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: stop: Range: 0 to max. frequency , Unit: HZ"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:FREQuency:STOP?')
		return Conversions.str_to_float(response)
