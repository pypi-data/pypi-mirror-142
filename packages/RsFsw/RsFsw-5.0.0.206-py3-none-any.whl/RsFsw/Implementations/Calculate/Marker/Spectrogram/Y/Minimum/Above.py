from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Above:
	"""Above commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("above", core, parent)

	def set(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:SPECtrogram:Y:MINimum:ABOVe \n
		Snippet: driver.calculate.marker.spectrogram.y.minimum.above.set(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command moves a marker vertically to the next higher minimum level for the current frequency. The search includes
		only frames above the current marker position. It does not change the horizontal position of the marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SPECtrogram:Y:MINimum:ABOVe')

	def set_with_opc(self, window=repcap.Window.Default, marker=repcap.Marker.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		"""SCPI: CALCulate<n>:MARKer<m>:SPECtrogram:Y:MINimum:ABOVe \n
		Snippet: driver.calculate.marker.spectrogram.y.minimum.above.set_with_opc(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command moves a marker vertically to the next higher minimum level for the current frequency. The search includes
		only frames above the current marker position. It does not change the horizontal position of the marker. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SPECtrogram:Y:MINimum:ABOVe', opc_timeout_ms)
