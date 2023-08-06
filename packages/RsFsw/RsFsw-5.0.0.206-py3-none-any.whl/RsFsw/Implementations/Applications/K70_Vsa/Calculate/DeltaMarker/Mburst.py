from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mburst:
	"""Mburst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mburst", core, parent)

	def start(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MBURst:STARt \n
		Snippet: driver.applications.k70Vsa.calculate.deltaMarker.mburst.start(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command moves the marker m to the start of the selected result range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MBURst:STARt')

	def start_with_opc(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		"""SCPI: CALCulate<n>:DELTamarker<m>:MBURst:STARt \n
		Snippet: driver.applications.k70Vsa.calculate.deltaMarker.mburst.start_with_opc(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command moves the marker m to the start of the selected result range. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MBURst:STARt', opc_timeout_ms)
