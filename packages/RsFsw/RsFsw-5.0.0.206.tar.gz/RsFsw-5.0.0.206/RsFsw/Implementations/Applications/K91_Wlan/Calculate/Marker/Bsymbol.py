from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bsymbol:
	"""Bsymbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsymbol", core, parent)

	def set(self, ppdu: float, symbol: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:BSYMbol \n
		Snippet: driver.applications.k91Wlan.calculate.marker.bsymbol.set(ppdu = 1.0, symbol = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		No command help available \n
			:param ppdu: No help available
			:param symbol: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ppdu', ppdu, DataType.Float), ArgSingle('symbol', symbol, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:BSYMbol {param}'.rstrip())

	# noinspection PyTypeChecker
	class BsymbolStruct(StructBase):
		"""Response structure. Fields: \n
			- Ppdu: float: No parameter help available
			- Symbol: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ppdu'),
			ArgStruct.scalar_float('Symbol')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ppdu: float = None
			self.Symbol: float = None

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> BsymbolStruct:
		"""SCPI: CALCulate<n>:MARKer<m>:BSYMbol \n
		Snippet: value: BsymbolStruct = driver.applications.k91Wlan.calculate.marker.bsymbol.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: structure: for return value, see the help for BsymbolStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:BSYMbol?', self.__class__.BsymbolStruct())
