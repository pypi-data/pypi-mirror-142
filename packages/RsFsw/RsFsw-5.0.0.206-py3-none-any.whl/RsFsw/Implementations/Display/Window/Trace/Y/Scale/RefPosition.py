from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefPosition:
	"""RefPosition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refPosition", core, parent)

	def set(self, position: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:RPOSition \n
		Snippet: driver.display.window.trace.y.scale.refPosition.set(position = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the vertical position of the reference level on the display grid (for all traces) . The R&S FSW
		adjusts the scaling of the y-axis accordingly. For measurements with the optional external generator control, the command
		defines the position of the reference value. \n
			:param position: 0 PCT corresponds to the lower display border, 100% corresponds to the upper display border. Unit: PCT
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(position)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:RPOSition {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:RPOSition \n
		Snippet: value: float = driver.display.window.trace.y.scale.refPosition.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the vertical position of the reference level on the display grid (for all traces) . The R&S FSW
		adjusts the scaling of the y-axis accordingly. For measurements with the optional external generator control, the command
		defines the position of the reference value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: position: 0 PCT corresponds to the lower display border, 100% corresponds to the upper display border. Unit: PCT"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:RPOSition?')
		return Conversions.str_to_float(response)
