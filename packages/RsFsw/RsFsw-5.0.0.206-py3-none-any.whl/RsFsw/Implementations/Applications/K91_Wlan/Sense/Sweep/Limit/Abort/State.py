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
		"""SCPI: [SENSe]:SWEep:LIMit:ABORt:STATe \n
		Snippet: driver.applications.k91Wlan.sense.sweep.limit.abort.state.set(state = False) \n
		This command determines the behavior of the application after a limit check fails. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 A limit check has no effects on the measurement. ON | 1 The measurement is stopped if the limit check fails at any time during the measurement.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:LIMit:ABORt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:LIMit:ABORt:STATe \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.sweep.limit.abort.state.get() \n
		This command determines the behavior of the application after a limit check fails. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 A limit check has no effects on the measurement. ON | 1 The measurement is stopped if the limit check fails at any time during the measurement."""
		response = self._core.io.query_str(f'SENSe:SWEep:LIMit:ABORt:STATe?')
		return Conversions.str_to_bool(response)
