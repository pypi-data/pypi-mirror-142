from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impedance:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	def set(self, impedance: int, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:IMPedance \n
		Snippet: driver.applications.k91Wlan.inputPy.impedance.set(impedance = 1, inputIx = repcap.InputIx.Default) \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported. \n
			:param impedance: 50 | 75 Unit: OHM
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(impedance)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IMPedance {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> int:
		"""SCPI: INPut<Undef>:IMPedance \n
		Snippet: value: int = driver.applications.k91Wlan.inputPy.impedance.get(inputIx = repcap.InputIx.Default) \n
		This command selects the nominal input impedance of the RF input. In some applications, only 50 Ω are supported. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: impedance: 50 | 75 Unit: OHM"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IMPedance?')
		return Conversions.str_to_int(response)
