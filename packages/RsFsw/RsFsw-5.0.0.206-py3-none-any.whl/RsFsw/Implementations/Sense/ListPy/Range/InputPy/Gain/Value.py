from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, gain: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN[:VALue] \n
		Snippet: driver.sense.listPy.range.inputPy.gain.value.set(gain = 1.0, rangePy = repcap.RangePy.Default) \n
		This command selects the preamplification level for the range. The command requires option R&S FSW-B24. The sweep list
		cannot be configured using remote commands during an on-going sweep operation. \n
			:param gain: 15 dB | 30 dB The availability of preamplification levels depends on the R&S FSW model. •R&S FSW8/13: 15dB and 30 dB •R&S FSW26 or higher: 30 dB All other values are rounded to the nearest of these two.
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(gain)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:VALue {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INPut:GAIN[:VALue] \n
		Snippet: value: float = driver.sense.listPy.range.inputPy.gain.value.get(rangePy = repcap.RangePy.Default) \n
		This command selects the preamplification level for the range. The command requires option R&S FSW-B24. The sweep list
		cannot be configured using remote commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: gain: 15 dB | 30 dB The availability of preamplification levels depends on the R&S FSW model. •R&S FSW8/13: 15dB and 30 dB •R&S FSW26 or higher: 30 dB All other values are rounded to the nearest of these two."""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INPut:GAIN:VALue?')
		return Conversions.str_to_float(response)
