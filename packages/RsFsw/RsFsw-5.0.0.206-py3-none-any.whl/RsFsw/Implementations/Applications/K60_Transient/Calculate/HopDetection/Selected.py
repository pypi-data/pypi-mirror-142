from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Selected:
	"""Selected commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selected", core, parent)

	def set(self, hop_no: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:SELected \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.selected.set(hop_no = 1.0, window = repcap.Window.Default) \n
		Defines or queries the individual hop number in the current sweep for which results are calculated and displayed. \n
			:param hop_no: Hop number
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(hop_no)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:SELected {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:HOPDetection:SELected \n
		Snippet: value: float = driver.applications.k60Transient.calculate.hopDetection.selected.get(window = repcap.Window.Default) \n
		Defines or queries the individual hop number in the current sweep for which results are calculated and displayed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: hop_no: Hop number"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:SELected?')
		return Conversions.str_to_float(response)
