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

	def set(self, source: enums.TriggerSourceF) -> None:
		"""SCPI: TRIGger[:SEQuence]:SOURce \n
		Snippet: driver.applications.k9X11Ad.trigger.sequence.source.set(source = enums.TriggerSourceF.EXTernal) \n
		This command selects the trigger source. Note on external triggers: If a measurement is configured to wait for an
		external trigger signal in a remote control program, remote control is blocked until the trigger is received and the
		program can continue. Make sure this situation is avoided in your remote control programs. \n
			:param source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. If power splitter mode is active, this parameter activates the 'EXT TRIGGER INPUT' connector on the oscilloscope. Then the R&S FSW triggers when the signal fed into the 'EXT TRIGGER INPUT' connector on the oscilloscope meets or exceeds the specified trigger level. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For R&S FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'. RFPower First intermediate frequency (Frequency and time domain measurements only.) IFPower Second intermediate frequency IQPower Magnitude of sampled I/Q data For applications that process I/Q data, such as the I/Q Analyzer or optional applications.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceF)
		self._core.io.write(f'TRIGger:SEQuence:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerSourceF:
		"""SCPI: TRIGger[:SEQuence]:SOURce \n
		Snippet: value: enums.TriggerSourceF = driver.applications.k9X11Ad.trigger.sequence.source.get() \n
		This command selects the trigger source. Note on external triggers: If a measurement is configured to wait for an
		external trigger signal in a remote control program, remote control is blocked until the trigger is received and the
		program can continue. Make sure this situation is avoided in your remote control programs. \n
			:return: source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. If power splitter mode is active, this parameter activates the 'EXT TRIGGER INPUT' connector on the oscilloscope. Then the R&S FSW triggers when the signal fed into the 'EXT TRIGGER INPUT' connector on the oscilloscope meets or exceeds the specified trigger level. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For R&S FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'. RFPower First intermediate frequency (Frequency and time domain measurements only.) IFPower Second intermediate frequency IQPower Magnitude of sampled I/Q data For applications that process I/Q data, such as the I/Q Analyzer or optional applications."""
		response = self._core.io.query_str(f'TRIGger:SEQuence:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceF)
