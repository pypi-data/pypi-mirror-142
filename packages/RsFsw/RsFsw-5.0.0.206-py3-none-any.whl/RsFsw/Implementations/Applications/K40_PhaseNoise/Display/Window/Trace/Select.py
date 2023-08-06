from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, trace_number: int, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:SELect \n
		Snippet: driver.applications.k40PhaseNoise.display.window.trace.select.set(trace_number = 1, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the trace for which spot noise results are calculated. A trace can only be selected if it has been
		turned on ('Trace Mode' ≠ Blank) . \n
			:param trace_number: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(trace_number)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:SELect {param}')
