from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fpath:
	"""Fpath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fpath", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: CONFigure:REFSignal:CWF:FPATh \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cwf.fpath.set(filename = '1') \n
		This command selects a waveform file containing a reference signal. \n
			:param filename: String containing the name and path to the waveform file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:REFSignal:CWF:FPATh {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:REFSignal:CWF:FPATh \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.refSignal.cwf.fpath.get() \n
		This command selects a waveform file containing a reference signal. \n
			:return: filename: String containing the name and path to the waveform file."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:CWF:FPATh?')
		return trim_str_response(response)
