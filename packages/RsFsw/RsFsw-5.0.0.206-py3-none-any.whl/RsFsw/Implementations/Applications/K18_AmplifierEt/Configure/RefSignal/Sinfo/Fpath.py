from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fpath:
	"""Fpath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fpath", core, parent)

	def get(self) -> str:
		"""SCPI: CONFigure:REFSignal:SINFo:FPATh \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.refSignal.sinfo.fpath.get() \n
		This command queries the file name and location of the currently used reference signal. \n
			:return: filename: String containing the file name and location of the file."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:SINFo:FPATh?')
		return trim_str_response(response)
