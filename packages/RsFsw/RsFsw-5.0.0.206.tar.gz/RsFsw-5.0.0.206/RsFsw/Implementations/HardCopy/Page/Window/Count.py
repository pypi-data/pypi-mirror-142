from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, arg_0: float, window=repcap.Window.Default) -> None:
		"""SCPI: HCOPy:PAGE:WINDow<1|2>:COUNt \n
		Snippet: driver.hardCopy.page.window.count.set(arg_0 = 1.0, window = repcap.Window.Default) \n
		This command defines how many windows are displayed on a single page of the printout for method RsFsw.HardCopy.Content.
		set. \n
			:param arg_0: integer
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'HCOPy:PAGE:WINDow{window_cmd_val}:COUNt {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: HCOPy:PAGE:WINDow<1|2>:COUNt \n
		Snippet: value: float = driver.hardCopy.page.window.count.get(window = repcap.Window.Default) \n
		This command defines how many windows are displayed on a single page of the printout for method RsFsw.HardCopy.Content.
		set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: arg_0: integer"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'HCOPy:PAGE:WINDow{window_cmd_val}:COUNt?')
		return Conversions.str_to_float(response)
