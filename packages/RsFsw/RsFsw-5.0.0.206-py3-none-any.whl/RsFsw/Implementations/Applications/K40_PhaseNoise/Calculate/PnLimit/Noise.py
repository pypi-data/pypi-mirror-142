from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	def set(self, noise_level: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PNLimit:NOISe \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.noise.set(noise_level = 1.0, window = repcap.Window.Default) \n
		This command defines the noise floor level of the DUT. The noise floor level is necessary for the calculation of a phase
		noise limit line. \n
			:param noise_level: Range: -200 to 200, Unit: dBm/Hz
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(noise_level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PNLimit:NOISe {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PNLimit:NOISe \n
		Snippet: value: float = driver.applications.k40PhaseNoise.calculate.pnLimit.noise.get(window = repcap.Window.Default) \n
		This command defines the noise floor level of the DUT. The noise floor level is necessary for the calculation of a phase
		noise limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: noise_level: Range: -200 to 200, Unit: dBm/Hz"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PNLimit:NOISe?')
		return Conversions.str_to_float(response)
