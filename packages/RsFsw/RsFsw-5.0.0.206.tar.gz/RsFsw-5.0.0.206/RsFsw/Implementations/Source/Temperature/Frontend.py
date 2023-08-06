from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frontend:
	"""Frontend commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frontend", core, parent)

	def get(self) -> float:
		"""SCPI: SOURce:TEMPerature:FRONtend \n
		Snippet: value: float = driver.source.temperature.frontend.get() \n
		This command queries the current frontend temperature of the R&S FSW. During self-alignment, the instrument's (frontend)
		temperature is also measured (as soon as the instrument has warmed up completely) . This temperature is used as a
		reference for a continuous temperature check during operation. If the current temperature deviates from the stored
		self-alignment temperature by a certain degree, a warning is displayed in the status bar indicating the resulting
		deviation in the measured power levels. A status bit in the STATUs:QUEStionable:TEMPerature register indicates a possible
		deviation. \n
			:return: temperature: Temperature in degrees Celsius."""
		response = self._core.io.query_str(f'SOURce:TEMPerature:FRONtend?')
		return Conversions.str_to_float(response)
