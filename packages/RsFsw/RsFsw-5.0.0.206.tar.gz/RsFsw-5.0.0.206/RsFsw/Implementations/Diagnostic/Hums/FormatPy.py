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

	def set(self, format_py: enums.HumsFileFormat) -> None:
		"""SCPI: DIAGnostic:HUMS:FORMat \n
		Snippet: driver.diagnostic.hums.formatPy.set(format_py = enums.HumsFileFormat.JSON) \n
		This command defines the format for the queried HUMS data. You can query the HUMS data either in JSON format or XML
		format. The defined format affects all other commands that return block data. \n
			:param format_py: JSON | XML JSON Returns the HUMS data in JSON format. XML Returns the HUMS data in XML format.
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.HumsFileFormat)
		self._core.io.write(f'DIAGnostic:HUMS:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.HumsFileFormat:
		"""SCPI: DIAGnostic:HUMS:FORMat \n
		Snippet: value: enums.HumsFileFormat = driver.diagnostic.hums.formatPy.get() \n
		This command defines the format for the queried HUMS data. You can query the HUMS data either in JSON format or XML
		format. The defined format affects all other commands that return block data. \n
			:return: format_py: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:HUMS:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.HumsFileFormat)
