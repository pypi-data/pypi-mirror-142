from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.TriggerSourceLte, mimoAntenna=repcap.MimoAntenna.Nr1) -> None:
		"""SCPI: TRIGger[:SEQuence]:SOURce<si> \n
		Snippet: driver.applications.k10Xlte.trigger.sequence.source.set(source = enums.TriggerSourceLte.BBPower, mimoAntenna = repcap.MimoAntenna.Nr1) \n
		This command selects the trigger source. Note on external triggers: If a measurement is configured to wait for an
		external trigger signal in a remote control program, remote control is blocked until the trigger is received and the
		program can continue. Make sure this situation is avoided in your remote control programs. \n
			:param source: IMMediate Free run (no trigger event to start a measurement) . EXTernal Measurement starts when the external trigger signal exceeds a certain level. Trigger signal from the 'Trigger In' connector. EXT2 Trigger signal from the 'Trigger Input / Output' connector. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'Trigger 3 Input / Output' connector. Note: Connector must be configured for 'Input'. RFPower Measurement starts when the first intermediate frequency exceeds a certain level. (Frequency and time domain measurements only.) Not available for input from the optional Digital Baseband Interface or the optional analog baseband Interface. IFPower Measurement starts when the second intermediate frequency exceeds a certain level. Not available for input from the optional digital baseband interface. For input from the optional analog baseband interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Measurement starts when the sampled I/Q data exceeds a certain magnitude. For applications that process I/Q data, such as the I/Q analyzer or optional applications. BBPower Measurement starts when the baseband power exceeds a certain level. For digital input via the optional digital baseband interface or the optional analog baseband interface. PSEN External power sensor GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q analyzer or optional applications, and only if the optional digital baseband interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general purpose bit (0 to 5) will provide the trigger data. TUNit If activated, the measurement is triggered by a connected R&S FS-Z11 trigger unit, simultaneously for all connected analyzers.
			:param mimoAntenna: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceLte)
		mimoAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoAntenna, repcap.MimoAntenna)
		self._core.io.write(f'TRIGger:SEQuence:SOURce{mimoAntenna_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, mimoAntenna=repcap.MimoAntenna.Nr1) -> enums.TriggerSourceLte:
		"""SCPI: TRIGger[:SEQuence]:SOURce<si> \n
		Snippet: value: enums.TriggerSourceLte = driver.applications.k10Xlte.trigger.sequence.source.get(mimoAntenna = repcap.MimoAntenna.Nr1) \n
		This command selects the trigger source. Note on external triggers: If a measurement is configured to wait for an
		external trigger signal in a remote control program, remote control is blocked until the trigger is received and the
		program can continue. Make sure this situation is avoided in your remote control programs. \n
			:param mimoAntenna: optional repeated capability selector. Default value: Nr1
			:return: source: IMMediate Free run (no trigger event to start a measurement) . EXTernal Measurement starts when the external trigger signal exceeds a certain level. Trigger signal from the 'Trigger In' connector. EXT2 Trigger signal from the 'Trigger Input / Output' connector. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'Trigger 3 Input / Output' connector. Note: Connector must be configured for 'Input'. RFPower Measurement starts when the first intermediate frequency exceeds a certain level. (Frequency and time domain measurements only.) Not available for input from the optional Digital Baseband Interface or the optional analog baseband Interface. IFPower Measurement starts when the second intermediate frequency exceeds a certain level. Not available for input from the optional digital baseband interface. For input from the optional analog baseband interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Measurement starts when the sampled I/Q data exceeds a certain magnitude. For applications that process I/Q data, such as the I/Q analyzer or optional applications. BBPower Measurement starts when the baseband power exceeds a certain level. For digital input via the optional digital baseband interface or the optional analog baseband interface. PSEN External power sensor GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q analyzer or optional applications, and only if the optional digital baseband interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general purpose bit (0 to 5) will provide the trigger data. TUNit If activated, the measurement is triggered by a connected R&S FS-Z11 trigger unit, simultaneously for all connected analyzers."""
		mimoAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoAntenna, repcap.MimoAntenna)
		response = self._core.io.query_str(f'TRIGger:SEQuence:SOURce{mimoAntenna_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceLte)
