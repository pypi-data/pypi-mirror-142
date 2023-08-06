from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self) -> int:
		"""SCPI: [SENSe]:SWEep:COUNt:CURRent \n
		Snippet: value: int = driver.applications.k6Pulse.sense.sweep.count.current.get() \n
		This query returns the current number of started sweeps or measurements. This command is only available if a sweep count
		value is defined and the instrument is in single sweep mode. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt:CURRent?')
		return Conversions.str_to_int(response)
