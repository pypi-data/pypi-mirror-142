from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.TypeLte) -> None:
		"""SCPI: CONFigure[:LTE]:TYPE \n
		Snippet: driver.applications.k10Xlte.configure.lte.typePy.set(type_py = enums.TypeLte.ANCHor) \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.TypeLte)
		self._core.io.write(f'CONFigure:LTE:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TypeLte:
		"""SCPI: CONFigure[:LTE]:TYPE \n
		Snippet: value: enums.TypeLte = driver.applications.k10Xlte.configure.lte.typePy.get() \n
		No command help available \n
			:return: type_py: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.TypeLte)
