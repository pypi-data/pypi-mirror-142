from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dseparator:
	"""Dseparator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dseparator", core, parent)

	def set(self, separator: enums.Separator) -> None:
		"""SCPI: FORMat:DEXPort:DSEParator \n
		Snippet: driver.applications.k17Mcgd.formatPy.dexport.dseparator.set(separator = enums.Separator.COMMa) \n
		No command help available \n
			:param separator: No help available
		"""
		param = Conversions.enum_scalar_to_str(separator, enums.Separator)
		self._core.io.write(f'FORMat:DEXPort:DSEParator {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Separator:
		"""SCPI: FORMat:DEXPort:DSEParator \n
		Snippet: value: enums.Separator = driver.applications.k17Mcgd.formatPy.dexport.dseparator.get() \n
		No command help available \n
			:return: separator: No help available"""
		response = self._core.io.query_str(f'FORMat:DEXPort:DSEParator?')
		return Conversions.str_to_scalar_enum(response, enums.Separator)
