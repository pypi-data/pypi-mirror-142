from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npoints:
	"""Npoints commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npoints", core, parent)

	def set(self, points: float) -> None:
		"""SCPI: CONFigure:MODeling:NPOints \n
		Snippet: driver.applications.k18AmplifierEt.configure.modeling.npoints.set(points = 1.0) \n
		This command defines the number of modeling points. \n
			:param points: numeric value: (integer only) Unit: ---
		"""
		param = Conversions.decimal_value_to_str(points)
		self._core.io.write(f'CONFigure:MODeling:NPOints {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:MODeling:NPOints \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.modeling.npoints.get() \n
		This command defines the number of modeling points. \n
			:return: points: numeric value: (integer only) Unit: ---"""
		response = self._core.io.query_str(f'CONFigure:MODeling:NPOints?')
		return Conversions.str_to_float(response)
