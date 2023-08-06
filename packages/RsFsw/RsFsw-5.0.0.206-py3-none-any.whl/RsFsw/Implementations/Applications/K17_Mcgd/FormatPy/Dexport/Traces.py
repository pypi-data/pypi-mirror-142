from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Traces:
	"""Traces commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("traces", core, parent)

	def set(self, mode: enums.SelectionScope) -> None:
		"""SCPI: FORMat:DEXPort:TRACes \n
		Snippet: driver.applications.k17Mcgd.formatPy.dexport.traces.set(mode = enums.SelectionScope.ALL) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SelectionScope)
		self._core.io.write(f'FORMat:DEXPort:TRACes {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SelectionScope:
		"""SCPI: FORMat:DEXPort:TRACes \n
		Snippet: value: enums.SelectionScope = driver.applications.k17Mcgd.formatPy.dexport.traces.get() \n
		No command help available \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'FORMat:DEXPort:TRACes?')
		return Conversions.str_to_scalar_enum(response, enums.SelectionScope)
