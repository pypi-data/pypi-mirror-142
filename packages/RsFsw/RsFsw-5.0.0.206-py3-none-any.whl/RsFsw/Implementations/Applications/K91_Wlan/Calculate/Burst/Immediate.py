from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, window=repcap.Window.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALCulate<n>:BURSt[:IMMediate] \n
		Snippet: driver.applications.k91Wlan.calculate.burst.immediate.set(window = repcap.Window.Default) \n
		This command forces the IQ measurement results to be recalculated according to the current settings. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:BURSt:IMMediate', opc_timeout_ms)
