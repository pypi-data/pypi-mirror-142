from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Idn:
	"""Idn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("idn", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:IDN \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.idn.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: idn: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:IDN?')
		return Conversions.str_to_float(response)
