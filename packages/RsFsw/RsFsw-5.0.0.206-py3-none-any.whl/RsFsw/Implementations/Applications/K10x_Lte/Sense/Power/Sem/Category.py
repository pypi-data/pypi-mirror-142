from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Category:
	"""Category commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("category", core, parent)

	def set(self, category: enums.SemPowerCategory) -> None:
		"""SCPI: [SENSe]:POWer:SEM:CATegory \n
		Snippet: driver.applications.k10Xlte.sense.power.sem.category.set(category = enums.SemPowerCategory.A) \n
		This command selects the SEM limit category as defined in 3GPP TS 36.104. \n
			:param category: A Category A (wide area base station) B1 Category B Opt 1 (wide area base station) B2 Category B Opt 2 (wide area base station) HOME Home base station LARE Local area base station MED Medium range base station
		"""
		param = Conversions.enum_scalar_to_str(category, enums.SemPowerCategory)
		self._core.io.write(f'SENSe:POWer:SEM:CATegory {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SemPowerCategory:
		"""SCPI: [SENSe]:POWer:SEM:CATegory \n
		Snippet: value: enums.SemPowerCategory = driver.applications.k10Xlte.sense.power.sem.category.get() \n
		This command selects the SEM limit category as defined in 3GPP TS 36.104. \n
			:return: category: A Category A (wide area base station) B1 Category B Opt 1 (wide area base station) B2 Category B Opt 2 (wide area base station) HOME Home base station LARE Local area base station MED Medium range base station"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:CATegory?')
		return Conversions.str_to_scalar_enum(response, enums.SemPowerCategory)
