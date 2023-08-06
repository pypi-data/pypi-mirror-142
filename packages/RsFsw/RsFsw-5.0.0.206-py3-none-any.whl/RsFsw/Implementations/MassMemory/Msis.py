from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msis:
	"""Msis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msis", core, parent)

	def set(self, drive: str) -> None:
		"""SCPI: MMEMory:MSIS \n
		Snippet: driver.massMemory.msis.set(drive = '1') \n
		This command selects the default storage device used by all MMEMory commands. \n
			:param drive: 'A:' | 'C:' | … | 'Z:' String containing the device drive name
		"""
		param = Conversions.value_to_quoted_str(drive)
		self._core.io.write(f'MMEMory:MSIS {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:MSIS \n
		Snippet: value: str = driver.massMemory.msis.get() \n
		This command selects the default storage device used by all MMEMory commands. \n
			:return: drive: 'A:' | 'C:' | … | 'Z:' String containing the device drive name"""
		response = self._core.io.query_str(f'MMEMory:MSIS?')
		return trim_str_response(response)
