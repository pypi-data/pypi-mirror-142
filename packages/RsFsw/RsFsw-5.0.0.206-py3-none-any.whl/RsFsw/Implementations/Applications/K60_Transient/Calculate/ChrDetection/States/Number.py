from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Number:
	"""Number commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("number", core, parent)

	def get(self, window=repcap.Window.Default) -> int:
		"""SCPI: CALCulate<n>:CHRDetection:STATes:NUMBer \n
		Snippet: value: int = driver.applications.k60Transient.calculate.chrDetection.states.number.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: states: Range: 0 to 1000"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:CHRDetection:STATes:NUMBer?')
		return Conversions.str_to_int(response)
