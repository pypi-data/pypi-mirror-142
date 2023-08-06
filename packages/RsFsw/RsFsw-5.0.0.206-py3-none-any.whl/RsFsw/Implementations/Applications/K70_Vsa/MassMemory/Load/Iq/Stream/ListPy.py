from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self) -> str:
		"""SCPI: MMEMory:LOAD:IQ:STReam:LIST \n
		Snippet: value: str = driver.applications.k70Vsa.massMemory.load.iq.stream.listPy.get() \n
		Returns the available channels in the currently loaded input file. \n
			:return: channel: No help available"""
		response = self._core.io.query_str(f'MMEMory:LOAD:IQ:STReam:LIST?')
		return trim_str_response(response)
