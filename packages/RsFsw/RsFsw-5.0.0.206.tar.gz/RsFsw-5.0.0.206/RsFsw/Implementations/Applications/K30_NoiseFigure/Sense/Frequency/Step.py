from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def set(self, stepsize: float) -> None:
		"""SCPI: [SENSe]:FREQuency:STEP \n
		Snippet: driver.applications.k30NoiseFigure.sense.frequency.step.set(stepsize = 1.0) \n
		This command defines the frequency stepsize in the frequency table. The stepsize corresponds to the distance from one
		measurement point to another. If you change the stepsize, the application creates a new frequency list. \n
			:param stepsize: Range: 0 Hz to span, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'SENSe:FREQuency:STEP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:STEP \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.frequency.step.get() \n
		This command defines the frequency stepsize in the frequency table. The stepsize corresponds to the distance from one
		measurement point to another. If you change the stepsize, the application creates a new frequency list. \n
			:return: stepsize: Range: 0 Hz to span, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:STEP?')
		return Conversions.str_to_float(response)
