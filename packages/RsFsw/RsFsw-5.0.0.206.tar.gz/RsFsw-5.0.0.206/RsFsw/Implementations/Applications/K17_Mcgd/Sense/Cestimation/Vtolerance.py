from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vtolerance:
	"""Vtolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vtolerance", core, parent)

	def set(self, tolerance: float) -> None:
		"""SCPI: [SENSe]:CESTimation:VTOLerance \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.vtolerance.set(tolerance = 1.0) \n
		Defines an additional tolerance to the Max relative Satellite Velocity in %. This information is used to calculate the
		Max Clock Offset. \n
			:param tolerance: numeric value Unit: %
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		self._core.io.write(f'SENSe:CESTimation:VTOLerance {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CESTimation:VTOLerance \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.cestimation.vtolerance.get() \n
		Defines an additional tolerance to the Max relative Satellite Velocity in %. This information is used to calculate the
		Max Clock Offset. \n
			:return: tolerance: numeric value Unit: %"""
		response = self._core.io.query_str(f'SENSe:CESTimation:VTOLerance?')
		return Conversions.str_to_float(response)
