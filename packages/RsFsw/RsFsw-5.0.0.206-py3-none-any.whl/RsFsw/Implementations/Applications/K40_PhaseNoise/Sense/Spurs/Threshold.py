from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:SPURs:THReshold \n
		Snippet: driver.applications.k40PhaseNoise.sense.spurs.threshold.set(threshold = 1.0) \n
		This command defines the level threshold for spur removal. \n
			:param threshold: Range: 0 to 50, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:SPURs:THReshold {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SPURs:THReshold \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.spurs.threshold.get() \n
		This command defines the level threshold for spur removal. \n
			:return: threshold: Range: 0 to 50, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:SPURs:THReshold?')
		return Conversions.str_to_float(response)
