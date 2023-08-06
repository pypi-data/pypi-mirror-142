from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Direction:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def set(self, direction: enums.InOutDirection, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut:TRIGger<2|3>:DIRection \n
		Snippet: driver.output.trigger.direction.set(direction = enums.InOutDirection.INPut, triggerPort = repcap.TriggerPort.Default) \n
		This command selects the trigger direction for trigger ports that serve as an input as well as an output. \n
			:param direction: INPut | OUTPut INPut Port works as an input. OUTPut Port works as an output.
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.InOutDirection)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut:TRIGger{triggerPort_cmd_val}:DIRection {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.InOutDirection:
		"""SCPI: OUTPut:TRIGger<2|3>:DIRection \n
		Snippet: value: enums.InOutDirection = driver.output.trigger.direction.get(triggerPort = repcap.TriggerPort.Default) \n
		This command selects the trigger direction for trigger ports that serve as an input as well as an output. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: direction: INPut | OUTPut INPut Port works as an input. OUTPut Port works as an output."""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut:TRIGger{triggerPort_cmd_val}:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.InOutDirection)
