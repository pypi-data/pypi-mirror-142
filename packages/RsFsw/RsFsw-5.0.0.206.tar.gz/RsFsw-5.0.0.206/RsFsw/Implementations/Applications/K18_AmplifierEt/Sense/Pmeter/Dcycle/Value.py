from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, percentage: float) -> None:
		"""SCPI: [SENSe]:PMETer:DCYCle:VALue \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.dcycle.value.set(percentage = 1.0) \n
		This command defines the duty cycle for the correction of pulse signals. The power sensor uses the duty cycle in
		combination with the mean power to calculate the power of the pulse. \n
			:param percentage: Range: 0.001 to 99.999, Unit: %
		"""
		param = Conversions.decimal_value_to_str(percentage)
		self._core.io.write(f'SENSe:PMETer:DCYCle:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:DCYCle:VALue \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.dcycle.value.get() \n
		This command defines the duty cycle for the correction of pulse signals. The power sensor uses the duty cycle in
		combination with the mean power to calculate the power of the pulse. \n
			:return: percentage: Range: 0.001 to 99.999, Unit: %"""
		response = self._core.io.query_str(f'SENSe:PMETer:DCYCle:VALue?')
		return Conversions.str_to_float(response)
