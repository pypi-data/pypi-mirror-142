from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ratio:
	"""Ratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ratio", core, parent)

	def set(self, ratio: float) -> None:
		"""SCPI: [SENSe]:LIST:BWIDth[:RESolution]:RATio \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.bandwidth.resolution.ratio.set(ratio = 1.0) \n
		This command defines the resolution bandwidth over all half decades. \n
			:param ratio: Numeric value in %. The resulting RBW is the percentage of the start frequency of each half decade. If the resulting RBW is not available, the application rounds to the next available bandwidth. Range: 1 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SENSe:LIST:BWIDth:RESolution:RATio {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:LIST:BWIDth[:RESolution]:RATio \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.listPy.bandwidth.resolution.ratio.get() \n
		This command defines the resolution bandwidth over all half decades. \n
			:return: ratio: Numeric value in %. The resulting RBW is the percentage of the start frequency of each half decade. If the resulting RBW is not available, the application rounds to the next available bandwidth. Range: 1 to 100, Unit: PCT"""
		response = self._core.io.query_str(f'SENSe:LIST:BWIDth:RESolution:RATio?')
		return Conversions.str_to_float(response)
