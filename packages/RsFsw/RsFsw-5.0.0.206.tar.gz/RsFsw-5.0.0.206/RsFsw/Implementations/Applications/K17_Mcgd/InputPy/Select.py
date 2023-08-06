from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, signal_source: enums.BbInputSource, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>:SELect \n
		Snippet: driver.applications.k17Mcgd.inputPy.select.set(signal_source = enums.BbInputSource.AIQ, inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input is supported. For R&S FSW85 models with two RF input
		connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.
		set. \n
			:param signal_source: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(signal_source, enums.BbInputSource)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.BbInputSource:
		"""SCPI: INPut<Undef>:SELect \n
		Snippet: value: enums.BbInputSource = driver.applications.k17Mcgd.inputPy.select.get(inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input is supported. For R&S FSW85 models with two RF input
		connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.
		set. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: signal_source: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.BbInputSource)
