from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def set(self, gain: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNCertainty:PREamp:GAIN \n
		Snippet: driver.applications.k30NoiseFigure.calculate.uncertainty.preamp.gain.set(gain = 1.0, window = repcap.Window.Default) \n
		This command define the gain of an external preamplifier that may be part of the test setup. \n
			:param gain: Gain of the preamplifier. Refer to the data sheet of the preamplifier to determine its gain. Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(gain)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNCertainty:PREamp:GAIN {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:UNCertainty:PREamp:GAIN \n
		Snippet: value: float = driver.applications.k30NoiseFigure.calculate.uncertainty.preamp.gain.get(window = repcap.Window.Default) \n
		This command define the gain of an external preamplifier that may be part of the test setup. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: gain: Gain of the preamplifier. Refer to the data sheet of the preamplifier to determine its gain. Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNCertainty:PREamp:GAIN?')
		return Conversions.str_to_float(response)
