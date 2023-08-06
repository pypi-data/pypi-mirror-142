from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class B:
	"""B commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("b", core, parent)

	def set(self, category: enums.PowerCategoryB) -> None:
		"""SCPI: [SENSe]:POWer:CATegory:B \n
		Snippet: driver.applications.k14Xnr5G.sense.power.category.b.set(category = enums.PowerCategoryB.OPT1) \n
		This command selects the limit table for category B stations.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select category B base station ([SENSe:]POWer:CATegory) . \n
			:param category: OPT1 | OPT2
		"""
		param = Conversions.enum_scalar_to_str(category, enums.PowerCategoryB)
		self._core.io.write(f'SENSe:POWer:CATegory:B {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerCategoryB:
		"""SCPI: [SENSe]:POWer:CATegory:B \n
		Snippet: value: enums.PowerCategoryB = driver.applications.k14Xnr5G.sense.power.category.b.get() \n
		This command selects the limit table for category B stations.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select category B base station ([SENSe:]POWer:CATegory) . \n
			:return: category: OPT1 | OPT2"""
		response = self._core.io.query_str(f'SENSe:POWer:CATegory:B?')
		return Conversions.str_to_scalar_enum(response, enums.PowerCategoryB)
