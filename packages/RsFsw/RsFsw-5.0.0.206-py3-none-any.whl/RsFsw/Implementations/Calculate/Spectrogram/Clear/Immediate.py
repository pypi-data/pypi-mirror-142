from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:CLEar[:IMMediate] \n
		Snippet: driver.calculate.spectrogram.clear.immediate.set(window = repcap.Window.Default) \n
		This command resets the spectrogram and clears the history buffer. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:CLEar:IMMediate')

	def set_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: CALCulate<n>:SPECtrogram:CLEar[:IMMediate] \n
		Snippet: driver.calculate.spectrogram.clear.immediate.set_with_opc(window = repcap.Window.Default) \n
		This command resets the spectrogram and clears the history buffer. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:SPECtrogram:CLEar:IMMediate', opc_timeout_ms)
