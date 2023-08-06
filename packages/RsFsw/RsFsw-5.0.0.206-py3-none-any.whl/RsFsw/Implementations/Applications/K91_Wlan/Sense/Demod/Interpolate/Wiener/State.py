from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:STATe \n
		Snippet: driver.applications.k91Wlan.sense.demod.interpolate.wiener.state.set(state = False) \n
		Defines whether the relative delay spread is determined automatically or manually. This command is only available for
		standards IEEE 802.11ax, be and only for [SENSe:]DEMod:INTerpolate Wiener. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The value is determined manually, using [SENSe:]DEMod:INTerpolate:WIENer:DSPRead. ON | 1 The value is determined automatically.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:INTerpolate:WIENer:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:INTerpolate:WIENer:STATe \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.interpolate.wiener.state.get() \n
		Defines whether the relative delay spread is determined automatically or manually. This command is only available for
		standards IEEE 802.11ax, be and only for [SENSe:]DEMod:INTerpolate Wiener. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The value is determined manually, using [SENSe:]DEMod:INTerpolate:WIENer:DSPRead. ON | 1 The value is determined automatically."""
		response = self._core.io.query_str(f'SENSe:DEMod:INTerpolate:WIENer:STATe?')
		return Conversions.str_to_bool(response)
