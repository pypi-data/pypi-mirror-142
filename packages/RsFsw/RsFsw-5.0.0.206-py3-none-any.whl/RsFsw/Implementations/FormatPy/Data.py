from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data_format: enums.DataFormat) -> None:
		"""SCPI: FORMat[:DATA] \n
		Snippet: driver.formatPy.data.set(data_format = enums.DataFormat.ASCii) \n
		This command selects the data format that is used for transmission of trace data from the R&S FSW to the controlling
		computer. Note that the command has no effect for data that you send to the R&S FSW. The R&S FSW automatically recognizes
		the data it receives, regardless of the format. For details on data formats see 'Formats for returned values: ASCII
		format and binary format'. \n
			:param data_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(data_format, enums.DataFormat)
		self._core.io.write_with_opc(f'FORMat:DATA {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DataFormat:
		"""SCPI: FORMat[:DATA] \n
		Snippet: value: enums.DataFormat = driver.formatPy.data.get() \n
		This command selects the data format that is used for transmission of trace data from the R&S FSW to the controlling
		computer. Note that the command has no effect for data that you send to the R&S FSW. The R&S FSW automatically recognizes
		the data it receives, regardless of the format. For details on data formats see 'Formats for returned values: ASCII
		format and binary format'. \n
			:return: data_format: No help available"""
		response = self._core.io.query_str_with_opc(f'FORMat:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataFormat)
