from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, minimum: float) -> None:
		"""SCPI: [SENSe]:DETect:BURSt:LENGth:MINimum \n
		Snippet: driver.applications.k149Uwb.sense.detect.burst.length.minimum.set(minimum = 1.0) \n
		Defines the minimum burst length. \n
			:param minimum: numeric value
		"""
		param = Conversions.decimal_value_to_str(minimum)
		self._core.io.write(f'SENSe:DETect:BURSt:LENGth:MINimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:BURSt:LENGth:MINimum \n
		Snippet: value: float = driver.applications.k149Uwb.sense.detect.burst.length.minimum.get() \n
		Defines the minimum burst length. \n
			:return: minimum: numeric value"""
		response = self._core.io.query_str(f'SENSe:DETect:BURSt:LENGth:MINimum?')
		return Conversions.str_to_float(response)
