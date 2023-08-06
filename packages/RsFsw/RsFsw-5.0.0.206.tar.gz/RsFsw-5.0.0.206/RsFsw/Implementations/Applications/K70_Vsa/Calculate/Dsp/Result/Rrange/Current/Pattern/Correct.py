from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correct:
	"""Correct commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correct", core, parent)

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:DSP:RESult:RRANge:CURRent:PATTern:CORRect \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.dsp.result.rrange.current.pattern.correct.get(window = repcap.Window.Default) \n
		Queries whether the pattern is correct or not in the current result range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: correct: ON | OFF | 0 | 1 OFF | 0 Pattern not correct. ON | 1 Pattern correct"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DSP:RESult:RRANge:CURRent:PATTern:CORRect?')
		return Conversions.str_to_bool(response)
