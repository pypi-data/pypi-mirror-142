from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tolerance:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, tolerance: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:TOLerance \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.tolerance.set(tolerance = 1.0) \n
		This command controls burst search tolerance. \n
			:param tolerance: Range: 1 to 15000, Unit: SYM
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:TOLerance {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:TOLerance \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.burst.tolerance.get() \n
		This command controls burst search tolerance. \n
			:return: tolerance: Range: 1 to 15000, Unit: SYM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:TOLerance?')
		return Conversions.str_to_float(response)
