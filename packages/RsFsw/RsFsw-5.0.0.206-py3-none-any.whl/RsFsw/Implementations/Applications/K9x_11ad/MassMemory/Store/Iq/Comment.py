from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:COMMent \n
		Snippet: driver.applications.k9X11Ad.massMemory.store.iq.comment.set(comment = '1', store = repcap.Store.Default) \n
		This command adds a comment to a file that contains I/Q data. \n
			:param comment: String containing the comment.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(comment)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:COMMent {param}')

	def get(self, store=repcap.Store.Default) -> str:
		"""SCPI: MMEMory:STORe<n>:IQ:COMMent \n
		Snippet: value: str = driver.applications.k9X11Ad.massMemory.store.iq.comment.get(store = repcap.Store.Default) \n
		This command adds a comment to a file that contains I/Q data. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: comment: String containing the comment."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:IQ:COMMent?')
		return trim_str_response(response)
