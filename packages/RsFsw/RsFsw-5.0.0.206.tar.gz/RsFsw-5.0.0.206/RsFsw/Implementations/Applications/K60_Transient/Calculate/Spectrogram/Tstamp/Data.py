from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Seconds: float: No parameter help available
			- Nanoseconds: float: No parameter help available
			- Reserved: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Seconds'),
			ArgStruct.scalar_float('Nanoseconds'),
			ArgStruct.scalar_float('Reserved')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Seconds: float = None
			self.Nanoseconds: float = None
			self.Reserved: float = None

	def get(self, frames: enums.SelectionRangeB, window=repcap.Window.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:SPECtrogram:TSTamp:DATA \n
		Snippet: value: GetStruct = driver.applications.k60Transient.calculate.spectrogram.tstamp.data.get(frames = enums.SelectionRangeB.ALL, window = repcap.Window.Default) \n
		No command help available \n
			:param frames: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(frames, enums.SelectionRangeB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:SPECtrogram:TSTamp:DATA? {param}', self.__class__.GetStruct())
