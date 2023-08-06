from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmark:
	"""Rmark commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmark", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SSEarch:RMARk \n
		Snippet: driver.applications.k50Spurious.sense.ssearch.rmark.set(state = False) \n
		No command help available \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Residuals are not marked ON | 1 Residuals are marked
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SSEarch:RMARk {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SSEarch:RMARk \n
		Snippet: value: bool = driver.applications.k50Spurious.sense.ssearch.rmark.get() \n
		No command help available \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Residuals are not marked ON | 1 Residuals are marked"""
		response = self._core.io.query_str(f'SENSe:SSEarch:RMARk?')
		return Conversions.str_to_bool(response)
