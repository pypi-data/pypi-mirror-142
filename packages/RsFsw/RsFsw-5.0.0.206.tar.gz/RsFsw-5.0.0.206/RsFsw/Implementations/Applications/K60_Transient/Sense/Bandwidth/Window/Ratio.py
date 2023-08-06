from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ratio:
	"""Ratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ratio", core, parent)

	def set(self, bandwidth_ratio: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe]:BWIDth[:WINDow<n>]:RATio \n
		Snippet: driver.applications.k60Transient.sense.bandwidth.window.ratio.set(bandwidth_ratio = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param bandwidth_ratio: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(bandwidth_ratio)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:BWIDth:WINDow{window_cmd_val}:RATio {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe]:BWIDth[:WINDow<n>]:RATio \n
		Snippet: value: float = driver.applications.k60Transient.sense.bandwidth.window.ratio.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: bandwidth_ratio: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:BWIDth:WINDow{window_cmd_val}:RATio?')
		return Conversions.str_to_float(response)
