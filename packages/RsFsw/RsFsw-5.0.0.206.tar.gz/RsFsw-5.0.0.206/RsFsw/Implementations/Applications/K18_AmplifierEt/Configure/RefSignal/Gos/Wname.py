from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wname:
	"""Wname commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wname", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:WNAMe \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.wname.set(filename = '1') \n
		This command defines a file name for the waveform of the reference signal. \n
			:param filename: String containing the name of the waveform file. The file extension (.wv) is added automatically.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:REFSignal:GOS:WNAMe {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:REFSignal:GOS:WNAMe \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.refSignal.gos.wname.get() \n
		This command defines a file name for the waveform of the reference signal. \n
			:return: filename: String containing the name of the waveform file. The file extension (.wv) is added automatically."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:WNAMe?')
		return trim_str_response(response)
