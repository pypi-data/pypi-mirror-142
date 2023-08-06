from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Time_X_1: float: absolute position in time of the n dB marker to the left of the reference marker in seconds
			- Time_X_2: float: absolute position in time of the n dB marker to the right of the reference marker in seconds"""
		__meta_args_list = [
			ArgStruct.scalar_float('Time_X_1'),
			ArgStruct.scalar_float('Time_X_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Time_X_1: float = None
			self.Time_X_2: float = None

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:NDBDown:TIME \n
		Snippet: value: GetStruct = driver.calculate.marker.function.ndbDown.time.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the position of the n dB down markers on the x-axis when measuring in the time domain.
		To get a valid result, you have to perform a complete measurement with synchronization to the end of the measurement
		before reading out the result. This is only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.
		Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:NDBDown:TIME?', self.__class__.GetStruct())
