from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.EgateType) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TYPE \n
		Snippet: driver.applications.k10Xlte.sense.sweep.egate.typePy.set(type_py = enums.EgateType.EDGE) \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.EgateType)
		self._core.io.write(f'SENSe:SWEep:EGATe:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EgateType:
		"""SCPI: [SENSe]:SWEep:EGATe:TYPE \n
		Snippet: value: enums.EgateType = driver.applications.k10Xlte.sense.sweep.egate.typePy.get() \n
		No command help available \n
			:return: type_py: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.EgateType)
