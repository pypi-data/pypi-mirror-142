from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, start: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:THReshold:STARt \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.threshold.start.set(start = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines an absolute threshold that the power level must exceed for a peak to be detected as a true spur. The start value
		must be lower than the stop value. \n
			:param start: Range: -200 dBm to 0 dBm , Unit: DBM
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(start)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:THReshold:STARt {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:THReshold:STARt \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.threshold.start.get(rangePy = repcap.RangePy.Default) \n
		Defines an absolute threshold that the power level must exceed for a peak to be detected as a true spur. The start value
		must be lower than the stop value. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: start: Range: -200 dBm to 0 dBm , Unit: DBM"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:THReshold:STARt?')
		return Conversions.str_to_float(response)
