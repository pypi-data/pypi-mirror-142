from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, window=repcap.Window.Default) -> int:
		"""SCPI: CALCulate<n>:SPECtrogram:FRAMe:COUNt \n
		Snippet: value: int = driver.applications.k60Transient.calculate.spectrogram.frame.count.get(window = repcap.Window.Default) \n
		This command queries the number of frames that are contained in the selected result display (depends on the evaluation
		basis) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: frames: The maximum number of frames depends on the history depth. Range: 1 to history depth"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:SPECtrogram:FRAMe:COUNt?')
		return Conversions.str_to_int(response)
