from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: ExternalPort, default value after init: ExternalPort.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_externalPort_get', 'repcap_externalPort_set', repcap.ExternalPort.Nr1)

	def repcap_externalPort_set(self, externalPort: repcap.ExternalPort) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ExternalPort.Default
		Default value after init: ExternalPort.Nr1"""
		self._cmd_group.set_repcap_enum_value(externalPort)

	def repcap_externalPort_get(self) -> repcap.ExternalPort:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, level_external: float, triggerPort=repcap.TriggerPort.Default, externalPort=repcap.ExternalPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:LEVel[:EXTernal<ap>] \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.level.external.set(level_external = 1.0, triggerPort = repcap.TriggerPort.Default, externalPort = repcap.ExternalPort.Default) \n
		This command defines the level the external signal must exceed to cause a trigger event. \n
			:param level_external: No help available
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:param externalPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
		"""
		param = Conversions.decimal_value_to_str(level_external)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		externalPort_cmd_val = self._cmd_group.get_repcap_cmd_value(externalPort, repcap.ExternalPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:LEVel:EXTernal{externalPort_cmd_val} {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default, externalPort=repcap.ExternalPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:LEVel[:EXTernal<ap>] \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.level.external.get(triggerPort = repcap.TriggerPort.Default, externalPort = repcap.ExternalPort.Default) \n
		This command defines the level the external signal must exceed to cause a trigger event. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:param externalPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
			:return: level_external: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		externalPort_cmd_val = self._cmd_group.get_repcap_cmd_value(externalPort, repcap.ExternalPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:LEVel:EXTernal{externalPort_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
