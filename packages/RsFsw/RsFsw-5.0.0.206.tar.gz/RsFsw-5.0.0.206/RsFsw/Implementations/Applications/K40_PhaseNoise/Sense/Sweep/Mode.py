from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.SweepModePhNoise) -> None:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: driver.applications.k40PhaseNoise.sense.sweep.mode.set(mode = enums.SweepModePhNoise.AVERaged) \n
		This command selects the type of measurement configuration. \n
			:param mode: AVERage Selects a measurement configuration optimized for quality results. FAST Selects a measurement configuration optimized for speed. NORMal Selects a balanced measurement configuration.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModePhNoise)
		self._core.io.write(f'SENSe:SWEep:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepModePhNoise:
		"""SCPI: [SENSe]:SWEep:MODE \n
		Snippet: value: enums.SweepModePhNoise = driver.applications.k40PhaseNoise.sense.sweep.mode.get() \n
		This command selects the type of measurement configuration. \n
			:return: mode: AVERage Selects a measurement configuration optimized for quality results. FAST Selects a measurement configuration optimized for speed. NORMal Selects a balanced measurement configuration."""
		response = self._core.io.query_str(f'SENSe:SWEep:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModePhNoise)
