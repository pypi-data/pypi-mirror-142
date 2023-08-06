from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:ATTenuation:AUTO \n
		Snippet: driver.applications.k91Wlan.inputPy.attenuation.auto.set(state = False, inputIx = repcap.InputIx.Default) \n
		This command couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the
		R&S FSW determines the signal level for optimal internal data processing and sets the required attenuation accordingly.
		This function is not available if the optional Digital Baseband Interface is active. \n
			:param state: ON | OFF | 0 | 1
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:ATTenuation:AUTO {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<Undef>:ATTenuation:AUTO \n
		Snippet: value: bool = driver.applications.k91Wlan.inputPy.attenuation.auto.get(inputIx = repcap.InputIx.Default) \n
		This command couples or decouples the attenuation to the reference level. Thus, when the reference level is changed, the
		R&S FSW determines the signal level for optimal internal data processing and sets the required attenuation accordingly.
		This function is not available if the optional Digital Baseband Interface is active. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 0 | 1"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:ATTenuation:AUTO?')
		return Conversions.str_to_bool(response)
