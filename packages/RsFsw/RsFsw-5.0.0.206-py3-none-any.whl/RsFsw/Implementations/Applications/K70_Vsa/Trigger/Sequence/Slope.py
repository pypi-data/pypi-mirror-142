from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slope:
	"""Slope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slope", core, parent)

	def set(self, type_py: enums.SlopeType, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:SLOPe \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.slope.set(type_py = enums.SlopeType.NEGative, triggerPort = repcap.TriggerPort.Default) \n
		For all trigger sources except time you can define whether triggering occurs when the signal rises to the trigger level
		or falls down to it. \n
			:param type_py: POSitive | NEGative POSitive Triggers when the signal rises to the trigger level (rising edge) . NEGative Triggers when the signal drops to the trigger level (falling edge) .
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.SlopeType)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:SLOPe {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.SlopeType:
		"""SCPI: TRIGger<tp>[:SEQuence]:SLOPe \n
		Snippet: value: enums.SlopeType = driver.applications.k70Vsa.trigger.sequence.slope.get(triggerPort = repcap.TriggerPort.Default) \n
		For all trigger sources except time you can define whether triggering occurs when the signal rises to the trigger level
		or falls down to it. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: type_py: POSitive | NEGative POSitive Triggers when the signal rises to the trigger level (rising edge) . NEGative Triggers when the signal drops to the trigger level (falling edge) ."""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)
