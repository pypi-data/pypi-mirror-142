from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, time: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TDOMain:X[:SCALe]:DURation \n
		Snippet: driver.applications.k18AmplifierEt.display.window.tdomain.x.scale.duration.set(time = 1.0, window = repcap.Window.Default) \n
		This command defines the amount of data displayed on the x-axis of the time domain result display.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off automatic scaling (method RsFsw.Applications.K18_AmplifierEt.Display.Window.Tdomain.X.Scale.Mode.set) . \n
			:param time: numeric value Time that is displayed on the x-axis, beginning at the offset defined with method RsFsw.Applications.K18_AmplifierEt.Display.Window.Tdomain.X.Scale.Offset.set. Unit: s
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TDOMain:X:SCALe:DURation {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TDOMain:X[:SCALe]:DURation \n
		Snippet: value: float = driver.applications.k18AmplifierEt.display.window.tdomain.x.scale.duration.get(window = repcap.Window.Default) \n
		This command defines the amount of data displayed on the x-axis of the time domain result display.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off automatic scaling (method RsFsw.Applications.K18_AmplifierEt.Display.Window.Tdomain.X.Scale.Mode.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: time: numeric value Time that is displayed on the x-axis, beginning at the offset defined with method RsFsw.Applications.K18_AmplifierEt.Display.Window.Tdomain.X.Scale.Offset.set. Unit: s"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TDOMain:X:SCALe:DURation?')
		return Conversions.str_to_float(response)
