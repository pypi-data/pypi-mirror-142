from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, gain: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN[:VALue] \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.inputPy.gain.value.set(gain = 1.0, rangePy = repcap.RangePy.Default) \n
		Defines the value of the optional preamplifier (for [SENSe:]LIST:RANGe<ri>:INPut:GAIN:STATeON) . For R&S FSW26 or higher
		models, the input signal is amplified by 30 dB if the preamplifier is activated. For R&S FSW8 or R&S FSW13 models, the
		following settings are available: \n
			:param gain: all values other than 15 dB or 30 dB are rounded to the nearest of the two 15 dB The input signal is amplified by about 15 dB. 30 dB The input signal is amplified by about 30 dB.
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(gain)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:VALue {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN[:VALue] \n
		Snippet: value: float = driver.applications.k50Spurious.sense.listPy.range.inputPy.gain.value.get(rangePy = repcap.RangePy.Default) \n
		Defines the value of the optional preamplifier (for [SENSe:]LIST:RANGe<ri>:INPut:GAIN:STATeON) . For R&S FSW26 or higher
		models, the input signal is amplified by 30 dB if the preamplifier is activated. For R&S FSW8 or R&S FSW13 models, the
		following settings are available: \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: gain: all values other than 15 dB or 30 dB are rounded to the nearest of the two 15 dB The input signal is amplified by about 15 dB. 30 dB The input signal is amplified by about 30 dB."""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:VALue?')
		return Conversions.str_to_float(response)
