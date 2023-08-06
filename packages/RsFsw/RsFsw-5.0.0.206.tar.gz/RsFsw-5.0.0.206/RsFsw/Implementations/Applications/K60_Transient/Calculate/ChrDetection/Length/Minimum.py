from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, time: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:LENGth:MINimum \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.length.minimum.set(time = 1.0, window = repcap.Window.Default) \n
		Defines the minimum chirp length for detection. \n
			:param time: Range: 0.000000251 to 0.00035, Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:LENGth:MINimum {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:CHRDetection:LENGth:MINimum \n
		Snippet: value: float = driver.applications.k60Transient.calculate.chrDetection.length.minimum.get(window = repcap.Window.Default) \n
		Defines the minimum chirp length for detection. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: time: Range: 0.000000251 to 0.00035, Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:CHRDetection:LENGth:MINimum?')
		return Conversions.str_to_float(response)
