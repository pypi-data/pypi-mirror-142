from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, holdoff: float) -> None:
		"""SCPI: [SENSe]:PMETer:TRIGger:HOLDoff \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.trigger.holdoff.set(holdoff = 1.0) \n
		This command defines the trigger holdoff for external power triggers. \n
			:param holdoff: Time period that has to pass between the trigger event and the start of the measurement, in case another trigger event occurs. Range: 0 s to 1 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(holdoff)
		self._core.io.write(f'SENSe:PMETer:TRIGger:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:TRIGger:HOLDoff \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.trigger.holdoff.get() \n
		This command defines the trigger holdoff for external power triggers. \n
			:return: holdoff: Time period that has to pass between the trigger event and the start of the measurement, in case another trigger event occurs. Range: 0 s to 1 s, Unit: S"""
		response = self._core.io.query_str(f'SENSe:PMETer:TRIGger:HOLDoff?')
		return Conversions.str_to_float(response)
