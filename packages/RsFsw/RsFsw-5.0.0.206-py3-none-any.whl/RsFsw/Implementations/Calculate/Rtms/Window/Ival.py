from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ival:
	"""Ival commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ival", core, parent)

	# noinspection PyTypeChecker
	class TimeSpan(StructBase):
		"""Response structure. Fields: \n
			- Start: float: No parameter help available
			- Stop: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Start'),
			ArgStruct.scalar_float('Stop')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start: float = None
			self.Stop: float = None

	def get(self, stimulus: float, window=repcap.Window.Default) -> TimeSpan:
		"""SCPI: CALCulate<n>:RTMS:WINDow:IVAL \n
		Snippet: value: TimeSpan = driver.calculate.rtms.window.ival.get(stimulus = 1.0, window = repcap.Window.Default) \n
		Returns the current analysis interval for applications in MSRT operating mode. \n
			:param stimulus: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for TimeSpan structure arguments."""
		param = Conversions.decimal_value_to_str(stimulus)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:RTMS:WINDow:IVAL? {param}', self.__class__.TimeSpan())
