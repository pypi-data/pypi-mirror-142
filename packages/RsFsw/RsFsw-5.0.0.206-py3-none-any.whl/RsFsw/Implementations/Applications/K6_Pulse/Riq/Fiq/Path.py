from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: RIQ:FIQ:PATH \n
		Snippet: driver.applications.k6Pulse.riq.fiq.path.set(filename = '1') \n
		Selects the I/Q data file which contains the reference waveform. The file must be in iq.tar format as specified in 'I/Q
		data file format (iq-tar) '. \n
			:param filename: String containing the path and name of the file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'RIQ:FIQ:PATH {param}')

	def get(self) -> str:
		"""SCPI: RIQ:FIQ:PATH \n
		Snippet: value: str = driver.applications.k6Pulse.riq.fiq.path.get() \n
		Selects the I/Q data file which contains the reference waveform. The file must be in iq.tar format as specified in 'I/Q
		data file format (iq-tar) '. \n
			:return: filename: String containing the path and name of the file."""
		response = self._core.io.query_str(f'RIQ:FIQ:PATH?')
		return trim_str_response(response)
