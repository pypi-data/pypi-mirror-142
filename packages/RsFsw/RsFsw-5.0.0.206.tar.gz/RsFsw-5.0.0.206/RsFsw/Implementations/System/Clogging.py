from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clogging:
	"""Clogging commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clogging", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:CLOGging \n
		Snippet: driver.system.clogging.set(state = False) \n
		This command turns logging of remote commands on and off. \n
			:param state: ON | OFF | 1 | 0 ON | 1 Writes all remote commands that have been sent to a file. The destination is C:/R_S/INSTR/ScpiLogging/ ScpiLog.no.. where no. is a sequential number A new log file is started each time logging was stopped and is restarted. OFF | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:CLOGging {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:CLOGging \n
		Snippet: value: bool = driver.system.clogging.get() \n
		This command turns logging of remote commands on and off. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 Writes all remote commands that have been sent to a file. The destination is C:/R_S/INSTR/ScpiLogging/ ScpiLog.no.. where no. is a sequential number A new log file is started each time logging was stopped and is restarted. OFF | 0"""
		response = self._core.io.query_str(f'SYSTem:CLOGging?')
		return Conversions.str_to_bool(response)
