from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:AUTO \n
		Snippet: driver.massMemory.load.auto.set(filename = '1') \n
		This command restores an instrument configuration and defines that configuration as the default state. The default state
		is restored after a preset (*RST) or after you turn on the R&S FSW. \n
			:param filename: 'Factory' Restores the factory settings as the default state. 'file_name String containing the path and name of the configuration file. Note that only instrument settings files can be selected for the startup recall function; channel files cause an error.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write_with_opc(f'MMEMory:LOAD:AUTO 1, {param}')
