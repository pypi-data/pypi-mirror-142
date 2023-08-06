from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rf:
	"""Rf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rf", core, parent)

	def set(self, path: enums.Path) -> None:
		"""SCPI: CONFigure:GENerator:TARGet:PATH:RF \n
		Snippet: driver.configure.generator.target.path.rf.set(path = enums.Path.A) \n
		Selects the RF signal path of the generator to be used for signal generation. \n
			:param path: A | B
		"""
		param = Conversions.enum_scalar_to_str(path, enums.Path)
		self._core.io.write(f'CONFigure:GENerator:TARGet:PATH:RF {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Path:
		"""SCPI: CONFigure:GENerator:TARGet:PATH:RF \n
		Snippet: value: enums.Path = driver.configure.generator.target.path.rf.get() \n
		Selects the RF signal path of the generator to be used for signal generation. \n
			:return: path: A | B"""
		response = self._core.io.query_str(f'CONFigure:GENerator:TARGet:PATH:RF?')
		return Conversions.str_to_scalar_enum(response, enums.Path)
