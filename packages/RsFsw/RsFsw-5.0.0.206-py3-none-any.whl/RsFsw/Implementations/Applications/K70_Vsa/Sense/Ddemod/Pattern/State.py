from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern[:STATe] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.state.set(state = False) \n
		Determines whether the pattern uses a different modulation type than the data symbols. This command is only available if
		the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The pattern uses the same modulation as the data symbols, defined by [SENSe:]DDEMod:MAPPing[:VALue]. ON | 1 The pattern uses a different modulation, configured by [SENSe:]DDEMod:PATTern:MAPPing[:VALue].
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:PATTern:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:PATTern[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.pattern.state.get() \n
		Determines whether the pattern uses a different modulation type than the data symbols. This command is only available if
		the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The pattern uses the same modulation as the data symbols, defined by [SENSe:]DDEMod:MAPPing[:VALue]. ON | 1 The pattern uses a different modulation, configured by [SENSe:]DDEMod:PATTern:MAPPing[:VALue]."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:STATe?')
		return Conversions.str_to_bool(response)
