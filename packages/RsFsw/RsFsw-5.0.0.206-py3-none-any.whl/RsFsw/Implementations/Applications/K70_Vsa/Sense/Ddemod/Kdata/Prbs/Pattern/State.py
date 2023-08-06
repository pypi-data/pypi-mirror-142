from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:PATTern[:STATe] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.pattern.state.set(state = False) \n
		Determines whether the pattern symbols are part of the PRBS sequence and are thus treated as data symbols. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The pattern is not part of the PRBS ON | 1 The pattern is part of the PRBS
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:PATTern:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:PATTern[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.pattern.state.get() \n
		Determines whether the pattern symbols are part of the PRBS sequence and are thus treated as data symbols. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The pattern is not part of the PRBS ON | 1 The pattern is part of the PRBS"""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:PATTern:STATe?')
		return Conversions.str_to_bool(response)
