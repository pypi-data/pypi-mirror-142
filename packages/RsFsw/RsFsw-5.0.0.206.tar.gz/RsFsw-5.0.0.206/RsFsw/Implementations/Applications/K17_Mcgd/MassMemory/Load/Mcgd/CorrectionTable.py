from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correctionTable", core, parent)

	def set(self, file: str) -> None:
		"""SCPI: MMEMory:LOAD:MCGD:CTABle \n
		Snippet: driver.applications.k17Mcgd.massMemory.load.mcgd.correctionTable.set(file = '1') \n
		Loads a carrier table from a .csv file. Make sure the multi carrier signal description (center frequency, carrier spacing,
		number of carriers) is set appropriate before loading the carrier table. If you have defined a smaller number of carriers
		in the signal description than in the stored .csv file, carrier table information is getting truncated when loading the .
		csv file. \n
			:param file: No help available
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'MMEMory:LOAD:MCGD:CTABle {param}')
