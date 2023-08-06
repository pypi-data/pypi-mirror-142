from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bb:
	"""Bb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bb", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.Path:
		"""SCPI: CONFigure:GENerator:TARGet:PATH:BB \n
		Snippet: value: enums.Path = driver.configure.generator.target.path.bb.get() \n
		Queries the BB signal path of the generator used for signal generation. \n
			:return: path: A | B"""
		response = self._core.io.query_str(f'CONFigure:GENerator:TARGet:PATH:BB?')
		return Conversions.str_to_scalar_enum(response, enums.Path)
