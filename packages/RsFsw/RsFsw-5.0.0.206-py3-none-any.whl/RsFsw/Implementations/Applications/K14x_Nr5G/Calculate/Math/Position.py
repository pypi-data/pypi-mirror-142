from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Position:
	"""Position commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def set(self, position: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MATH:POSition \n
		Snippet: driver.applications.k14Xnr5G.calculate.math.position.set(position = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param position: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(position)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MATH:POSition {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:MATH:POSition \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.math.position.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: position: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MATH:POSition?')
		return Conversions.str_to_float(response)
