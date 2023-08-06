from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hysteresis:
	"""Hysteresis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hysteresis", core, parent)

	def set(self, hysteresis: float) -> None:
		"""SCPI: [SENSe]:PMETer:TRIGger:HYSTeresis \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.trigger.hysteresis.set(hysteresis = 1.0) \n
		This command defines the trigger hysteresis for external power triggers. The hysteresis in dB is the value the input
		signal must stay below the IF power trigger level in order to allow a trigger to start the measurement. \n
			:param hysteresis: Range: 3 dB to 50 dB, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(hysteresis)
		self._core.io.write(f'SENSe:PMETer:TRIGger:HYSTeresis {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:TRIGger:HYSTeresis \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.trigger.hysteresis.get() \n
		This command defines the trigger hysteresis for external power triggers. The hysteresis in dB is the value the input
		signal must stay below the IF power trigger level in order to allow a trigger to start the measurement. \n
			:return: hysteresis: Range: 3 dB to 50 dB, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:PMETer:TRIGger:HYSTeresis?')
		return Conversions.str_to_float(response)
