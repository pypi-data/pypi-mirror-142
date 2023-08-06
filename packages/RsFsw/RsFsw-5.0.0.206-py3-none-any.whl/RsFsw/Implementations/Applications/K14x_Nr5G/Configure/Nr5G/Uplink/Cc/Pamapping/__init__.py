from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pamapping:
	"""Pamapping commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: AntennaPortConfig, default value after init: AntennaPortConfig.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pamapping", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPortConfig_get', 'repcap_antennaPortConfig_set', repcap.AntennaPortConfig.Nr1)

	def repcap_antennaPortConfig_set(self, antennaPortConfig: repcap.AntennaPortConfig) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPortConfig.Default
		Default value after init: AntennaPortConfig.Nr1"""
		self._cmd_group.set_repcap_enum_value(antennaPortConfig)

	def repcap_antennaPortConfig_get(self) -> repcap.AntennaPortConfig:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def pusch(self):
		"""pusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Pamapping':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pamapping(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
