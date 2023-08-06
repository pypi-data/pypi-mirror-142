from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Left:
	"""Left commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("left", core, parent)

	def set(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MAXimum:LEFT \n
		Snippet: driver.applications.k70Vsa.calculate.deltaMarker.maximum.left.set(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command moves a delta marker to the next higher value. The search includes only measurement values to the left of
		the current marker position. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MAXimum:LEFT', opc_timeout_ms)
