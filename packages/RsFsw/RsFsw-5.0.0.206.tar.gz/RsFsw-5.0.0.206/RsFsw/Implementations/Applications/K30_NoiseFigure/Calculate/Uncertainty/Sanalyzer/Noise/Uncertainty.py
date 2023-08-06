from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uncertainty:
	"""Uncertainty commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uncertainty", core, parent)

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:SANalyzer:NOISe:UNCertainty \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.sanalyzer.noise.uncertainty.get(window = repcap.Window.Default) \n
		This command queries the uncertainty value of the spectrum analyzer's internal noise. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: uncertainty: Noise figure uncertainty of the spectrum analyzer in dB. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:SANalyzer:NOISe:UNCertainty?')
		return Conversions.str_to_float(response)
