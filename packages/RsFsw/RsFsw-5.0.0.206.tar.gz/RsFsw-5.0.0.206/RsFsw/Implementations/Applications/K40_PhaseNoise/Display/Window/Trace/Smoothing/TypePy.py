from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.TraceSmoothing, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:SMOothing:TYPE \n
		Snippet: driver.applications.k40PhaseNoise.display.window.trace.smoothing.typePy.set(type_py = enums.TraceSmoothing.LINear, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the trace smoothing method. \n
			:param type_py: LINear | LOGarithmic | MEDian LINear Linear smoothing. LOGarithmic Logarithmic smoothing. MEDian Median smoothing.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TraceSmoothing)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:SMOothing:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.TraceSmoothing:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:SMOothing:TYPE \n
		Snippet: value: enums.TraceSmoothing = driver.applications.k40PhaseNoise.display.window.trace.smoothing.typePy.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the trace smoothing method. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: type_py: LINear | LOGarithmic | MEDian LINear Linear smoothing. LOGarithmic Logarithmic smoothing. MEDian Median smoothing."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:SMOothing:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.TraceSmoothing)
