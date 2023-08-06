from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def set(self, mode: enums.SweepModeB) -> None:
		"""SCPI: CONFigure[:UWB]:MEASurement \n
		Snippet: driver.applications.k149Uwb.configure.uwb.measurement.set(mode = enums.SweepModeB.AUTO) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepModeB)
		self._core.io.write(f'CONFigure:UWB:MEASurement {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepModeB:
		"""SCPI: CONFigure[:UWB]:MEASurement \n
		Snippet: value: enums.SweepModeB = driver.applications.k149Uwb.configure.uwb.measurement.get() \n
		No command help available \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement?')
		return Conversions.str_to_scalar_enum(response, enums.SweepModeB)
