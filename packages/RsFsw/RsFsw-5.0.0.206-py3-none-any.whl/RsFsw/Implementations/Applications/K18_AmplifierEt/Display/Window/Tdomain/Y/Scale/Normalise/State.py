from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TDOMain:Y[:SCALe]:NORMalise[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.display.window.tdomain.y.scale.normalise.state.set(state = False, window = repcap.Window.Default) \n
		This command turns normalization of the results in the time domain result display on and off. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TDOMain:Y:SCALe:NORMalise:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TDOMain:Y[:SCALe]:NORMalise[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.display.window.tdomain.y.scale.normalise.state.get(window = repcap.Window.Default) \n
		This command turns normalization of the results in the time domain result display on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TDOMain:Y:SCALe:NORMalise:STATe?')
		return Conversions.str_to_bool(response)
