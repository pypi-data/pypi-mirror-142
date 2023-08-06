from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	def get(self) -> bool:
		"""SCPI: FETCh:DDPD:OPERation:STATus \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.fetch.ddpd.operation.status.get() \n
		This command queries the state of a direct DPD operation. \n
			:return: state: ON | OFF | 1 | 0 ON Direct DPD operation was successful. OFF Direct DPD operation was not successful."""
		response = self._core.io.query_str(f'FETCh:DDPD:OPERation:STATus?')
		return Conversions.str_to_bool(response)
