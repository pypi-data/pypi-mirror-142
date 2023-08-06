from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tolerance:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:POWer:RLEVel:VERify:TOLerance \n
		Snippet: driver.applications.k40PhaseNoise.sense.power.refLevel.verify.tolerance.set(level = 1.0) \n
		This command defines a relative level tolerance for level verification \n
			:param level: Numeric value in dB, relative to the nominal level. Unit: DB
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:POWer:RLEVel:VERify:TOLerance {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:RLEVel:VERify:TOLerance \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.power.refLevel.verify.tolerance.get() \n
		This command defines a relative level tolerance for level verification \n
			:return: level: Numeric value in dB, relative to the nominal level. Unit: DB"""
		response = self._core.io.query_str(f'SENSe:POWer:RLEVel:VERify:TOLerance?')
		return Conversions.str_to_float(response)
