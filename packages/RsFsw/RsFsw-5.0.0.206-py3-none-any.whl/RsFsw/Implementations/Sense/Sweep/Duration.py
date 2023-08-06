from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:DURation \n
		Snippet: value: float = driver.sense.sweep.duration.get() \n
		This command provides an estimation of the total time required to capture the data and process it. This time span may be
		considerably longer than the actual sweep time (see [SENSe:]SWEep:TIME) . Tip: To determine the necessary timeout for
		data capturing in a remote control program, double the estimated time and add 1 second. \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:DURation?')
		return Conversions.str_to_float(response)
