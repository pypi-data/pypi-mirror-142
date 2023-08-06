from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Peak:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FIXed:RPOint:MAXimum[:PEAK] \n
		Snippet: driver.applications.k91Wlan.calculate.deltaMarker.function.fixed.rpoint.maximum.peak.set(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FIXed:RPOint:MAXimum:PEAK')

	def set_with_opc(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FIXed:RPOint:MAXimum[:PEAK] \n
		Snippet: driver.applications.k91Wlan.calculate.deltaMarker.function.fixed.rpoint.maximum.peak.set_with_opc(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FIXed:RPOint:MAXimum:PEAK', opc_timeout_ms)
