from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dirty:
	"""Dirty commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dirty", core, parent)

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:MEAS:DIRTy \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.meas.dirty.get(window = repcap.Window.Default) \n
		Queries the validity of the measurement data, as indicated in the channel bar in manual operation. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 0 | 1 OFF | 0 The measurement results are valid. ON | 1 Invalid or inconsistent data is displayed, that is: the trace no longer matches the displayed instrument settings."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MEAS:DIRTy?')
		return Conversions.str_to_bool(response)
