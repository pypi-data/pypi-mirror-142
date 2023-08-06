from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	def set(self, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:DEFault \n
		Snippet: driver.applications.k70Vsa.calculate.limit.maccuracy.default.set(window = repcap.Window.Default) \n
		Restores the default limits and deactivates all checks in all windows. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:DEFault')

	def set_with_opc(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:DEFault \n
		Snippet: driver.applications.k70Vsa.calculate.limit.maccuracy.default.set_with_opc(window = repcap.Window.Default) \n
		Restores the default limits and deactivates all checks in all windows. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:DEFault', opc_timeout_ms)
