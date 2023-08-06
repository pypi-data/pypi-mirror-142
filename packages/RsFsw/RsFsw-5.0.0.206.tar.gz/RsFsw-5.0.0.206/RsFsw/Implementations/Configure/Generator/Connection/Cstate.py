from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstate:
	"""Cstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cstate", core, parent)

	def get(self) -> str:
		"""SCPI: CONFigure:GENerator:CONNection:CSTate \n
		Snippet: value: str = driver.configure.generator.connection.cstate.get() \n
		Queries the state of the connected signal generator. \n
			:return: connection_state: UNKNown no signal generator connected CONNected connection established NCONnected connection could not be established, possibly due to an incompatible instrument or invalid IP address"""
		response = self._core.io.query_str(f'CONFigure:GENerator:CONNection:CSTate?')
		return trim_str_response(response)
