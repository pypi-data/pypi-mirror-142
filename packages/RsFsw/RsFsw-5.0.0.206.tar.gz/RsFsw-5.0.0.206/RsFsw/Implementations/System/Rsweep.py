from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsweep:
	"""Rsweep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsweep", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:RSWeep \n
		Snippet: driver.system.rsweep.set(state = False) \n
		Controls a repeated sweep of the E1 and MKPK HI HP model commands (for details on the commands refer to 'Reference: GPIB
		commands of emulated HP models') . If the repeated sweep is OFF, the marker is set without sweeping before. This command
		is only available if a HP language is selected using method RsFsw.System.Language.set \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:RSWeep {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:RSWeep \n
		Snippet: value: bool = driver.system.rsweep.get() \n
		Controls a repeated sweep of the E1 and MKPK HI HP model commands (for details on the commands refer to 'Reference: GPIB
		commands of emulated HP models') . If the repeated sweep is OFF, the marker is set without sweeping before. This command
		is only available if a HP language is selected using method RsFsw.System.Language.set \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SYSTem:RSWeep?')
		return Conversions.str_to_bool(response)
