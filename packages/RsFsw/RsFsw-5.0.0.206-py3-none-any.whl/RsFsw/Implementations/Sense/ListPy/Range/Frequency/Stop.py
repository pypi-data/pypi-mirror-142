from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, frequency: float, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>[:FREQuency]:STOP \n
		Snippet: driver.sense.listPy.range.frequency.stop.set(frequency = 1.0, rangePy = repcap.RangePy.Default) \n
		This command defines the stop frequency of a spurious emission measurement range. Make sure to set an appropriate span.
		If you set a span that is
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- smaller than the span the sweep list covers, the R&S FSW will not measure the ranges that are outside the span - results may be invalid.
			- greater than the span the sweep list covers, the R&S FSW will adjust the start frequency of the first range and the stop frequency of the last range to the span
		For more information see'Spurious emissions measurement' . \n
			:param frequency: Numeric value. Unit: Hz
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:FREQuency:STOP {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:LIST:RANGe<ri>[:FREQuency]:STOP \n
		Snippet: value: float = driver.sense.listPy.range.frequency.stop.get(rangePy = repcap.RangePy.Default) \n
		This command defines the stop frequency of a spurious emission measurement range. Make sure to set an appropriate span.
		If you set a span that is
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- smaller than the span the sweep list covers, the R&S FSW will not measure the ranges that are outside the span - results may be invalid.
			- greater than the span the sweep list covers, the R&S FSW will adjust the start frequency of the first range and the stop frequency of the last range to the span
		For more information see'Spurious emissions measurement' . \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: frequency: Numeric value. Unit: Hz"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:FREQuency:STOP?')
		return Conversions.str_to_float(response)
