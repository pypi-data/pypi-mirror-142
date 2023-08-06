from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:QUADoffset:MINimum \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.quadOffset.minimum.get() \n
		This command returns the average, maximum or minimum quadrature offset of symbols within a PPDU. This value indicates the
		phase accuracy. For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:return: result: list"""
		response = self._core.io.query_str(f'FETCh:BURSt:QUADoffset:MINimum?')
		return trim_str_response(response)
