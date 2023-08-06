from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fail:
	"""Fail commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fail", core, parent)

	def get(self) -> bool:
		"""SCPI: FETCh:SYNC:FAIL \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.fetch.sync.fail.get() \n
		This command queries the synchronization status. \n
			:return: state: 1 Synchronization was not successful. 0 Synchronization was successful."""
		response = self._core.io.query_str(f'FETCh:SYNC:FAIL?')
		return Conversions.str_to_bool(response)
