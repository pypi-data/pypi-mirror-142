from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	def set(self, frequency: enums.FrequencyType, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe] \n
		Snippet: driver.applications.k30NoiseFigure.display.window.trace.x.scale.set(frequency = enums.FrequencyType.IF, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the type of frequency displayed on the x-axis. \n
			:param frequency: RF | IF | LO IF Intermediary frequency, e.g. for measurements on frequency converting DUTs. RF Radio frequency.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(frequency, enums.FrequencyType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.FrequencyType:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe] \n
		Snippet: value: enums.FrequencyType = driver.applications.k30NoiseFigure.display.window.trace.x.scale.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the type of frequency displayed on the x-axis. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: frequency: RF | IF | LO IF Intermediary frequency, e.g. for measurements on frequency converting DUTs. RF Radio frequency."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe?')
		return Conversions.str_to_scalar_enum(response, enums.FrequencyType)
