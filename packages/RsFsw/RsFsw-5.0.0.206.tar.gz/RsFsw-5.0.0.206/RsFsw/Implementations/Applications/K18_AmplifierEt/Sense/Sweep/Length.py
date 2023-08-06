from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, samples: float) -> None:
		"""SCPI: [SENSe]:SWEep:LENGth \n
		Snippet: driver.applications.k18AmplifierEt.sense.sweep.length.set(samples = 1.0) \n
		This command defines the capture length.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off automatic selection of the capture time ([SENSe:]SWEep:TIME:AUTO) .
			INTRO_CMD_HELP: Effects of this command \n
			- Changing the capture length automatically adjusts the capture time. \n
			:param samples: numeric value: (integer only) Unit: Samples
		"""
		param = Conversions.decimal_value_to_str(samples)
		self._core.io.write(f'SENSe:SWEep:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:LENGth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.sweep.length.get() \n
		This command defines the capture length.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn off automatic selection of the capture time ([SENSe:]SWEep:TIME:AUTO) .
			INTRO_CMD_HELP: Effects of this command \n
			- Changing the capture length automatically adjusts the capture time. \n
			:return: samples: numeric value: (integer only) Unit: Samples"""
		response = self._core.io.query_str(f'SENSe:SWEep:LENGth?')
		return Conversions.str_to_float(response)
