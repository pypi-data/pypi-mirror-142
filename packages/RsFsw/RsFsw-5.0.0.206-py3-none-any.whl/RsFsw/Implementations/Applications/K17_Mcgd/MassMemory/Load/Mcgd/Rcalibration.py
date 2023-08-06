from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rcalibration:
	"""Rcalibration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcalibration", core, parent)

	def set(self, file: str) -> None:
		"""SCPI: MMEMory:LOAD:MCGD:RCALibration \n
		Snippet: driver.applications.k17Mcgd.massMemory.load.mcgd.rcalibration.set(file = '1') \n
		This command loads the calibration data stored in the selected file and replaces the current data. \n
			:param file: path and file name of the .csv file that contains the calibration data
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'MMEMory:LOAD:MCGD:RCALibration {param}')
