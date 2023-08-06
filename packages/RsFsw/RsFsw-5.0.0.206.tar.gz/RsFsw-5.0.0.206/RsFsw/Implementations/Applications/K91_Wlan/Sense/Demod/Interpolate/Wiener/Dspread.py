from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dspread:
	"""Dspread commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dspread", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:DSPRead \n
		Snippet: driver.applications.k91Wlan.sense.demod.interpolate.wiener.dspread.set(value = 1.0) \n
		Defines the value relative to the DFT period that is used for the Wiener filter design. Decrease this setting to finetune
		the EVM result if there is negligible delay spread, for example for a wired connection. This setting is only available
		for [SENSe:]DEMod:INTerpolate:WIENer:STATe OFF. \n
			:param value: Range: 0.0001 to 0.5
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:DEMod:INTerpolate:WIENer:DSPRead {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:DSPRead \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.interpolate.wiener.dspread.get() \n
		Defines the value relative to the DFT period that is used for the Wiener filter design. Decrease this setting to finetune
		the EVM result if there is negligible delay spread, for example for a wired connection. This setting is only available
		for [SENSe:]DEMod:INTerpolate:WIENer:STATe OFF. \n
			:return: value: Range: 0.0001 to 0.5"""
		response = self._core.io.query_str(f'SENSe:DEMod:INTerpolate:WIENer:DSPRead?')
		return Conversions.str_to_float(response)
