from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wav:
	"""Wav commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wav", core, parent)

	@property
	def agc(self):
		"""agc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agc'):
			from .Agc import Agc
			self._agc = Agc(self._core, self._cmd_group)
		return self._agc

	def set(self, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:WAV \n
		Snippet: driver.massMemory.store.wav.set(filename = '1', store = repcap.Store.Default) \n
		No command help available \n
			:param filename: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:WAV {param}')

	def get(self, store=repcap.Store.Default) -> str:
		"""SCPI: MMEMory:STORe<n>:WAV \n
		Snippet: value: str = driver.massMemory.store.wav.get(store = repcap.Store.Default) \n
		No command help available \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: filename: No help available"""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:WAV?')
		return trim_str_response(response)

	def clone(self) -> 'Wav':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wav(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
