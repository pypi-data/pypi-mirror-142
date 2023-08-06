from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsamples:
	"""Nsamples commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsamples", core, parent)

	def set(self, samples: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:NSAMples \n
		Snippet: driver.calculate.statistics.nsamples.set(samples = 1.0, window = repcap.Window.Default) \n
		This command defines the number of samples included in the analysis of statistical measurement functions. \n
			:param samples: Range: Min: 100, Max: depends on the RBW filter
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(samples)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:NSAMples {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:STATistics:NSAMples \n
		Snippet: value: float = driver.calculate.statistics.nsamples.get(window = repcap.Window.Default) \n
		This command defines the number of samples included in the analysis of statistical measurement functions. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: samples: Range: Min: 100, Max: depends on the RBW filter"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:NSAMples?')
		return Conversions.str_to_float(response)
