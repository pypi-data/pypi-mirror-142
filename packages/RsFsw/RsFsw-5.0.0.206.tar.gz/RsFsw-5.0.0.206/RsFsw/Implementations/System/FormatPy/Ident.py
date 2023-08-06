from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ident:
	"""Ident commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ident", core, parent)

	def set(self, idn_format: enums.IdnFormat) -> None:
		"""SCPI: SYSTem:FORMat:IDENt \n
		Snippet: driver.system.formatPy.ident.set(idn_format = enums.IdnFormat.FSL) \n
		This command selects the response format to the *IDN? query. \n
			:param idn_format: LEGacy Format is compatible to R&S FSP/FSU/FSQ/FSG family. NEW | FSL R&S FSW format Format is also compatible to the R&S FSL and R&S FSV family
		"""
		param = Conversions.enum_scalar_to_str(idn_format, enums.IdnFormat)
		self._core.io.write(f'SYSTem:FORMat:IDENt {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IdnFormat:
		"""SCPI: SYSTem:FORMat:IDENt \n
		Snippet: value: enums.IdnFormat = driver.system.formatPy.ident.get() \n
		This command selects the response format to the *IDN? query. \n
			:return: idn_format: LEGacy Format is compatible to R&S FSP/FSU/FSQ/FSG family. NEW | FSL R&S FSW format Format is also compatible to the R&S FSL and R&S FSV family"""
		response = self._core.io.query_str(f'SYSTem:FORMat:IDENt?')
		return Conversions.str_to_scalar_enum(response, enums.IdnFormat)
