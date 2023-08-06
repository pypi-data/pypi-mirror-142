from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: float) -> None:
		"""SCPI: CONFigure:EQUalizer:FILTer:LENGth \n
		Snippet: driver.applications.k18AmplifierEt.configure.equalizer.filterPy.length.set(length = 1.0) \n
		This command defines the length of the filter that the equalizer training is based on. \n
			:param length: numeric value (integer only)
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'CONFigure:EQUalizer:FILTer:LENGth {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:EQUalizer:FILTer:LENGth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.equalizer.filterPy.length.get() \n
		This command defines the length of the filter that the equalizer training is based on. \n
			:return: length: numeric value (integer only)"""
		response = self._core.io.query_str(f'CONFigure:EQUalizer:FILTer:LENGth?')
		return Conversions.str_to_float(response)
