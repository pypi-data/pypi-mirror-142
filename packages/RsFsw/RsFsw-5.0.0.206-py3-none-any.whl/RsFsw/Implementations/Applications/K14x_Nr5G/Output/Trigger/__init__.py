from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 6 total commands, 4 Subgroups, 1 group commands
	Repeated Capability: TriggerPort, default value after init: TriggerPort.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_triggerPort_get', 'repcap_triggerPort_set', repcap.TriggerPort.Nr1)

	def repcap_triggerPort_set(self, triggerPort: repcap.TriggerPort) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to TriggerPort.Default
		Default value after init: TriggerPort.Nr1"""
		self._cmd_group.set_repcap_enum_value(triggerPort)

	def repcap_triggerPort_get(self) -> repcap.TriggerPort:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def direction(self):
		"""direction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_direction'):
			from .Direction import Direction
			self._direction = Direction(self._core, self._cmd_group)
		return self._direction

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def otype(self):
		"""otype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_otype'):
			from .Otype import Otype
			self._otype = Otype(self._core, self._cmd_group)
		return self._otype

	@property
	def pulse(self):
		"""pulse commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pulse'):
			from .Pulse import Pulse
			self._pulse = Pulse(self._core, self._cmd_group)
		return self._pulse

	def set(self, level: enums.LowHigh, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut<xxx>:TRIGger<port> \n
		Snippet: driver.applications.k14Xnr5G.output.trigger.set(level = enums.LowHigh.HIGH, outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		No command help available \n
			:param level: No help available
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(level, enums.LowHigh)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> enums.LowHigh:
		"""SCPI: OUTPut<xxx>:TRIGger<port> \n
		Snippet: value: enums.LowHigh = driver.applications.k14Xnr5G.output.trigger.get(outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		No command help available \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: level: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
