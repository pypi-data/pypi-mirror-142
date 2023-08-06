from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ival:
	"""Ival commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ival", core, parent)

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:MSRA:WINDow:IVAL \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.msra.window.ival.get(window = repcap.Window.Default) \n
		Returns the current analysis interval for applications in MSRA operating mode. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: stimulus: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MSRA:WINDow:IVAL?')
		return Conversions.str_to_float(response)
