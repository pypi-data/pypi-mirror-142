from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:HBERate:MAXimum \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.hbeRate.maximum.get() \n
		This command returns the average, maximum or minimum Bit Error Rate of the PPDU header. For details see 'IEEE 802.
		11ad modulation accuracy measurement'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:HBERate:MAXimum?')
		return Conversions.str_to_float(response)
