from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qerror:
	"""Qerror commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qerror", core, parent)

	def get(self) -> str:
		"""SCPI: CONFigure:GENerator:QERRor \n
		Snippet: value: str = driver.applications.k14Xnr5G.configure.generator.qerror.get() \n
		This command queries any errors that might have occurred for the generator control \n
			:return: message: String containing the error messages."""
		response = self._core.io.query_str(f'CONFigure:GENerator:QERRor?')
		return trim_str_response(response)
