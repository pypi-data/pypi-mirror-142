from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:CLEar[:IMMediate] \n
		Snippet: driver.calculate.limit.clear.immediate.set(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command deletes the result of the current limit check. The command works on all limit lines in all measurement
		windows at the same time. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CLEar:IMMediate')

	def set_with_opc(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		"""SCPI: CALCulate<n>:LIMit<li>:CLEar[:IMMediate] \n
		Snippet: driver.calculate.limit.clear.immediate.set_with_opc(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command deletes the result of the current limit check. The command works on all limit lines in all measurement
		windows at the same time. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CLEar:IMMediate', opc_timeout_ms)
