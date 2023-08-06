from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McFilter:
	"""McFilter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcFilter", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:MCFilter \n
		Snippet: driver.applications.k10Xlte.sense.lte.downlink.demod.mcFilter.set(state = False) \n
		This command turns suppression of interfering neighboring carriers on and off (e.g. LTE, WCDMA, GSM etc) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LTE:DL:DEMod:MCFilter {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:MCFilter \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.lte.downlink.demod.mcFilter.get() \n
		This command turns suppression of interfering neighboring carriers on and off (e.g. LTE, WCDMA, GSM etc) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:LTE:DL:DEMod:MCFilter?')
		return Conversions.str_to_bool(response)
