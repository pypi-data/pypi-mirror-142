from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:DATA:FREQuency \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.data.frequency.set(frequency = 1.0, window = repcap.Window.Default) \n
		This command defines the frequency for which the uncertainty should be calculated. This command is available if you have
		turned automatic determination of the DUT characteristics off withmethod RsFsw.Applications.K30_NoiseFigure.Calculate.
		Uncertainty.Data.Frequency.set . \n
			:param frequency: Frequency of the DUT. Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:DATA:FREQuency {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:DATA:FREQuency \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.data.frequency.get(window = repcap.Window.Default) \n
		This command defines the frequency for which the uncertainty should be calculated. This command is available if you have
		turned automatic determination of the DUT characteristics off withmethod RsFsw.Applications.K30_NoiseFigure.Calculate.
		Uncertainty.Data.Frequency.set . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: frequency: Frequency of the DUT. Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:DATA:FREQuency?')
		return Conversions.str_to_float(response)
