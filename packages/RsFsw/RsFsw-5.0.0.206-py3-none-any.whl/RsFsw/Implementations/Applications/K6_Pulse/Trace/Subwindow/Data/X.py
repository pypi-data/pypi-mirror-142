from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def get(self, trace: enums.TraceTypeNumeric, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> str:
		"""SCPI: TRACe<n>[:SUBWindow<w>][:DATA]:X \n
		Snippet: value: str = driver.applications.k6Pulse.trace.subwindow.data.x.get(trace = enums.TraceTypeNumeric.TRACe1, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		No command help available \n
			:param trace: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:return: data: No help available"""
		param = Conversions.enum_scalar_to_str(trace, enums.TraceTypeNumeric)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:SUBWindow{subWindow_cmd_val}:DATA:X? {param}')
		return trim_str_response(response)
