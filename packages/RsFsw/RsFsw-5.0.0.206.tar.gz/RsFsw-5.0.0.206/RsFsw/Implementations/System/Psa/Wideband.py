from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wideband:
	"""Wideband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wideband", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:PSA:WIDeband \n
		Snippet: driver.system.psa.wideband.set(state = False) \n
		This command defines which option is returned when the *OPT? query is executed, depending on the state of the wideband
		option. It is only available for PSA89600 emulation. \n
			:param state: ON | OFF | HIGH OFF The option is indicated as 'B7J' ON The 40 MHz wideband is used. The option is indicated as 'B7J, 140'. HIGH The 80 MHz wideband is used. The option is indicated as 'B7J, 122'.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:PSA:WIDeband {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:PSA:WIDeband \n
		Snippet: value: bool = driver.system.psa.wideband.get() \n
		This command defines which option is returned when the *OPT? query is executed, depending on the state of the wideband
		option. It is only available for PSA89600 emulation. \n
			:return: state: ON | OFF | HIGH OFF The option is indicated as 'B7J' ON The 40 MHz wideband is used. The option is indicated as 'B7J, 140'. HIGH The 80 MHz wideband is used. The option is indicated as 'B7J, 122'."""
		response = self._core.io.query_str(f'SYSTem:PSA:WIDeband?')
		return Conversions.str_to_bool(response)
