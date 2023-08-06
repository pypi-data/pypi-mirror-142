from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:DEModsetting:ALL \n
		Snippet: driver.applications.k14Xnr5G.massMemory.store.demodSetting.all.set(filename = '1', store = repcap.Store.Default) \n
		This command saves the signal description of multiple carriers in a single file. \n
			:param filename: String containing the path and name of the file. The file extension is .ccallocation.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:DEModsetting:ALL {param}')

	def get(self, store=repcap.Store.Default) -> str:
		"""SCPI: MMEMory:STORe<n>:DEModsetting:ALL \n
		Snippet: value: str = driver.applications.k14Xnr5G.massMemory.store.demodSetting.all.get(store = repcap.Store.Default) \n
		This command saves the signal description of multiple carriers in a single file. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: filename: String containing the path and name of the file. The file extension is .ccallocation."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:DEModsetting:ALL?')
		return trim_str_response(response)
