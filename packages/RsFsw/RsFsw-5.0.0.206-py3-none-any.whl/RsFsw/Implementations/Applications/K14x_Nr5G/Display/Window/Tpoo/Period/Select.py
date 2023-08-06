from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, period_number: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TPOO:PERiod:SELect \n
		Snippet: driver.applications.k14Xnr5G.display.window.tpoo.period.select.set(period_number = 1.0, window = repcap.Window.Default) \n
		This command selects the period to display the rising or falling edge in the on / off power measurement. \n
			:param period_number: Window
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(period_number)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TPOO:PERiod:SELect {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TPOO:PERiod:SELect \n
		Snippet: value: float = driver.applications.k14Xnr5G.display.window.tpoo.period.select.get(window = repcap.Window.Default) \n
		This command selects the period to display the rising or falling edge in the on / off power measurement. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: period_number: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TPOO:PERiod:SELect?')
		return Conversions.str_to_float(response)
