from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: driver.applications.k40PhaseNoise.configure.power.auto.set(arg_0 = False) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'CONFigure:POWer:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.configure.power.auto.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO?')
		return Conversions.str_to_bool(response)
