from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Manual:
	"""Manual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("manual", core, parent)

	def set(self, mode: enums.ScalingManualMode, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:MANual \n
		Snippet: driver.applications.k40PhaseNoise.display.window.trace.y.scale.manual.set(mode = enums.ScalingManualMode.BRANge, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the type of manual scaling of the vertical axis. \n
			:param mode: OFF | TBOTtom | TRANge | BRANge OFF Turns manual scaling of the y-axis off. TBOTtom Scaling based on the values on the bottom and top of the diagram. BRANge Scaling based on the value at the bottom of the diagram and the axis range. TRANge Scaling based on the value at the top of the diagram and the axis range.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ScalingManualMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:MANual {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.ScalingManualMode:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:MANual \n
		Snippet: value: enums.ScalingManualMode = driver.applications.k40PhaseNoise.display.window.trace.y.scale.manual.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the type of manual scaling of the vertical axis. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: mode: OFF | TBOTtom | TRANge | BRANge OFF Turns manual scaling of the y-axis off. TBOTtom Scaling based on the values on the bottom and top of the diagram. BRANge Scaling based on the value at the bottom of the diagram and the axis range. TRANge Scaling based on the value at the top of the diagram and the axis range."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:MANual?')
		return Conversions.str_to_scalar_enum(response, enums.ScalingManualMode)
