from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bypass:
	"""Bypass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bypass", core, parent)

	def set(self, bypass: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:EGAin:BYPass \n
		Snippet: driver.applications.k9X11Ad.inputPy.egain.bypass.set(bypass = False, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param bypass: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(bypass)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:EGAin:BYPass {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<Undef>:EGAin:BYPass \n
		Snippet: value: bool = driver.applications.k9X11Ad.inputPy.egain.bypass.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: bypass: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:EGAin:BYPass?')
		return Conversions.str_to_bool(response)
