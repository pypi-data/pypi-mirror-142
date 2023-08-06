from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AnalysisModeUl) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:MODE \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.mode.set(mode = enums.AnalysisModeUl.NPRach) \n
		This command selects the uplink analysis mode. \n
			:param mode: PUSCh Analyzes the PUSCH and PUCCH. PRACh Analyzes the PRACH.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AnalysisModeUl)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AnalysisModeUl:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:MODE \n
		Snippet: value: enums.AnalysisModeUl = driver.applications.k10Xlte.sense.lte.uplink.demod.mode.get() \n
		This command selects the uplink analysis mode. \n
			:return: mode: PUSCh Analyzes the PUSCH and PUCCH. PRACh Analyzes the PRACH."""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AnalysisModeUl)
