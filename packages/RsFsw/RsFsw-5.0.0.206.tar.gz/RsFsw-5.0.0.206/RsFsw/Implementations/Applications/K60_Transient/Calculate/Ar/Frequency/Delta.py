from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delta:
	"""Delta commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delta", core, parent)

	def set(self, frequency: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:AR:FREQuency:DELTa \n
		Snippet: driver.applications.k60Transient.calculate.ar.frequency.delta.set(frequency = 1.0, window = repcap.Window.Default) \n
		Defines the center of the frequency span for the analysis region. It is defined as an offset from the center frequency. \n
			:param frequency: Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:AR:FREQuency:DELTa {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:AR:FREQuency:DELTa \n
		Snippet: value: float = driver.applications.k60Transient.calculate.ar.frequency.delta.get(window = repcap.Window.Default) \n
		Defines the center of the frequency span for the analysis region. It is defined as an offset from the center frequency. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: frequency: Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:AR:FREQuency:DELTa?')
		return Conversions.str_to_float(response)
