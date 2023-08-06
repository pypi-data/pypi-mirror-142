from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:PMETer:TRIGger:LEVel \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.trigger.level.set(level = 1.0) \n
		This command defines the trigger level for external power triggers. This command requires the use of a Rohde & Schwarz
		power sensor. For a list of supported sensors see the datasheet. \n
			:param level: -20 to +20 dBm Range: -20 dBm to 20 dBm, Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:PMETer:TRIGger:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:TRIGger:LEVel \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.trigger.level.get() \n
		This command defines the trigger level for external power triggers. This command requires the use of a Rohde & Schwarz
		power sensor. For a list of supported sensors see the datasheet. \n
			:return: level: -20 to +20 dBm Range: -20 dBm to 20 dBm, Unit: DBM"""
		response = self._core.io.query_str(f'SENSe:PMETer:TRIGger:LEVel?')
		return Conversions.str_to_float(response)
