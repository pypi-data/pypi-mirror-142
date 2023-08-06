from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpath:
	"""Dpath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpath", core, parent)

	def set(self, auto_off: enums.State, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:DPATh \n
		Snippet: driver.applications.k70Vsa.inputPy.dpath.set(auto_off = enums.State.ALL, inputIx = repcap.InputIx.Default) \n
		Enables or disables the use of the direct path for frequencies close to 0 Hz. \n
			:param auto_off: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(auto_off, enums.State)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:DPATh {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.State:
		"""SCPI: INPut<ip>:DPATh \n
		Snippet: value: enums.State = driver.applications.k70Vsa.inputPy.dpath.get(inputIx = repcap.InputIx.Default) \n
		Enables or disables the use of the direct path for frequencies close to 0 Hz. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: auto_off: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DPATh?')
		return Conversions.str_to_scalar_enum(response, enums.State)
