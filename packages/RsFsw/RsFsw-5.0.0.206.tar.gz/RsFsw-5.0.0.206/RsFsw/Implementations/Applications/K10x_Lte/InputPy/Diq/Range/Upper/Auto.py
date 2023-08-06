from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:DIQ:RANGe[:UPPer]:AUTO \n
		Snippet: driver.applications.k10Xlte.inputPy.diq.range.upper.auto.set(state = False, inputIx = repcap.InputIx.Default) \n
		If enabled, the digital input full scale level is automatically set to the value provided by the connected device (if
		available) . This command is only available if the optional Digital Baseband interface is installed. \n
			:param state: ON | OFF | 1 | 0
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer:AUTO {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:DIQ:RANGe[:UPPer]:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.inputPy.diq.range.upper.auto.get(inputIx = repcap.InputIx.Default) \n
		If enabled, the digital input full scale level is automatically set to the value provided by the connected device (if
		available) . This command is only available if the optional Digital Baseband interface is installed. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 1 | 0"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DIQ:RANGe:UPPer:AUTO?')
		return Conversions.str_to_bool(response)
