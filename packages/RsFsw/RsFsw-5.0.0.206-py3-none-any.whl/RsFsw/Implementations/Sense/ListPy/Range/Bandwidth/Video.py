from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Video:
	"""Video commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("video", core, parent)

	def set(self, vbw: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BANDwidth:VIDeo \n
		Snippet: driver.sense.listPy.range.bandwidth.video.set(vbw = 1.0, rangePy = repcap.RangePy.Default) \n
		This command defines the video bandwidth for a spurious emission measurement range. The sweep list cannot be configured
		using remote commands during an on-going sweep operation. \n
			:param vbw: Video bandwidth. Refer to the data sheet for available video bandwidths. Unit: Hz
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(vbw)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BANDwidth:VIDeo {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:BANDwidth:VIDeo \n
		Snippet: value: float = driver.sense.listPy.range.bandwidth.video.get(rangePy = repcap.RangePy.Default) \n
		This command defines the video bandwidth for a spurious emission measurement range. The sweep list cannot be configured
		using remote commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: vbw: Video bandwidth. Refer to the data sheet for available video bandwidths. Unit: Hz"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:BANDwidth:VIDeo?')
		return Conversions.str_to_float(response)
