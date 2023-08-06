from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preset:
	"""Preset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	def set(self, result_type: enums.TracePresetType, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:PRESet \n
		Snippet: driver.applications.k60Transient.display.window.trace.preset.set(result_type = enums.TracePresetType.ALL, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param result_type: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(result_type, enums.TracePresetType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:PRESet {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.TracePresetType:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:PRESet \n
		Snippet: value: enums.TracePresetType = driver.applications.k60Transient.display.window.trace.preset.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: result_type: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:PRESet?')
		return Conversions.str_to_scalar_enum(response, enums.TracePresetType)
