from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scope:
	"""Scope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scope", core, parent)

	def set(self, scope: enums.ScaleScope, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:SCOPe \n
		Snippet: driver.applications.k40PhaseNoise.display.window.trace.x.scale.scope.set(scope = enums.ScaleScope.HDECades, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the way the application scales the horizontal axis. \n
			:param scope: MRANge | HDECades | MANual MRANge Shows the complete measurement range. HDECade Shows a particular half decade only. You can select a particular half decade with . MANual Shows a custom part of the measurement range. You can select the start and stop offsets with .
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(scope, enums.ScaleScope)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:SCOPe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.ScaleScope:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:SCOPe \n
		Snippet: value: enums.ScaleScope = driver.applications.k40PhaseNoise.display.window.trace.x.scale.scope.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the way the application scales the horizontal axis. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: scope: MRANge | HDECades | MANual MRANge Shows the complete measurement range. HDECade Shows a particular half decade only. You can select a particular half decade with . MANual Shows a custom part of the measurement range. You can select the start and stop offsets with ."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:SCOPe?')
		return Conversions.str_to_scalar_enum(response, enums.ScaleScope)
