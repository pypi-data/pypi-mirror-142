from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficient:
	"""Coefficient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficient", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:EQUalizer:FILTer:COEFficient \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.load.equalizer.filterPy.coefficient.set(filename = '1') \n
		This command restores an equalizer filter that you have previously saved. \n
			:param filename: String containing the file name and location of the filter (csv file format) .
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:LOAD:EQUalizer:FILTer:COEFficient {param}')
