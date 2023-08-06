from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Seconds: float: Number of seconds that have passed since 01.01.1970 till the frame start
			- Nanoseconds: float: Number of nanoseconds that have passed in addition to the Seconds since 01.01.1970 till the frame start.
			- Reserved: float: The third value is reserved for future uses.
			- Reserved_B: float: The third value is reserved for future uses."""
		__meta_args_list = [
			ArgStruct.scalar_float('Seconds'),
			ArgStruct.scalar_float('Nanoseconds'),
			ArgStruct.scalar_float('Reserved'),
			ArgStruct.scalar_float('Reserved_B')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Seconds: float = None
			self.Nanoseconds: float = None
			self.Reserved: float = None
			self.Reserved_B: float = None

	def get(self, frames: enums.SelectionRangeB, window=repcap.Window.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:SPECtrogram:TSTamp:DATA \n
		Snippet: value: GetStruct = driver.calculate.spectrogram.tstamp.data.get(frames = enums.SelectionRangeB.ALL, window = repcap.Window.Default) \n
		This command queries the starting time of the frames. The return values consist of four values for each frame.
		If the Spectrogram is empty, the command returns '0,0,0,0'. The times are given as delta values, which simplifies
		evaluating relative results; however, you can also calculate the absolute date and time as displayed on the screen. The
		frame results themselves are returned with TRAC:DATA? SGR See method RsFsw.Trace.Data.get_. \n
			:param frames: CURRent Returns the starting time of the current frame. ALL Returns the starting time for all frames. The results are sorted in descending order, beginning with the current frame.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(frames, enums.SelectionRangeB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:SPECtrogram:TSTamp:DATA? {param}', self.__class__.GetStruct())
