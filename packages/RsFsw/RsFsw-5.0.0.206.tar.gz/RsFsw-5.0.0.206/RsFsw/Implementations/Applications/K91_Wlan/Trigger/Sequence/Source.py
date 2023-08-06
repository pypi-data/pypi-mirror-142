from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.TriggerSourceH) -> None:
		"""SCPI: TRIGger[:SEQuence]:SOURce \n
		Snippet: driver.applications.k91Wlan.trigger.sequence.source.set(source = enums.TriggerSourceH.AF) \n
		This command selects the trigger source. For details on the available trigger sources see 'Trigger Source'.
		Note on external triggers: If a measurement is configured to wait for an external trigger signal in a remote control
		program, remote control is blocked until the trigger is received and the program can continue. Make sure this situation
		is avoided in your remote control programs. \n
			:param source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For R&S FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'. RFPower First intermediate frequency (Frequency and time domain measurements only.) Not available for input from the optional Digital Baseband Interface or the optional Analog Baseband Interface. IFPower Second intermediate frequency Not available for input from the optional Digital Baseband Interface. For input from the optional Analog Baseband Interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Magnitude of sampled I/Q data For applications that process I/Q data, such as the I/Q Analyzer or optional applications. Not available for input from the optional Digital Baseband Interface or the optional Analog Baseband Interface. TIME Time interval BBPower Baseband power (for digital input via the optional Digital Baseband Interface Baseband power (for digital input via the optional Digital Baseband Interface or the optional Analog Baseband interface PSEN External power sensor GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q Analyzer or optional applications, and only if the optional Digital Baseband Interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general purpose bit (0 to 5) will provide the trigger data. The assignment of the general purpose bits used by the Digital IQ trigger to the LVDS connector pins is provided in 'Digital I/Q'. TUNit If activated, the measurement is triggered by a connected R&S FS-Z11 trigger unit, simultaneously for all connected analyzers. For details see 'Trigger synchronization using an R&S FS-Z11 trigger unit'.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceH)
		self._core.io.write(f'TRIGger:SEQuence:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerSourceH:
		"""SCPI: TRIGger[:SEQuence]:SOURce \n
		Snippet: value: enums.TriggerSourceH = driver.applications.k91Wlan.trigger.sequence.source.get() \n
		This command selects the trigger source. For details on the available trigger sources see 'Trigger Source'.
		Note on external triggers: If a measurement is configured to wait for an external trigger signal in a remote control
		program, remote control is blocked until the trigger is received and the program can continue. Make sure this situation
		is avoided in your remote control programs. \n
			:return: source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For R&S FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'. RFPower First intermediate frequency (Frequency and time domain measurements only.) Not available for input from the optional Digital Baseband Interface or the optional Analog Baseband Interface. IFPower Second intermediate frequency Not available for input from the optional Digital Baseband Interface. For input from the optional Analog Baseband Interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Magnitude of sampled I/Q data For applications that process I/Q data, such as the I/Q Analyzer or optional applications. Not available for input from the optional Digital Baseband Interface or the optional Analog Baseband Interface. TIME Time interval BBPower Baseband power (for digital input via the optional Digital Baseband Interface Baseband power (for digital input via the optional Digital Baseband Interface or the optional Analog Baseband interface PSEN External power sensor GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q Analyzer or optional applications, and only if the optional Digital Baseband Interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general purpose bit (0 to 5) will provide the trigger data. The assignment of the general purpose bits used by the Digital IQ trigger to the LVDS connector pins is provided in 'Digital I/Q'. TUNit If activated, the measurement is triggered by a connected R&S FS-Z11 trigger unit, simultaneously for all connected analyzers. For details see 'Trigger synchronization using an R&S FS-Z11 trigger unit'."""
		response = self._core.io.query_str(f'TRIGger:SEQuence:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceH)
