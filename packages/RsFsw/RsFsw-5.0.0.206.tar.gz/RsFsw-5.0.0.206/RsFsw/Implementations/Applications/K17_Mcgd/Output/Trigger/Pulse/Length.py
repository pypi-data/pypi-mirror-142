from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut:TRIGger<tp>:PULSe:LENGth \n
		Snippet: driver.applications.k17Mcgd.output.trigger.pulse.length.set(length = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		This command defines the length of the pulse generated at the trigger output. \n
			:param length: Pulse length in seconds. Unit: S
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(length)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut:TRIGger{triggerPort_cmd_val}:PULSe:LENGth {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: OUTPut:TRIGger<tp>:PULSe:LENGth \n
		Snippet: value: float = driver.applications.k17Mcgd.output.trigger.pulse.length.get(triggerPort = repcap.TriggerPort.Default) \n
		This command defines the length of the pulse generated at the trigger output. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: length: Pulse length in seconds. Unit: S"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut:TRIGger{triggerPort_cmd_val}:PULSe:LENGth?')
		return Conversions.str_to_float(response)
