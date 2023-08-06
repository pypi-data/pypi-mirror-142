from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, gain: float) -> None:
		"""SCPI: [SENSe]:DIRected:INPut:GAIN[:VALue] \n
		Snippet: driver.applications.k50Spurious.sense.directed.inputPy.gain.value.set(gain = 1.0) \n
		Defines the gain by the optional preamplifier (if activated for the directed search measurement,
		see [SENSe:]DIRected:INPut:GAIN:STATe) . For R&S FSW26 or higher models, the input signal is amplified by 30 dB if the
		preamplifier is activated. For R&S FSW8 or R&S FSW13 models, different settings are available. \n
			:param gain: 15 dB | 30 dB All other values are rounded to the nearest of these two.
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'SENSe:DIRected:INPut:GAIN:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:INPut:GAIN[:VALue] \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.inputPy.gain.value.get() \n
		Defines the gain by the optional preamplifier (if activated for the directed search measurement,
		see [SENSe:]DIRected:INPut:GAIN:STATe) . For R&S FSW26 or higher models, the input signal is amplified by 30 dB if the
		preamplifier is activated. For R&S FSW8 or R&S FSW13 models, different settings are available. \n
			:return: gain: 15 dB | 30 dB All other values are rounded to the nearest of these two."""
		response = self._core.io.query_str(f'SENSe:DIRected:INPut:GAIN:VALue?')
		return Conversions.str_to_float(response)
