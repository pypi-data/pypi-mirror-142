from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, range_py: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:SCALe:X:RANGe \n
		Snippet: driver.calculate.statistics.scale.x.range.set(range_py = 1.0, window = repcap.Window.Default) \n
		This command defines the display range of the x-axis for statistical measurements. The effects are identical to method
		RsFsw.Display.Window.Trace.Y.Scale.set. \n
			:param range_py: Range: 1 dB to 200 dB, Unit: dB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(range_py)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:SCALe:X:RANGe {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:STATistics:SCALe:X:RANGe \n
		Snippet: value: float = driver.calculate.statistics.scale.x.range.get(window = repcap.Window.Default) \n
		This command defines the display range of the x-axis for statistical measurements. The effects are identical to method
		RsFsw.Display.Window.Trace.Y.Scale.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: range_py: Range: 1 dB to 200 dB, Unit: dB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:SCALe:X:RANGe?')
		return Conversions.str_to_float(response)
