from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, lower_reference: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:RLEVel:LOWer \n
		Snippet: driver.applications.k40PhaseNoise.display.window.trace.y.scale.refLevel.lower.set(lower_reference = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the reference value or upper border of the diagram area. Note that you have to select manual y-axis
		scaling before you can use the command. \n
			:param lower_reference: Range: -400 to 1, Unit: DBC/HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(lower_reference)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:RLEVel:LOWer {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:RLEVel:LOWer \n
		Snippet: value: float = driver.applications.k40PhaseNoise.display.window.trace.y.scale.refLevel.lower.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the reference value or upper border of the diagram area. Note that you have to select manual y-axis
		scaling before you can use the command. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: lower_reference: Range: -400 to 1, Unit: DBC/HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:RLEVel:LOWer?')
		return Conversions.str_to_float(response)
