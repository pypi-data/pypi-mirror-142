from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SiSync:
	"""SiSync commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("siSync", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:SISYnc \n
		Snippet: driver.applications.k10Xlte.sense.lte.uplink.demod.siSync.set(state = False) \n
		This command turns suppressed interference synchronization on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LTE:UL:DEMod:SISYnc {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe][:LTE]:UL:DEMod:SISYnc \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.lte.uplink.demod.siSync.get() \n
		This command turns suppressed interference synchronization on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:LTE:UL:DEMod:SISYnc?')
		return Conversions.str_to_bool(response)
