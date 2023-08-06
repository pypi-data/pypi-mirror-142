from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rf:
	"""Rf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rf", core, parent)

	def set(self, arg_0: float) -> None:
		"""SCPI: CONFigure:POWer:EXPected:RF \n
		Snippet: driver.applications.k40PhaseNoise.configure.power.expected.rf.set(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'CONFigure:POWer:EXPected:RF {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:POWer:EXPected:RF \n
		Snippet: value: float = driver.applications.k40PhaseNoise.configure.power.expected.rf.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'CONFigure:POWer:EXPected:RF?')
		return Conversions.str_to_float(response)
