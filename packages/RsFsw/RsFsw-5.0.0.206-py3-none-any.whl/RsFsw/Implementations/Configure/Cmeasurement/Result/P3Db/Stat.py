from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stat:
	"""Stat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stat", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:CMEasurement:RESult:P3DB[:STAT] \n
		Snippet: driver.configure.cmeasurement.result.p3Db.stat.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:CMEasurement:RESult:P3DB:STAT {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:CMEasurement:RESult:P3DB[:STAT] \n
		Snippet: value: bool = driver.configure.cmeasurement.result.p3Db.stat.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'CONFigure:CMEasurement:RESult:P3DB:STAT?')
		return Conversions.str_to_bool(response)
