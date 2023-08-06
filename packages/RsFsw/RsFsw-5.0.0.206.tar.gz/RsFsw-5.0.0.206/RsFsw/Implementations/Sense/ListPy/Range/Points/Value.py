from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, points: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:POINts[:VALue] \n
		Snippet: driver.sense.listPy.range.points.value.set(points = 1.0, rangePy = repcap.RangePy.Default) \n
		This command defines the number of sweep points in a spurious emission measurement range. The sweep list cannot be
		configured using remote commands during an on-going sweep operation. \n
			:param points: For more information on sweep points see 'How much data is measured: Sweep points and Sweep count'.
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(points)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:POINts:VALue {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:POINts[:VALue] \n
		Snippet: value: float = driver.sense.listPy.range.points.value.get(rangePy = repcap.RangePy.Default) \n
		This command defines the number of sweep points in a spurious emission measurement range. The sweep list cannot be
		configured using remote commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: points: For more information on sweep points see 'How much data is measured: Sweep points and Sweep count'."""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:POINts:VALue?')
		return Conversions.str_to_float(response)
