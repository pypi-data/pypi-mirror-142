from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def get(self) -> str:
		"""SCPI: CONFigure:GENerator:NPRatio:BB:STANdard \n
		Snippet: value: str = driver.configure.generator.npratio.bb.standard.get() \n
		Queries the standard currently used by the signal generator. \n
			:return: standard: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:BB:STANdard?')
		return trim_str_response(response)
