from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Results:
	"""Results commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("results", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:DATA:RESults \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.data.results.set(state = False, window = repcap.Window.Default) \n
		This command turns automatic determination of the DUT characteristics for the calculation of the uncertainty on and off. \n
			:param state: ON | 1 The application calculates the uncertainty with the DUT characteristics (noise figure, gain and frequency) resulting from the noise figure measurement. OFF | 0 The application calculates the uncertainty with the DUT characteristics (noise figure, gain and frequency) based on the values you have defined manually.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:DATA:RESults {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:UNCertainty:DATA:RESults \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.calculate.uncertainty.data.results.get(window = repcap.Window.Default) \n
		This command turns automatic determination of the DUT characteristics for the calculation of the uncertainty on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | 1 The application calculates the uncertainty with the DUT characteristics (noise figure, gain and frequency) resulting from the noise figure measurement. OFF | 0 The application calculates the uncertainty with the DUT characteristics (noise figure, gain and frequency) based on the values you have defined manually."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:DATA:RESults?')
		return Conversions.str_to_bool(response)
