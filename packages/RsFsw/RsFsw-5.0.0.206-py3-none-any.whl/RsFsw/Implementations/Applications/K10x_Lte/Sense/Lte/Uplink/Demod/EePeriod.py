from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EePeriod:
	"""EePeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eePeriod", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:EEPeriod \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.eePeriod.set(state = False) \n
		This command includes or excludes the exclusion period from EVM results. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:EEPeriod {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:EEPeriod \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.lte.uplink.demod.eePeriod.get() \n
		This command includes or excludes the exclusion period from EVM results. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:EEPeriod?')
		return Conversions.str_to_bool(response)
