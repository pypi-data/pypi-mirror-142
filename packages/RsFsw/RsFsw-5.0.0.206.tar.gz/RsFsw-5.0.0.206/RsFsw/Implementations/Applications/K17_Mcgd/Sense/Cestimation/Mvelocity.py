from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mvelocity:
	"""Mvelocity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mvelocity", core, parent)

	def set(self, max_rel_velocity: float) -> None:
		"""SCPI: [SENSe]:CESTimation:MVELocity \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.mvelocity.set(max_rel_velocity = 1.0) \n
		Defines the relative velocity between ground station and satellite in m/s. This information is used to calculate the Max
		Clock Offset. \n
			:param max_rel_velocity: numeric value Unit: m/s
		"""
		param = Conversions.decimal_value_to_str(max_rel_velocity)
		self._core.io.write(f'SENSe:CESTimation:MVELocity {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CESTimation:MVELocity \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.cestimation.mvelocity.get() \n
		Defines the relative velocity between ground station and satellite in m/s. This information is used to calculate the Max
		Clock Offset. \n
			:return: max_rel_velocity: numeric value Unit: m/s"""
		response = self._core.io.query_str(f'SENSe:CESTimation:MVELocity?')
		return Conversions.str_to_float(response)
