from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	def set(self, noise_level: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:PREamp:NOISe \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.preamp.noise.set(noise_level = 1.0, window = repcap.Window.Default) \n
		This command defines the noise level of an external preamplifier that may be part of the test setup. \n
			:param noise_level: Noise level of the preamplifier. Refer to the data sheet of the preamplfier to determine its noise level. Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(noise_level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:PREamp:NOISe {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:PREamp:NOISe \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.preamp.noise.get(window = repcap.Window.Default) \n
		This command defines the noise level of an external preamplifier that may be part of the test setup. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: noise_level: Noise level of the preamplifier. Refer to the data sheet of the preamplfier to determine its noise level. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:PREamp:NOISe?')
		return Conversions.str_to_float(response)
