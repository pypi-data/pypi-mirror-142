from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Agc:
	"""Agc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("agc", core, parent)

	def set(self, state: bool, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:WAV:AGC \n
		Snippet: driver.massMemory.store.wav.agc.set(state = False, store = repcap.Store.Default) \n
		No command help available \n
			:param state: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.bool_to_str(state)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:WAV:AGC {param}')

	def get(self, store=repcap.Store.Default) -> bool:
		"""SCPI: MMEMory:STORe<n>:WAV:AGC \n
		Snippet: value: bool = driver.massMemory.store.wav.agc.get(store = repcap.Store.Default) \n
		No command help available \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: state: No help available"""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:WAV:AGC?')
		return Conversions.str_to_bool(response)
