from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def set(self, freq_range: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN[:MAXimum] \n
		Snippet: driver.sense.ademod.spectrum.span.maximum.set(freq_range = 1.0) \n
		Sets the DBW to the specified value and the span (around the center frequency) of the RF data to be evaluated to its new
		maximum (the demodulation bandwidth) . \n
			:param freq_range: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(freq_range)
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:SPAN:MAXimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN[:MAXimum] \n
		Snippet: value: float = driver.sense.ademod.spectrum.span.maximum.get() \n
		Sets the DBW to the specified value and the span (around the center frequency) of the RF data to be evaluated to its new
		maximum (the demodulation bandwidth) . \n
			:return: freq_range: Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SPECtrum:SPAN:MAXimum?')
		return Conversions.str_to_float(response)
