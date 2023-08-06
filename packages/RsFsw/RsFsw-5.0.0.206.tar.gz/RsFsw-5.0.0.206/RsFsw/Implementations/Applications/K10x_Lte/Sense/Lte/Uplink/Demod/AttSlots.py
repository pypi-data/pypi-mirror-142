from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttSlots:
	"""AttSlots commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attSlots", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:ATTSlots \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.attSlots.set(state = False) \n
		This command includes or excludes the transient slots present after a switch from downlink to uplink from the analysis. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:ATTSlots {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:ATTSlots \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.lte.uplink.demod.attSlots.get() \n
		This command includes or excludes the transient slots present after a switch from downlink to uplink from the analysis. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:ATTSlots?')
		return Conversions.str_to_bool(response)
