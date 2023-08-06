from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	def set(self, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:SPECtrogram:COLor:DEFault \n
		Snippet: driver.display.window.spectrogram.color.default.set(window = repcap.Window.Default) \n
		This command restores the original color map. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SPECtrogram:COLor:DEFault')

	def set_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: DISPlay[:WINDow<n>]:SPECtrogram:COLor:DEFault \n
		Snippet: driver.display.window.spectrogram.color.default.set_with_opc(window = repcap.Window.Default) \n
		This command restores the original color map. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:SPECtrogram:COLor:DEFault', opc_timeout_ms)
