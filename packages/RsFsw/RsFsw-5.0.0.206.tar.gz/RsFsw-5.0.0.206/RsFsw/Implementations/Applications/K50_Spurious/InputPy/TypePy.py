from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, input_py: enums.InputSelect, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:TYPE \n
		Snippet: driver.applications.k50Spurious.inputPy.typePy.set(input_py = enums.InputSelect.INPut1, inputIx = repcap.InputIx.Default) \n
		The command selects the input path. \n
			:param input_py: INPUT1 Selects RF input 1. 1 mm [RF Input] connector INPUT2 Selects RF input 2. For R&S FSW85 models with two RF input connectors: 1.85 mm [RF2 Input] connector For all other models: not available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(input_py, enums.InputSelect)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.InputSelect:
		"""SCPI: INPut<ip>:TYPE \n
		Snippet: value: enums.InputSelect = driver.applications.k50Spurious.inputPy.typePy.get(inputIx = repcap.InputIx.Default) \n
		The command selects the input path. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: input_py: INPUT1 Selects RF input 1. 1 mm [RF Input] connector INPUT2 Selects RF input 2. For R&S FSW85 models with two RF input connectors: 1.85 mm [RF2 Input] connector For all other models: not available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.InputSelect)
