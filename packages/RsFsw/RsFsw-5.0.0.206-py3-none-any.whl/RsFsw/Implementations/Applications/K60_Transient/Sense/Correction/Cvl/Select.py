from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:CORRection:CVL:SELect \n
		Snippet: driver.applications.k60Transient.sense.correction.cvl.select.set(filename = '1') \n
		This command selects the conversion loss table with the specified file name. If <file_name> is not available, a new
		conversion loss table is created. This command is only available with option B21 (External Mixer) installed. \n
			:param filename: String containing the path and name of the file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:CORRection:CVL:SELect {param}')

	def get(self, filename: str) -> str:
		"""SCPI: [SENSe]:CORRection:CVL:SELect \n
		Snippet: value: str = driver.applications.k60Transient.sense.correction.cvl.select.get(filename = '1') \n
		This command selects the conversion loss table with the specified file name. If <file_name> is not available, a new
		conversion loss table is created. This command is only available with option B21 (External Mixer) installed. \n
			:param filename: String containing the path and name of the file.
			:return: filename: String containing the path and name of the file."""
		param = Conversions.value_to_quoted_str(filename)
		response = self._core.io.query_str(f'SENSe:CORRection:CVL:SELect? {param}')
		return trim_str_response(response)
