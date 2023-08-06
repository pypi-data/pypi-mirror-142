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
		"""SCPI: INPut<ip>:EATT:AUTO \n
		Snippet: driver.applications.k70Vsa.inputPy.eatt.auto.set(state = False, inputIx = repcap.InputIx.Default) \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. This command requires the electronic attenuation hardware option. It is not
		available if the optional Digital Baseband Interface is active. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:EATT:AUTO {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:EATT:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.inputPy.eatt.auto.get(inputIx = repcap.InputIx.Default) \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. This command requires the electronic attenuation hardware option. It is not
		available if the optional Digital Baseband Interface is active. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:EATT:AUTO?')
		return Conversions.str_to_bool(response)
