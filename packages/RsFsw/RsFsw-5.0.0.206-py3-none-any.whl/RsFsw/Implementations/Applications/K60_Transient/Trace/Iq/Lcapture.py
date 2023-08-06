from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lcapture:
	"""Lcapture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcapture", core, parent)

	def set(self, display_mode: enums.AutoMode, window=repcap.Window.Default) -> None:
		"""SCPI: TRACe<n>:IQ:LCAPture \n
		Snippet: driver.applications.k60Transient.trace.iq.lcapture.set(display_mode = enums.AutoMode.AUTO, window = repcap.Window.Default) \n
		The long capture buffer provides functionality to use the full I/Q memory depth of the R&S FSW for data acquisition. \n
			:param display_mode: AUTO | ON | OFF AUTO The long capture buffer is activated in case that the record length exceeds the amount of data which can be acquired within the standard memory capacity of the R&S FSW. If the record length decreases again, the long capture buffer is deactivated automatically. ON The long capture buffer is activated permanently. A data capture in a different measurement channel will overwrite and invalidate the acquired I/Q data. A red 'IQ' icon in the channel tab indicates that the results for the channel no longer match the data currently in the capture buffer. OFF This is the default setting. Only the standard I/Q memory capacity of the R&S FSW is used. The available I/Q memory capacity is shared by all measurement channels.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(display_mode, enums.AutoMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'TRACe{window_cmd_val}:IQ:LCAPture {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AutoMode:
		"""SCPI: TRACe<n>:IQ:LCAPture \n
		Snippet: value: enums.AutoMode = driver.applications.k60Transient.trace.iq.lcapture.get(window = repcap.Window.Default) \n
		The long capture buffer provides functionality to use the full I/Q memory depth of the R&S FSW for data acquisition. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: display_mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:IQ:LCAPture?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
