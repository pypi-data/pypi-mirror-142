from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Show:
	"""Show commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("show", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MSRA:ALINe:SHOW \n
		Snippet: driver.applications.k14Xnr5G.calculate.msra.aline.show.set(state = False, window = repcap.Window.Default) \n
		No command help available \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MSRA:ALINe:SHOW {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:MSRA:ALINe:SHOW \n
		Snippet: value: bool = driver.applications.k14Xnr5G.calculate.msra.aline.show.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MSRA:ALINe:SHOW?')
		return Conversions.str_to_bool(response)
