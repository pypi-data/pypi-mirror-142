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

	def set(self, source: enums.ReferenceSourceD, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:SOURce \n
		Snippet: driver.applications.k30NoiseFigure.trigger.sequence.source.set(source = enums.ReferenceSourceD.EXT2, triggerPort = repcap.TriggerPort.Default) \n
		This command selects the trigger source. Note on external triggers: If a measurement is configured to wait for an
		external trigger signal in a remote control program, remote control is blocked until the trigger is received and the
		program can continue. Make sure this situation is avoided in your remote control programs. \n
			:param source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For R&S FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'.
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ReferenceSourceD)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.ReferenceSourceD:
		"""SCPI: TRIGger<tp>[:SEQuence]:SOURce \n
		Snippet: value: enums.ReferenceSourceD = driver.applications.k30NoiseFigure.trigger.sequence.source.get(triggerPort = repcap.TriggerPort.Default) \n
		This command selects the trigger source. Note on external triggers: If a measurement is configured to wait for an
		external trigger signal in a remote control program, remote control is blocked until the trigger is received and the
		program can continue. Make sure this situation is avoided in your remote control programs. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For R&S FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'."""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceSourceD)
