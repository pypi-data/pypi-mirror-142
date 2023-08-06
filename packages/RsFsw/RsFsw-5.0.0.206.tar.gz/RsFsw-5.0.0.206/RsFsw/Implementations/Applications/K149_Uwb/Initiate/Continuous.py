from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Continuous:
	"""Continuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("continuous", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INITiate:CONTinuous \n
		Snippet: driver.applications.k149Uwb.initiate.continuous.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INITiate:CONTinuous {param}')

	def get(self) -> bool:
		"""SCPI: INITiate:CONTinuous \n
		Snippet: value: bool = driver.applications.k149Uwb.initiate.continuous.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'INITiate:CONTinuous?')
		return Conversions.str_to_bool(response)
