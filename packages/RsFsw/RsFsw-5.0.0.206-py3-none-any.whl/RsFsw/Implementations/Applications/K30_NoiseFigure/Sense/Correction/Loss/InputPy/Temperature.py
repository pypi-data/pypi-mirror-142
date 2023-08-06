from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Temperature:
	"""Temperature commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("temperature", core, parent)

	def set(self, temperature: float) -> None:
		"""SCPI: [SENSe]:CORRection:LOSS:INPut:TEMPerature \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.loss.inputPy.temperature.set(temperature = 1.0) \n
		The specified temperature at the time of measurement is considered in the loss calculation. \n
			:param temperature: Unit: K
		"""
		param = Conversions.decimal_value_to_str(temperature)
		self._core.io.write(f'SENSe:CORRection:LOSS:INPut:TEMPerature {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:LOSS:INPut:TEMPerature \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.loss.inputPy.temperature.get() \n
		The specified temperature at the time of measurement is considered in the loss calculation. \n
			:return: temperature: Unit: K"""
		response = self._core.io.query_str(f'SENSe:CORRection:LOSS:INPut:TEMPerature?')
		return Conversions.str_to_float(response)
