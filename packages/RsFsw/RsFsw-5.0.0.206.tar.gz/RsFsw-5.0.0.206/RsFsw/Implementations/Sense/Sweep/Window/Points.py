from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Points:
	"""Points commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("points", core, parent)

	def set(self, no_points: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe]:SWEep[:WINDow<n>]:POINts \n
		Snippet: driver.sense.sweep.window.points.set(no_points = 1.0, window = repcap.Window.Default) \n
		This command defines the number of sweep points to analyze after a sweep. \n
			:param no_points: Range: 101 to 100001
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(no_points)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:SWEep:WINDow{window_cmd_val}:POINts {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe]:SWEep[:WINDow<n>]:POINts \n
		Snippet: value: float = driver.sense.sweep.window.points.get(window = repcap.Window.Default) \n
		This command defines the number of sweep points to analyze after a sweep. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: no_points: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:SWEep:WINDow{window_cmd_val}:POINts?')
		return Conversions.str_to_float(response)
