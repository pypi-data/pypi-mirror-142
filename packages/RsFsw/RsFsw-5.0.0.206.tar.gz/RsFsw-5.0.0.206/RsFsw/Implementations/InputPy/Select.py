from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, source: enums.InputSource, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:SELect \n
		Snippet: driver.inputPy.select.set(source = enums.InputSource.ABBand, inputIx = repcap.InputIx.Default) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input is supported. For R&S FSW85 models with two RF input
		connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.
		set. \n
			:param source: OBB Oscilloscope Baseband signal For details on Oscilloscope Baseband Input see 'Processing Oscilloscope Baseband Input'. Not available for Input2. RF Radio Frequency ('RF INPUT' connector) FIQ I/Q data file (selected by method RsFsw.Applications.K6_Pulse.InputPy.File.Path.set) For details, see 'Basics on Input from I/Q Data Files'. Not available for Input2. DIQ Digital IQ data (only available with optional Digital Baseband Interface) For details on I/Q input see 'Digital Input'. Not available for Input2. AIQ Analog Baseband signal (only available with optional Analog Baseband Interface R&S FSW-B71) For details on Analog Baseband input see 'Processing Data From the Analog Baseband Interface'. Not available for Input2.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.InputSource)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:SELect {param}')
