from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlockSize:
	"""BlockSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blockSize", core, parent)

	def set(self, block_size: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PPSPectrum:BLOCksize \n
		Snippet: driver.applications.k6Pulse.calculate.ppSpectrum.blockSize.set(block_size = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param block_size: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(block_size)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PPSPectrum:BLOCksize {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PPSPectrum:BLOCksize \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.ppSpectrum.blockSize.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: block_size: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PPSPectrum:BLOCksize?')
		return Conversions.str_to_float(response)
