from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pexcursion:
	"""Pexcursion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pexcursion", core, parent)

	def set(self, peak_exc: float) -> None:
		"""SCPI: [SENSe]:DIRected:PEXCursion \n
		Snippet: driver.applications.k50Spurious.sense.directed.pexcursion.set(peak_exc = 1.0) \n
		Defines the minimum level value by which the signal must rise or fall after a detected spur so that a new spur is
		detected. \n
			:param peak_exc: Range: 0 to 100, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(peak_exc)
		self._core.io.write(f'SENSe:DIRected:PEXCursion {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:PEXCursion \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.pexcursion.get() \n
		Defines the minimum level value by which the signal must rise or fall after a detected spur so that a new spur is
		detected. \n
			:return: peak_exc: Range: 0 to 100, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:DIRected:PEXCursion?')
		return Conversions.str_to_float(response)
