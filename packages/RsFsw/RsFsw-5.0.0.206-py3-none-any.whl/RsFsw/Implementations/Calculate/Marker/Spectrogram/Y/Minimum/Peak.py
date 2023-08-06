from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Peak:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:SPECtrogram:Y:MINimum[:PEAK] \n
		Snippet: driver.calculate.marker.spectrogram.y.minimum.peak.set(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command moves a marker vertically to the minimum level for the current frequency. The search includes all frames. It
		does not change the horizontal position of the marker. If the marker hasn't been active yet, the command first looks for
		the peak level for all frequencies and moves the marker vertically to the minimum level. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SPECtrogram:Y:MINimum:PEAK')

	def set_with_opc(self, window=repcap.Window.Default, marker=repcap.Marker.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		"""SCPI: CALCulate<n>:MARKer<m>:SPECtrogram:Y:MINimum[:PEAK] \n
		Snippet: driver.calculate.marker.spectrogram.y.minimum.peak.set_with_opc(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command moves a marker vertically to the minimum level for the current frequency. The search includes all frames. It
		does not change the horizontal position of the marker. If the marker hasn't been active yet, the command first looks for
		the peak level for all frequencies and moves the marker vertically to the minimum level. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SPECtrogram:Y:MINimum:PEAK', opc_timeout_ms)
