from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 8 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: SubBlock, default value after init: SubBlock.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subBlock_get', 'repcap_subBlock_set', repcap.SubBlock.Nr1)

	def repcap_subBlock_set(self, subBlock: repcap.SubBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubBlock.Default
		Default value after init: SubBlock.Nr1"""
		self._cmd_group.set_repcap_enum_value(subBlock)

	def repcap_subBlock_get(self) -> repcap.SubBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def preset(self):
		"""preset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import Preset
			self._preset = Preset(self._core, self._cmd_group)
		return self._preset

	@property
	def result(self):
		"""result commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def standard(self):
		"""standard commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import Standard
			self._standard = Standard(self._core, self._cmd_group)
		return self._standard

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
