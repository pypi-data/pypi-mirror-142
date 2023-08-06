from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:AUTO \n
		Snippet: driver.applications.k60Transient.display.window.trace.y.scale.auto.set(state = False, window = repcap.Window.Default) \n
		If enabled, the Y-axis is scaled automatically according to the current measurement. \n
			:param state: OFF Switch the function off ON Switch the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:AUTO {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:AUTO \n
		Snippet: value: bool = driver.applications.k60Transient.display.window.trace.y.scale.auto.get(window = repcap.Window.Default) \n
		If enabled, the Y-axis is scaled automatically according to the current measurement. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: OFF Switch the function off ON Switch the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:AUTO?')
		return Conversions.str_to_bool(response)
