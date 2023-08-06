from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer:LINK \n
		Snippet: driver.applications.k60Transient.calculate.marker.link.set(state = False, window = repcap.Window.Default) \n
		If enabled, the markers in all Transient Analysis diagrams - regardless of the x-axis unit - are linked, i.e. when you
		move a marker in one window, the markers in all other windows are moved to the same position in time. Linking is also
		possible across spectrogram and spectrum displays. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer:LINK {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer:LINK \n
		Snippet: value: bool = driver.applications.k60Transient.calculate.marker.link.get(window = repcap.Window.Default) \n
		If enabled, the markers in all Transient Analysis diagrams - regardless of the x-axis unit - are linked, i.e. when you
		move a marker in one window, the markers in all other windows are moved to the same position in time. Linking is also
		possible across spectrogram and spectrum displays. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer:LINK?')
		return Conversions.str_to_bool(response)
