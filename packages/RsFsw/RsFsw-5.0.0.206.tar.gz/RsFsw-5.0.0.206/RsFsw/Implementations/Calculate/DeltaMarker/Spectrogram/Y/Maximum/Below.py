from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Below:
	"""Below commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("below", core, parent)

	def set(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:SPECtrogram:Y:MAXimum:BELow \n
		Snippet: driver.calculate.deltaMarker.spectrogram.y.maximum.below.set(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command moves a marker vertically to the next higher level for the current frequency. The search includes only
		frames below the current marker position. It does not change the horizontal position of the marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:SPECtrogram:Y:MAXimum:BELow')

	def set_with_opc(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		"""SCPI: CALCulate<n>:DELTamarker<m>:SPECtrogram:Y:MAXimum:BELow \n
		Snippet: driver.calculate.deltaMarker.spectrogram.y.maximum.below.set_with_opc(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command moves a marker vertically to the next higher level for the current frequency. The search includes only
		frames below the current marker position. It does not change the horizontal position of the marker. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:SPECtrogram:Y:MAXimum:BELow', opc_timeout_ms)
