from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lrange:
	"""Lrange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrange", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:MODeling:LRANge \n
		Snippet: driver.applications.k18AmplifierEt.configure.modeling.lrange.set(level = 1.0) \n
		This command defines the modeling level range. \n
			:param level: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:MODeling:LRANge {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:MODeling:LRANge \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.modeling.lrange.get() \n
		This command defines the modeling level range. \n
			:return: level: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:MODeling:LRANge?')
		return Conversions.str_to_float(response)
