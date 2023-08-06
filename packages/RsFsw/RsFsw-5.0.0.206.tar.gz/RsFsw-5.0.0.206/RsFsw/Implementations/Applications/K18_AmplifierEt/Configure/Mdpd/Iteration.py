from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iteration:
	"""Iteration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iteration", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:MDPD:ITERation \n
		Snippet: driver.applications.k18AmplifierEt.configure.mdpd.iteration.set(level = 1.0) \n
		Configures the iteration step for memory polynomial DPD. \n
			:param level: numeric value
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:MDPD:ITERation {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:MDPD:ITERation \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.mdpd.iteration.get() \n
		Configures the iteration step for memory polynomial DPD. \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'CONFigure:MDPD:ITERation?')
		return Conversions.str_to_float(response)
