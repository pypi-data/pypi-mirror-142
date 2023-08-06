from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def set(self, stepsize: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP \n
		Snippet: driver.applications.k60Transient.sense.frequency.center.step.set(stepsize = 1.0) \n
		This command defines the center frequency step size. \n
			:param stepsize: fmax is specified in the data sheet. Range: 1 to fMAX, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP \n
		Snippet: value: float = driver.applications.k60Transient.sense.frequency.center.step.get() \n
		This command defines the center frequency step size. \n
			:return: stepsize: fmax is specified in the data sheet. Range: 1 to fMAX, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP?')
		return Conversions.str_to_float(response)
