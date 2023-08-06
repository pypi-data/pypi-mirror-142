from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, level: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:LIMit:STARt \n
		Snippet: driver.sense.listPy.range.limit.start.set(level = 1.0, rangePy = repcap.RangePy.Default) \n
		This command defines an absolute limit for a spurious emission measurement range. The sweep list cannot be configured
		using remote commands during an on-going sweep operation. \n
			:param level: Absolute limit at the start frequency of a SEM range. Range: -400 to 400, Unit: dBm
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(level)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:LIMit:STARt {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:LIMit:STARt \n
		Snippet: value: float = driver.sense.listPy.range.limit.start.get(rangePy = repcap.RangePy.Default) \n
		This command defines an absolute limit for a spurious emission measurement range. The sweep list cannot be configured
		using remote commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: level: Absolute limit at the start frequency of a SEM range. Range: -400 to 400, Unit: dBm"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:LIMit:STARt?')
		return Conversions.str_to_float(response)
