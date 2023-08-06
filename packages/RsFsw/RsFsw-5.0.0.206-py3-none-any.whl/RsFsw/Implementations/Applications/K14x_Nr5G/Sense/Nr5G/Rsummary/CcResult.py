from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcResult:
	"""CcResult commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccResult", core, parent)

	def set(self, result: enums.CarriersAnalyze) -> None:
		"""SCPI: [SENSe]:NR5G:RSUMmary:CCResult \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.rsummary.ccResult.set(result = enums.CarriersAnalyze.ALL) \n
		Selects the way multiple carriers are analyzed.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select mutiple carriers (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.NoCc.set) . \n
			:param result: ALL Analyzes all component carriers and shows information about all of them in the result summary. VIEWed Analyzes the two component carriers assigned to the two views. The result summary only shows information about those two component carriers.
		"""
		param = Conversions.enum_scalar_to_str(result, enums.CarriersAnalyze)
		self._core.io.write(f'SENSe:NR5G:RSUMmary:CCResult {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CarriersAnalyze:
		"""SCPI: [SENSe]:NR5G:RSUMmary:CCResult \n
		Snippet: value: enums.CarriersAnalyze = driver.applications.k14Xnr5G.sense.nr5G.rsummary.ccResult.get() \n
		Selects the way multiple carriers are analyzed.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select mutiple carriers (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.NoCc.set) . \n
			:return: result: ALL Analyzes all component carriers and shows information about all of them in the result summary. VIEWed Analyzes the two component carriers assigned to the two views. The result summary only shows information about those two component carriers."""
		response = self._core.io.query_str(f'SENSe:NR5G:RSUMmary:CCResult?')
		return Conversions.str_to_scalar_enum(response, enums.CarriersAnalyze)
