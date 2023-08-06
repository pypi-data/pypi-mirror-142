from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:FSYNc:RESult \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.fsync.result.get() \n
		Queries the result of the fine sync. \n
			:return: result: ON | OFF | 0 | 1 OFF | 0 fine sync with known data failed ON | 1 fine sync with known data successful"""
		response = self._core.io.query_str(f'SENSe:DDEMod:FSYNc:RESult?')
		return Conversions.str_to_bool(response)
