from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.IqType, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:TYPE \n
		Snippet: driver.applications.k70Vsa.inputPy.iq.typePy.set(type_py = enums.IqType.Ipart=I, inputIx = repcap.InputIx.Default) \n
		This command defines the format of the input signal. \n
			:param type_py: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.IqType)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.IqType:
		"""SCPI: INPut<ip>:IQ:TYPE \n
		Snippet: value: enums.IqType = driver.applications.k70Vsa.inputPy.iq.typePy.get(inputIx = repcap.InputIx.Default) \n
		This command defines the format of the input signal. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: type_py: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.IqType)
