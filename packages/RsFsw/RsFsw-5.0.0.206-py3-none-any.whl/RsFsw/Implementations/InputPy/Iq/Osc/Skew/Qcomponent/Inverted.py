from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Inverted:
	"""Inverted commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inverted", core, parent)

	def set(self, value: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:SKEW:Q:INVerted \n
		Snippet: driver.inputPy.iq.osc.skew.qcomponent.inverted.set(value = 1.0, inputIx = repcap.InputIx.Default) \n
		Compensates for skewed values in the negative Q path, e.g. due to different input cables. \n
			:param value: Unit: S
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(value)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:SKEW:Q:INVerted {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:SKEW:Q:INVerted \n
		Snippet: value: float = driver.inputPy.iq.osc.skew.qcomponent.inverted.get(inputIx = repcap.InputIx.Default) \n
		Compensates for skewed values in the negative Q path, e.g. due to different input cables. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: value: Unit: S"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:SKEW:Q:INVerted?')
		return Conversions.str_to_float(response)
