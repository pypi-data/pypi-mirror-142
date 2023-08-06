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

	def set(self, source: enums.BbInputSource, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<Undef>[:SELect] \n
		Snippet: driver.applications.k91Wlan.inputPy.select.set(source = enums.BbInputSource.AIQ, inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. For R&S FSW85 models with
		two RF input connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.
		InputPy.TypePy.set. Tip: The I/Q data to be analyzed for WLAN 802.11 can not only be measured by the R&S FSW WLAN
		application itself, it can also be imported to the application, provided it has the correct format. Furthermore, the
		analyzed I/Q data from the R&S FSW WLAN application can be exported for further analysis in external applications.
		For details, see the R&S FSW I/Q Analyzer and I/Q Input User Manual. \n
			:param source: RF Radio Frequency ('RF INPUT' connector) FIQ I/Q data file (selected by method RsFsw.Applications.K6_Pulse.InputPy.File.Path.set) For details, see 'Basics on input from I/Q data files'. Not available for Input2. DIQ Digital IQ data (only available with optional Digital Baseband Interface) For details on I/Q input see 'Digital Input'. Not available for Input2. AIQ Analog Baseband signal (only available with optional Analog Baseband Interface R&S FSW-B71) For details on Analog Baseband input see 'Processing Data From the Analog Baseband Interface'. Not available for Input2.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BbInputSource)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.BbInputSource:
		"""SCPI: INPut<Undef>[:SELect] \n
		Snippet: value: enums.BbInputSource = driver.applications.k91Wlan.inputPy.select.get(inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. For R&S FSW85 models with
		two RF input connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.
		InputPy.TypePy.set. Tip: The I/Q data to be analyzed for WLAN 802.11 can not only be measured by the R&S FSW WLAN
		application itself, it can also be imported to the application, provided it has the correct format. Furthermore, the
		analyzed I/Q data from the R&S FSW WLAN application can be exported for further analysis in external applications.
		For details, see the R&S FSW I/Q Analyzer and I/Q Input User Manual. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: source: RF Radio Frequency ('RF INPUT' connector) FIQ I/Q data file (selected by method RsFsw.Applications.K6_Pulse.InputPy.File.Path.set) For details, see 'Basics on input from I/Q data files'. Not available for Input2. DIQ Digital IQ data (only available with optional Digital Baseband Interface) For details on I/Q input see 'Digital Input'. Not available for Input2. AIQ Analog Baseband signal (only available with optional Analog Baseband Interface R&S FSW-B71) For details on Analog Baseband input see 'Processing Data From the Analog Baseband Interface'. Not available for Input2."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.BbInputSource)
