from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:IQOFfset:AVERage \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.iqOffset.average.get() \n
		This command returns the average, maximum or minimum I/Q offset for the PPDU in dB. For details see 'I/Q Offset [dB]'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:IQOFfset:AVERage?')
		return Conversions.str_to_float(response)
