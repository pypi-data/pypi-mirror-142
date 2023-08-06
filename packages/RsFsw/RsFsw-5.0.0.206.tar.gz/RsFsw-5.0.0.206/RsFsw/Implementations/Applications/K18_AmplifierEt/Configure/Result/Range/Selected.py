from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Selected:
	"""Selected commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selected", core, parent)

	def set(self, result_range: float) -> None:
		"""SCPI: CONFigure:RESult:RANGe[:SELected] \n
		Snippet: driver.applications.k18AmplifierEt.configure.result.range.selected.set(result_range = 1.0) \n
		Sets and querys the selected result range. \n
			:param result_range: numeric value
		"""
		param = Conversions.decimal_value_to_str(result_range)
		self._core.io.write(f'CONFigure:RESult:RANGe:SELected {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:RESult:RANGe[:SELected] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.result.range.selected.get() \n
		Sets and querys the selected result range. \n
			:return: result_range: numeric value"""
		response = self._core.io.query_str(f'CONFigure:RESult:RANGe:SELected?')
		return Conversions.str_to_float(response)
