from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Direction:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def set(self, direction: enums.InOutDirection, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut<up>:TRIGger<tp>:DIRection \n
		Snippet: driver.applications.k30NoiseFigure.output.trigger.direction.set(direction = enums.InOutDirection.INPut, outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		This command selects the trigger direction for trigger ports that serve as an input as well as an output. \n
			:param direction: INPut | OUTPut INPut Port works as an input. OUTPut Port works as an output.
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.InOutDirection)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}:DIRection {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> enums.InOutDirection:
		"""SCPI: OUTPut<up>:TRIGger<tp>:DIRection \n
		Snippet: value: enums.InOutDirection = driver.applications.k30NoiseFigure.output.trigger.direction.get(outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		This command selects the trigger direction for trigger ports that serve as an input as well as an output. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: direction: INPut | OUTPut INPut Port works as an input. OUTPut Port works as an output."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.InOutDirection)
