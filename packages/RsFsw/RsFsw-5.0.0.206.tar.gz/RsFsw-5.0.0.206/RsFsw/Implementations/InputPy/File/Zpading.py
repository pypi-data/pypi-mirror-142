from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zpading:
	"""Zpading commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zpading", core, parent)

	def set(self, arg_0: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<1|2>:FILE:ZPADing \n
		Snippet: driver.inputPy.file.zpading.set(arg_0 = False, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(arg_0)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:FILE:ZPADing {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<1|2>:FILE:ZPADing \n
		Snippet: value: bool = driver.inputPy.file.zpading.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: arg_0: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:FILE:ZPADing?')
		return Conversions.str_to_bool(response)
