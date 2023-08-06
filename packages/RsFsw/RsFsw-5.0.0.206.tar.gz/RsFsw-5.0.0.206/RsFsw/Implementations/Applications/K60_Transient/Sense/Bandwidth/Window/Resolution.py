from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolution:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, bandwidth_resolution: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe]:BWIDth[:WINDow<n>]:RESolution \n
		Snippet: driver.applications.k60Transient.sense.bandwidth.window.resolution.set(bandwidth_resolution = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param bandwidth_resolution: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(bandwidth_resolution)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:BWIDth:WINDow{window_cmd_val}:RESolution {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe]:BWIDth[:WINDow<n>]:RESolution \n
		Snippet: value: float = driver.applications.k60Transient.sense.bandwidth.window.resolution.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: bandwidth_resolution: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:BWIDth:WINDow{window_cmd_val}:RESolution?')
		return Conversions.str_to_float(response)
