from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, file_format: enums.FileFormat) -> None:
		"""SCPI: FORMat:DEXPort:FORMat \n
		Snippet: driver.formatPy.dexport.formatPy.set(file_format = enums.FileFormat.CSV) \n
		Determines the format of the ASCII file to be imported or exported. Depending on the external program in which the data
		file was created or will be evaluated, a comma-separated list (CSV) or a plain data format (DAT) file may be required. \n
			:param file_format: CSV | DAT
		"""
		param = Conversions.enum_scalar_to_str(file_format, enums.FileFormat)
		self._core.io.write(f'FORMat:DEXPort:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FileFormat:
		"""SCPI: FORMat:DEXPort:FORMat \n
		Snippet: value: enums.FileFormat = driver.formatPy.dexport.formatPy.get() \n
		Determines the format of the ASCII file to be imported or exported. Depending on the external program in which the data
		file was created or will be evaluated, a comma-separated list (CSV) or a plain data format (DAT) file may be required. \n
			:return: file_format: CSV | DAT"""
		response = self._core.io.query_str(f'FORMat:DEXPort:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.FileFormat)
