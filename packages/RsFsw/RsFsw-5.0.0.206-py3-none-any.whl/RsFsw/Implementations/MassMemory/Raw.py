from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Raw:
	"""Raw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("raw", core, parent)

	def set(self, path: str) -> None:
		"""SCPI: MMEMory:RAW \n
		Snippet: driver.massMemory.raw.set(path = '1') \n
		Defines the location where the measurement data sets for the report are stored until the report is created. \n
			:param path: String containing the path of the preliminary data
		"""
		param = Conversions.value_to_quoted_str(path)
		self._core.io.write(f'MMEMory:RAW {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:RAW \n
		Snippet: value: str = driver.massMemory.raw.get() \n
		Defines the location where the measurement data sets for the report are stored until the report is created. \n
			:return: path: String containing the path of the preliminary data"""
		response = self._core.io.query_str(f'MMEMory:RAW?')
		return trim_str_response(response)
