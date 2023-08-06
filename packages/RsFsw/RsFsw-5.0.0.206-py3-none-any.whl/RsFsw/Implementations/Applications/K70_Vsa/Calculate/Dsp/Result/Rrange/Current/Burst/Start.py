from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def get(self, window=repcap.Window.Default) -> int:
		"""SCPI: CALCulate<n>:DSP:RESult:RRANge:CURRent:BURSt:STARt \n
		Snippet: value: int = driver.applications.k70Vsa.calculate.dsp.result.rrange.current.burst.start.get(window = repcap.Window.Default) \n
		Queries the burst start in the current result range as an offset to the capture buffer start. Tip: To determine the
		capture buffer start, use the method RsFsw.Applications.K40_PhaseNoise.Display.Window.Trace.X.Scale.Start.set command for
		a window with a capture buffer display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: start: Offset in symbols from the capture buffer start. Unit: sym"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DSP:RESult:RRANge:CURRent:BURSt:STARt?')
		return Conversions.str_to_int(response)
