from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mservice:
	"""Mservice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mservice", core, parent)

	def set(self, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:MSERvice \n
		Snippet: driver.applications.k10Xlte.massMemory.store.mservice.set(filename = '1', store = repcap.Store.Default) \n
		This command exports the signal configuration to the microservice. \n
			:param filename: String containing the path and name of the file. The file extension is .m5g.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:MSERvice {param}')

	def get(self, store=repcap.Store.Default) -> str:
		"""SCPI: MMEMory:STORe<n>:MSERvice \n
		Snippet: value: str = driver.applications.k10Xlte.massMemory.store.mservice.get(store = repcap.Store.Default) \n
		This command exports the signal configuration to the microservice. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: filename: String containing the path and name of the file. The file extension is .m5g."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:MSERvice?')
		return trim_str_response(response)
