from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:RTIMe:MINimum \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.rtime.minimum.get() \n
		This command returns the average, maximum or minimum rise time for the PPDU in s. For details see 'Rise Time [s]'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:RTIMe:MINimum?')
		return Conversions.str_to_float(response)
