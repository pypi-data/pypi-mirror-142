from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:DEModsetting:ALL \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.demodSetting.all.set(filename = '1') \n
		This command restores the signal description of multiple carriers from a single file. \n
			:param filename: String containing the path and name of the file. The file extension is .ccallocation.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:LOAD:DEModsetting:ALL {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:LOAD:DEModsetting:ALL \n
		Snippet: value: str = driver.applications.k14Xnr5G.massMemory.load.demodSetting.all.get() \n
		This command restores the signal description of multiple carriers from a single file. \n
			:return: filename: String containing the path and name of the file. The file extension is .ccallocation."""
		response = self._core.io.query_str(f'MMEMory:LOAD:DEModsetting:ALL?')
		return trim_str_response(response)
