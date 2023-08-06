from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Saw:
	"""Saw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saw", core, parent)

	def set(self, state: enums.AutoOrOff, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:FILTer:SAW \n
		Snippet: driver.applications.k70Vsa.inputPy.filterPy.saw.set(state = enums.AutoOrOff.AUTO, inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param state: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoOrOff)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:FILTer:SAW {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.AutoOrOff:
		"""SCPI: INPut<ip>:FILTer:SAW \n
		Snippet: value: enums.AutoOrOff = driver.applications.k70Vsa.inputPy.filterPy.saw.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:FILTer:SAW?')
		return Conversions.str_to_scalar_enum(response, enums.AutoOrOff)
